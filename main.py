import sys

import pytube
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from sampel import Ui_Form

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Form()
ui.setupUi(Dialog)
Dialog.show()
derectory_save = None


def Download():
    text = ui.textEdit.toPlainText()
    yt = pytube.YouTube(text)
    stream = yt.streams.get_highest_resolution()
    stream.download(derectory_save)


def Select_derectory():
    global derectory_save
    derectory_save = QFileDialog.getExistingDirectory()


ui.pushButton.clicked.connect(Download)
ui.pushButton_2.clicked.connect(Select_derectory)
sys.exit(app.exec_())
