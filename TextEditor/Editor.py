import sys
import os
from PyQt5.QtWidgets import (QWidget, QTextEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QFileDialog)


class Editor(QWidget):

    def __init__(self):
        super().__init__()

        self.text = QTextEdit(self)
        self.save_btn = QPushButton("Save")
        self.clr_btn = QPushButton("Clear")
        self.opn_btn = QPushButton("Open")

        self.init_ui()
        self.actions()

    def init_ui(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.opn_btn)
        h_layout.addWidget(self.save_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)


    def actions(self):
        self.save_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open)

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as file:
            text = self.text.toPlainText()
            file.write(text)

    def clear_text(self):
        self.text.clear()

    def open(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as file:
            text = file.read()
            self.text.setText(text)
