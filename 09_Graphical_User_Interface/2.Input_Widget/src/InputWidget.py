# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(505, 300)
        font = QtGui.QFont()
        font.setPointSize(28)
        Form.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 52, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 52, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 60, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setCursorPosition(1)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(210, 30, 281, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(80, 90, 113, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setMinimumDate(QtCore.QDate(1752, 9, 14))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(77, 120, 121, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.submitState)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.textEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "Age"))
        self.label_3.setText(_translate("Form", "Birthday"))
        self.lineEdit_2.setInputMask(_translate("Form", "999"))
        self.pushButton.setText(_translate("Form", "Clear"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
    
    def submitState(self):
        name=self.lineEdit.text()
        age=self.lineEdit_2.text()
        date=self.dateEdit.date()
        data = str(name) + " " +str(age)+" "+str(date.toString())
        self.textEdit.append(data)
        print(data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
