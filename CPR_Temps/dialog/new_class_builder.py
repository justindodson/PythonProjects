import sys
from application.CPR_Temps import Ui_MainWindow
from PyQt5 import QtWidgets

from dialog.newClassDialog import Ui_class_build_dialog


class ClassBuilderExec():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        class_build_dialog = QtWidgets.QDialog()
        self.ui = Ui_class_build_dialog()
        self.ui.setupUi(class_build_dialog)

        class_build_dialog.show()
        sys.exit(app.exec_())



if __name__ == '__main__':
    ClassBuilderExec()