"""
    NOTE: future refactor to abstract out the class, instructor, and student
          instances into their own classes and store the object references in
          the database. This will clean up the code a bit and make managing the
          objects much easier.

"""

import sys
import os
import sqlite3
from application.CPR_Temps import Ui_MainWindow
from PyQt5 import QtWidgets
from dialog.newClassDialog import Ui_class_build_dialog
from dialog.class_dialog import Ui_Dialog
from dialog.newInstructorDialog import Ui_new_instructor_dialog
from dialog.newStudent import new_student_Ui_Dialog
from resources.string_operators import find_string_space_index, cut_string_spaces
from resources.excel_extractor import ExcelData
from resources.state_populator import state_populator


class MainAppExec:

    def __init__(self):
        self.db = 'db/application_primary.db'
        self.create_database()
        self.print_db()

        app = QtWidgets.QApplication(sys.argv)

        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.populate_class_tree()


        # Button Click Function Calls
        self.ui.create_class_btn.clicked.connect(self.add_class)
        self.ui.open_class_btn.clicked.connect(self.open_class)
        # TODO:// Add double click action to tree items
        self.ui.batch_upload_btn.clicked.connect(self.create_new_students_from_batch)
        self.ui.new_student_btn.clicked.connect(self.add_new_single_student)

        self.main_window.show()
        sys.exit(app.exec_())


    """
        CLASS METHODS SECTION
    """

    # populate the class tree when window is loaded.
    # This method is called during the __init__ method
    def populate_class_tree(self):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM classes")
        classes = cursor.fetchall()
        index = 0
        for c_class in classes:
            self.ui.class_tree_widget.addTopLevelItem(QtWidgets.QTreeWidgetItem())
            self.ui.class_tree_widget.topLevelItem(index).setText(0, c_class[5])
            self.ui.class_tree_widget.topLevelItem(index).setText(1, c_class[1])
            self.ui.class_tree_widget.topLevelItem(index).setText(2, self.find_instructor_by_id(c_class[6]))
            index += 1
        connection.close()

    # creates the class form dialog box, collects the input data
    # and passes it to the create_new_class method to add the gathered
    # data into the db
    def add_class(self):
        class_build_dialog = QtWidgets.QDialog()
        ui = Ui_class_build_dialog()
        ui.setupUi(class_build_dialog)

        # populate the instructor combobox from db
        instructors = self.populate_instructor_list()
        for instructor in instructors:
            ui.instructor_select.addItem("{} {}".format(instructor[1], instructor[2]))

        # method to add new instructor into the combox and add into db
        ui.add_instructor_link.clicked.connect(lambda: self.add_instructor(ui))
        class_build_dialog.show()

        response = class_build_dialog.exec_()  # collect the response from the dialog OK or CANCEL buttons

        # if ok, grab all input data and create a new class row in db and add to class tree view
        if response == QtWidgets.QDialog.Accepted:
            date = ui.class_date.date().toPyDate()
            exp_date = ui.class_date.date().addYears(2).toPyDate()
            f_date = "{}/{}/{}".format(date.month, date.day, date.year)  # formatted date to needed format
            f_exp_date = "{}/{}/{}".format(exp_date.month, exp_date.day, exp_date.year)  # formatted exp_date
            size = ui.class_size.text()
            hours = ui.class_hours.text()
            instructor = ui.instructor_select.currentText()
            facility = ui.facility_input.text()
            self.create_new_class(f_date, f_exp_date, size, hours, instructor, facility)

    # load class data pulled from dialog form into the database and also populate
    # the tree view with the new class information so it shows immediately
    def create_new_class(self, date, exp_date, size, hours, instructor_name, training_facility):
        instructor = self.find_instructor_by_name(instructor_name)
        print(instructor)
        params = (str(date), str(exp_date), str(size), str(hours), training_facility, instructor[0])
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO classes VALUES (NULL, ?, ?, ?, ?, ?, ?)", params)
        connection.commit()
        connection.close()
        new_item = QtWidgets.QTreeWidgetItem()
        new_item.setText(0, training_facility)
        new_item.setText(1, date)
        new_item.setText(2, instructor_name)
        self.ui.class_tree_widget.addTopLevelItem(new_item)

    # open selected class and show data in the window
    def open_class(self):
        self.clear_table()
        if self.ui.class_tree_widget.currentItem() is not None:
            class_params = (self.ui.class_tree_widget.currentItem().text(0),
                            self.ui.class_tree_widget.currentItem().text(1))

            selected_class = self.find_class(class_params)
            instructor = self.find_instructor_by_name(self.ui.class_tree_widget.currentItem().text(2))
            self.ui.name_label.setText("{} {}".format(instructor[1], instructor[2]))
            self.ui.id_label.setText(instructor[3])

            self.ui.date_label.setText(selected_class[1])
            self.ui.size_label.setText(selected_class[3])
            self.ui.length_label.setText(selected_class[4])
            self.ui.facility_label.setText(selected_class[5])

            self.populate_student_table(selected_class[0])

        else:
            self.no_class_selected_dialog()

    # search for class, takes in tuple of db params to search by
    def find_class(self, class_params):
        try:
            if isinstance(class_params, tuple):
                connection = sqlite3.connect(self.db)
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM classes WHERE facility=? AND date=?", class_params)
                selected_class = cursor.fetchone()
                connection.close()
                return selected_class
        except ValueError:
            print("Argument must be a tuple")

    def no_class_selected_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    """
        INSTRUCTOR METHODS SECTION
    """

    # return a list of all instructors in db to populate the instructor combobox in the class creation ui
    def populate_instructor_list(self):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM instructors")
        instructors = cursor.fetchall()
        return instructors

    # load new instructor ui, grab input data, and create new instructor from data.
    # populate the combobox with added instructor
    def add_instructor(self, class_ui):
        new_instructor_dialog = QtWidgets.QDialog()
        ui = Ui_new_instructor_dialog()
        ui.setupUi(new_instructor_dialog)
        new_instructor_dialog.show()
        response = new_instructor_dialog.exec_()

        if response == QtWidgets.QDialog.Accepted:
            # call cut_string_spaces to ensure there are no added spaces at end of inputs.
            f_name = cut_string_spaces(ui.first_name_input.text())
            l_name = cut_string_spaces(ui.last_name_input.text())
            instructor_id = cut_string_spaces(ui.instructor_id_input.text())
            self.create_new_instructor(f_name, l_name, instructor_id, class_ui)
            print("{} {} ID #: {}".format(f_name, l_name, instructor_id))

    # Create new instructor and insert into db
    def create_new_instructor(self, f_name, l_name, instructor_id, class_ui):
        params = (f_name, l_name, instructor_id)
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO instructors VALUES (NULL, ?, ?, ?)", params)
        connection.commit()
        connection.close()
        class_ui.instructor_select.addItem("{} {}".format(f_name, l_name))

    # search for instructor in db by given name (both first and last as single string)
    def find_instructor_by_name(self, name):
        index = find_string_space_index(name)
        f_name = name[:index]
        l_name = name[index+1:]
        print("First: {} Last: {}".format(f_name, l_name))
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM instructors WHERE f_name=? AND l_name=?", (f_name, l_name))
        instructor = cursor.fetchone()
        connection.close()
        return instructor

    # search for instructor in db by given id
    def find_instructor_by_id(self, instructor_id):
        print(int(instructor_id))
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM instructors WHERE id=?", (instructor_id,))
        instructor = cursor.fetchone()
        connection.close()
        return "{} {}".format(instructor[1], instructor[2])

    """
        STUDENT METHODS SECTIONS
    """

    def open_batch_upload_file(self):

        filename = QtWidgets.QFileDialog.getOpenFileName(self.main_window, 'Opened File', os.getenv('HOME'))
        return filename[0]

    def create_new_students_from_batch(self):

        if self.ui.class_tree_widget.currentItem() is None:
            self.no_class_selected_dialog()
        else:
            class_params = (self.ui.class_tree_widget.currentItem().text(0),
                            self.ui.class_tree_widget.currentItem().text(1))
            selected_class = self.find_class(class_params)

            try:
                # TODO:// Create validation on file type/name
                file = self.open_batch_upload_file()
                if file is not '':
                    excel_extractor = ExcelData(selected_class[3], file)  # selected_class[3] retrieves the class size
                    counter = 1
                    while counter <= int(selected_class[3]):
                        new_student = excel_extractor.create_student(counter + 2)
                        self.student_class_many_to_many(self.create_new_student(*new_student)[0], selected_class[0])
                        counter += 1
            except ValueError:
                pass

    def create_new_student(self, f_name, l_name, site_name, add1, add2, city, state, zipcode):
        params = (f_name, l_name, site_name, add1, add2, city, state, zipcode)
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students VALUES (NULL, ?,?,?,?,?,?,?,?)", params)
        cursor.execute("SELECT * FROM students WHERE f_name = ? AND l_name = ?", (params[0], params[1]))
        student = cursor.fetchone()
        connection.commit()
        connection.close()
        return student
        # TODO:// add students to table dynamically

    def insert_student_into_table(self, student_params):
        self.ui.tableWidget.insertRow(0)
        item_counter = 0
        for col in range(self.ui.tableWidget.columnCount()):
            new_item = QtWidgets.QTableWidgetItem(student_params[item_counter])
            self.ui.tableWidget.setItem(0, col, new_item)
            item_counter += 1

    def student_list_by_class(self, class_id):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student_classes WHERE class_id = ?", str(class_id))
        student_list = cursor.fetchall()
        students = []

        for student in student_list:
            s_id = str(student[0])  # student[0] returns the student id of any given student
            cursor.execute("SELECT * FROM students WHERE id = ?", [s_id])
            students.append(cursor.fetchone())

        connection.close()
        return students

    def populate_student_table(self, class_id):

        students = self.student_list_by_class(class_id)

        for student in students:
            self.ui.tableWidget.insertRow(0)
            for col in range(1, len(student)):
                new_item = QtWidgets.QTableWidgetItem(student[col])
                self.ui.tableWidget.setItem(0, col - 1, new_item)

    def student_class_many_to_many(self, student_id, class_id):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO student_classes VALUES (?, ?)", (student_id, class_id))
        connection.commit()
        connection.close()

    def add_new_single_student(self):
        new_student_Dialog = QtWidgets.QDialog()
        ui = new_student_Ui_Dialog()
        ui.setupUi(new_student_Dialog)

        # populate the state selection combobox
        state_list = state_populator()
        for state in state_list:
            ui.state.addItem(state)

        new_student_Dialog.show()
        response = new_student_Dialog.exec_()

        if response == QtWidgets.QDialog.Accepted:
            if self.ui.class_tree_widget.currentItem() is None:
                self.no_class_selected_dialog()
            else:
                class_params = (self.ui.class_tree_widget.currentItem().text(0),
                                self.ui.class_tree_widget.currentItem().text(1))

                selected_class = self.find_class(class_params)
                student = self.create_new_student(ui.f_name.text(), ui.l_name.text(), ui.site_name.text(),
                                                  ui.add_1.text(), ui.add_2.text(), ui.city.text(),
                                                  ui.state.currentText(), ui.zipcode.text())
                self.student_class_many_to_many(student[0], selected_class[0])
                self.clear_table()
                self.populate_student_table(selected_class[0])
    """
        DATABASE METHODS SECTIONS
    """

    # create the db
    def create_database(self):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()

        class_table = """CREATE TABLE IF NOT EXISTS classes(
                            id integer PRIMARY KEY,
                            date text NOT NULL,
                            exp_date text NOT NULL,
                            class_size text NOT NULL,
                            class_hours text NOT NULL,
                            facility text NOT NULL,
                            instructor_id integer NOT NULL,
                            FOREIGN KEY(instructor_id) REFERENCES instructors(id)                            
                            )"""
        instructor_table = """CREATE TABLE IF NOT EXISTS instructors (
                            id integer PRIMARY KEY,
                            f_name text NOT NULL,
                            l_name text NOT NULL,
                            instructor_id text NOT NULL
                            )"""
        student_table = """CREATE TABLE IF NOT EXISTS students(
                            id integer PRIMARY KEY,
                            f_name text NOT NULL,
                            l_name text NOT NULL,
                            site_name text,
                            address1 text,
                            address2 text, 
                            city text,
                            state text,
                            zipcode text
                            )"""
        student_class_table = """CREATE TABLE IF NOT EXISTS student_classes(
                            student_id integer,
                            class_id integer,
                            FOREIGN KEY(student_id) REFERENCES students(id),
                            FOREIGN KEY(class_id) REFERENCES classes(id)
                            )"""

        cursor.execute(class_table)
        cursor.execute(instructor_table)
        cursor.execute(student_table)
        cursor.execute(student_class_table)

        connection.commit()
        connection.close()

    # used during debugging the db and app data creation
    def print_db(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM classes")
        rows = cur.fetchall()
        print("***** CLASSES TABLE *****")
        for row in rows:
            print(row)

        cur.execute("SELECT * FROM instructors")
        rows = cur.fetchall()
        print("***** INSTRUCTORS TABLE *****")
        for row in rows:
            print(row)

        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        print("***** STUDENTS TABLE *****")
        for row in rows:
            print(row)

        cur.execute("SELECT * FROM student_classes")
        rows = cur.fetchall()
        print("******* STUDENT CLASSES M2M *********")
        for row in rows:
            print(row)
        conn.close()

    def clear_table(self):
        self.ui.tableWidget.setRowCount(0)

if __name__ == '__main__':
    MainAppExec()
