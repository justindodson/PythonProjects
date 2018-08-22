# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newClassDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_class_build_dialog(object):
    def setupUi(self, class_build_dialog):
        class_build_dialog.setObjectName("class_build_dialog")
        class_build_dialog.resize(373, 285)
        class_build_dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        class_build_dialog.setStyleSheet("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(10, 21, 26, 255), stop:0.522167 rgba(20, 43, 51, 255), stop:1 rgba(25, 64, 81, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
" background-color: rgb(85, 127, 255);\n"
" color: white;\n"
"}\n"
"\n"
"QLabel {\n"
" color: white;\n"
"}")
        self.label_4 = QtWidgets.QLabel(class_build_dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 100, 26))
        self.label_4.setObjectName("label_4")
        self.create_class_btn = QtWidgets.QDialogButtonBox(class_build_dialog)
        self.create_class_btn.setGeometry(QtCore.QRect(190, 240, 164, 32))
        self.create_class_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.create_class_btn.setCenterButtons(True)
        self.create_class_btn.setObjectName("create_class_btn")
        self.layoutWidget = QtWidgets.QWidget(class_build_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 351, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.instructor_select = QtWidgets.QComboBox(self.layoutWidget)
        self.instructor_select.setObjectName("instructor_select")
        self.instructor_select.addItem("")
        self.instructor_select.addItem("")
        self.instructor_select.setItemText(1, "")
        self.horizontalLayout_2.addWidget(self.instructor_select)
        self.layoutWidget1 = QtWidgets.QWidget(class_build_dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 120, 351, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.class_hours = QtWidgets.QSpinBox(self.layoutWidget1)
        self.class_hours.setObjectName("class_hours")
        self.horizontalLayout_4.addWidget(self.class_hours)
        self.layoutWidget2 = QtWidgets.QWidget(class_build_dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 150, 351, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.class_size = QtWidgets.QSpinBox(self.layoutWidget2)
        self.class_size.setObjectName("class_size")
        self.horizontalLayout_3.addWidget(self.class_size)
        self.facility_input = QtWidgets.QLineEdit(class_build_dialog)
        self.facility_input.setGeometry(QtCore.QRect(190, 190, 171, 21))
        self.facility_input.setObjectName("facility_input")
        self.layoutWidget3 = QtWidgets.QWidget(class_build_dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 351, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.class_date = QtWidgets.QDateEdit(self.layoutWidget3)
        self.class_date.setCalendarPopup(True)
        self.class_date.setDate(QtCore.QDate(2018, 1, 1))
        self.class_date.setObjectName("class_date")
        self.horizontalLayout.addWidget(self.class_date)
        self.line = QtWidgets.QFrame(class_build_dialog)
        self.line.setGeometry(QtCore.QRect(10, 220, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.add_instructor_link = QtWidgets.QCommandLinkButton(class_build_dialog)
        self.add_instructor_link.setGeometry(QtCore.QRect(190, 80, 171, 31))
        self.add_instructor_link.setObjectName("add_instructor_link")
        self.create_class_btn.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_4.raise_()
        self.facility_input.raise_()
        self.line.raise_()
        self.add_instructor_link.raise_()

        self.retranslateUi(class_build_dialog)
        self.create_class_btn.rejected.connect(class_build_dialog.reject)
        self.create_class_btn.accepted.connect(class_build_dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(class_build_dialog)

    def retranslateUi(self, class_build_dialog):
        _translate = QtCore.QCoreApplication.translate
        class_build_dialog.setWindowTitle(_translate("class_build_dialog", "Create New Class"))
        self.label_4.setText(_translate("class_build_dialog", "Training Facility:"))
        self.label_3.setText(_translate("class_build_dialog", "Instructor:"))
        self.instructor_select.setItemText(0, _translate("class_build_dialog", "Select Instructor"))
        self.label_5.setText(_translate("class_build_dialog", "Class Hours:"))
        self.label_2.setText(_translate("class_build_dialog", "Class Size:"))
        self.label.setText(_translate("class_build_dialog", "Class Date:"))
        self.add_instructor_link.setText(_translate("class_build_dialog", "Add New Instructor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    class_build_dialog = QtWidgets.QDialog()
    ui = Ui_class_build_dialog()
    ui.setupUi(class_build_dialog)
    class_build_dialog.show()
    sys.exit(app.exec_())

