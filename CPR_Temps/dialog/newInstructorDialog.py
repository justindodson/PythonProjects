# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newInstructorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_instructor_dialog(object):
    def setupUi(self, new_instructor_dialog):
        new_instructor_dialog.setObjectName("new_instructor_dialog")
        new_instructor_dialog.resize(373, 199)
        new_instructor_dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        new_instructor_dialog.setStyleSheet("QDialog{\n"
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
        self.create_instructor_btn = QtWidgets.QDialogButtonBox(new_instructor_dialog)
        self.create_instructor_btn.setGeometry(QtCore.QRect(190, 150, 164, 32))
        self.create_instructor_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.create_instructor_btn.setCenterButtons(True)
        self.create_instructor_btn.setObjectName("create_instructor_btn")
        self.instructor_id_input = QtWidgets.QLineEdit(new_instructor_dialog)
        self.instructor_id_input.setGeometry(QtCore.QRect(180, 80, 181, 21))
        self.instructor_id_input.setObjectName("instructor_id_input")
        self.line = QtWidgets.QFrame(new_instructor_dialog)
        self.line.setGeometry(QtCore.QRect(10, 120, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.first_name_input = QtWidgets.QLineEdit(new_instructor_dialog)
        self.first_name_input.setGeometry(QtCore.QRect(180, 20, 181, 21))
        self.first_name_input.setObjectName("first_name_input")
        self.label = QtWidgets.QLabel(new_instructor_dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(new_instructor_dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_3.setObjectName("label_3")
        self.last_name_input = QtWidgets.QLineEdit(new_instructor_dialog)
        self.last_name_input.setGeometry(QtCore.QRect(180, 50, 181, 21))
        self.last_name_input.setObjectName("last_name_input")
        self.label_5 = QtWidgets.QLabel(new_instructor_dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 101, 21))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(new_instructor_dialog)
        self.create_instructor_btn.rejected.connect(new_instructor_dialog.reject)
        self.create_instructor_btn.accepted.connect(new_instructor_dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(new_instructor_dialog)

    def retranslateUi(self, new_instructor_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_instructor_dialog.setWindowTitle(_translate("new_instructor_dialog", "Create New Class"))
        self.label.setText(_translate("new_instructor_dialog", "First Name:"))
        self.label_3.setText(_translate("new_instructor_dialog", "Last Name:"))
        self.label_5.setText(_translate("new_instructor_dialog", "Instructur ID #:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_instructor_dialog = QtWidgets.QDialog()
    ui = Ui_new_instructor_dialog()
    ui.setupUi(new_instructor_dialog)
    new_instructor_dialog.show()
    sys.exit(app.exec_())

