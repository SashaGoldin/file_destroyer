from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from pathlib import Path


def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select files")
    message.setText('\n'.join(filenames))


def delete_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, "wb") as file:
            file.write(b'')
        path.unlink()
    message.setText("Destruction was successful!")


app = QApplication([])

window = QWidget()
window.setWindowTitle("File Destroyer")
layout = QVBoxLayout()

description = QLabel('Select the files you want to <b>destroy</b>. The files will be '
                     '<font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton("Open Files")
open_btn.setToolTip('Open Files')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton("Destroy Files")
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(delete_files)

message = QLabel("")
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)
window.setLayout(layout)
window.show()
app.exec()
