import sys
from Editor import Editor
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class Notepad(QMainWindow):

    def __init__(self):
        super().__init__()

        self.editor = Editor()
        self.setCentralWidget(self.editor)
        self.init_ui()

    def init_ui(self):
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file = menu_bar.addMenu("File")

        new_action = QAction(QIcon('notebook.png'), 'New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction(QIcon('save.png'), 'Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction(QIcon('envelope.png'), '&Open', self)
        quit_action = QAction(QIcon('exit.png'), '&Quit', self)

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.response)

        self.setGeometry(300, 100, 800, 600)
        self.setWindowTitle("Simple Notepad Tool")
        self.show()

    def quit_trigger(self):
        qApp.quit()

    def response(self, action):
        signal = action.text()

        if signal == 'New':
            self.editor.clear_text()
        elif signal == 'Save':
            self.editor.save_text()
        elif signal == '&Open':
            self.editor.open()



app = QApplication(sys.argv)
win = Notepad()
sys.exit(app.exec_())
