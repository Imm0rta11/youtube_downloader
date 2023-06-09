from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(461, 121)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(232, 80, 211, 31))
        self.pushButton.setStyleSheet("font: 13pt \"Gill Sans\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 121, 16))
        self.label.setStyleSheet("font: 13pt \"Gill Sans\";")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 211, 31))
        self.pushButton_2.setStyleSheet("font: 13pt \"Gill Sans\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 421, 31))
        self.textEdit.setStyleSheet("font: 13pt \"Gill Sans\";")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Downloader"))
        self.pushButton.setText(_translate("Form", "Download"))
        self.label.setText(_translate("Form", "URL youtube video:"))
        self.pushButton_2.setText(_translate("Form", "Select derectory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
