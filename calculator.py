from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc import Ui_Form
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#knopki
def bp():
	ui.lineEdit.setText(" 1 ")


ui.pushButton_6.clicked.connect( bp )


sys.exit(app.exec_())