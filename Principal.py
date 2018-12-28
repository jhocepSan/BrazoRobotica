from PySide.QtCore import *
from PySide.QtGui import *
import sys

class Principal(QMainWindow):
	"""docstring for Principal"""
	def __init__(self, arg):
		super(Principal, self).__init__()
		self.setGeometry(100,100,500,400)
		self.arg = arg
		self.show()

def main():
	app=QApplication(sys.argv)
	ventana=Principal("Nombre")
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()