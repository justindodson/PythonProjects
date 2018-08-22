# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog/newStudent.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class new_student_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 331)
        Dialog.setStyleSheet("#Dialog {\n"
"    background-color: rgb(34, 73, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 280, 171, 32))
        self.buttonBox.setStyleSheet("background-color: white;")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(29, 60, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 180, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 240, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 210, 91, 21))
        self.label_8.setObjectName("label_8")
        self.f_name = QtWidgets.QLineEdit(Dialog)
        self.f_name.setGeometry(QtCore.QRect(130, 30, 141, 21))
        self.f_name.setObjectName("f_name")
        self.site_name = QtWidgets.QLineEdit(Dialog)
        self.site_name.setGeometry(QtCore.QRect(130, 90, 141, 21))
        self.site_name.setObjectName("site_name")
        self.add_1 = QtWidgets.QLineEdit(Dialog)
        self.add_1.setGeometry(QtCore.QRect(130, 120, 141, 21))
        self.add_1.setObjectName("add_1")
        self.add_2 = QtWidgets.QLineEdit(Dialog)
        self.add_2.setGeometry(QtCore.QRect(130, 150, 141, 21))
        self.add_2.setObjectName("add_2")
        self.city = QtWidgets.QLineEdit(Dialog)
        self.city.setGeometry(QtCore.QRect(130, 180, 141, 21))
        self.city.setObjectName("city")
        self.zipcode = QtWidgets.QLineEdit(Dialog)
        self.zipcode.setGeometry(QtCore.QRect(130, 240, 141, 21))
        self.zipcode.setObjectName("zipcode")
        self.state = QtWidgets.QComboBox(Dialog)
        self.state.setGeometry(QtCore.QRect(130, 210, 141, 26))
        self.state.setObjectName("state")
        self.l_name = QtWidgets.QLineEdit(Dialog)
        self.l_name.setGeometry(QtCore.QRect(130, 60, 141, 21))
        self.l_name.setObjectName("l_name")

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Student"))
        self.label.setText(_translate("Dialog", "First Name"))
        self.label_2.setText(_translate("Dialog", "Last Name"))
        self.label_3.setText(_translate("Dialog", "Site Name"))
        self.label_4.setText(_translate("Dialog", "Address 2"))
        self.label_5.setText(_translate("Dialog", "Address 1"))
        self.label_6.setText(_translate("Dialog", "City"))
        self.label_7.setText(_translate("Dialog", "Zipcode"))
        self.label_8.setText(_translate("Dialog", "State"))

