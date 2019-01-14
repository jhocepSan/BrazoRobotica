from PySide.QtCore import *
from PySide.QtGui import *
import sys,CinDirec,CinInv

class Principal(QMainWindow):
	"""docstring for Principal"""
	def __init__(self, nombre):
		super(Principal, self).__init__()
		self.setWindowIcon(QIcon("img/logo.png"))
		self.nombre=str(nombre)
		self.setWindowTitle(self.nombre)
		self.setGeometry(100,100,700,500)
		self.statusBar().showMessage("Sistema de Control de un Braso")
		self.statusBar().setObjectName("infB")
		self.menu()
		self.show()
	def menu(self):
		self.menuBar().setObjectName("menu")
		cinematica=self.menuBar().addMenu(str('&Cinematica'))
		venDirecta = QAction(QIcon("img/directo.png"),"Cinematica &Directa", self,shortcut="Ctrl+D",
			statusTip="Cinematica Directa", triggered=lambda:self.loadDirecto())
		venInversa = QAction(QIcon("img/inverso.png"),"Cinematica &Inversa",self,shortcut="Ctrl+I",
			statusTip="Cinematica &Inversa",triggered=lambda:self.loadInverso())
		cinematica.addAction(venDirecta)
		cinematica.addAction(venInversa)
		sequimiento=self.menuBar().addMenu(str('&Sequimiento'))
		trayectoria=QAction(QIcon("img/trayectoria.png"),"Trayectorias",self,shortcut="Ctrl+T",
			statusTip="Sequimiento de Trayectorias",triggered=lambda:self.loadTrayectora())
		sequimiento.addAction(trayectoria)
		prueba=self.menuBar().addMenu(str('&Pruebas'))
		pruebas=QAction(QIcon("img/pruebas.png"),"General",self,shortcut="Ctrl+G",
			statusTip="Pruebas del Braso robotico",triggered=lambda:self.loadPruenba())
		prueba.addAction(pruebas)
		salir=QAction(QIcon("img/salir.png"),"Salir",self,shortcut="Ctrl+X",
			statusTip="Salir de la Aplicacion",triggered=lambda:self.salir())
		toolbarBox = QToolBar(self)
		toolbarBox.addAction(venDirecta)
		toolbarBox.addAction(venInversa)
		toolbarBox.addAction(trayectoria)
		toolbarBox.addAction(pruebas)
		toolbarBox.addSeparator()
		toolbarBox.addAction(salir)
		self.addToolBar(Qt.LeftToolBarArea, toolbarBox)
	def loadDirecto(self):
		cinDirec=CinDirec.CinDirec("Cinematica Directa")
		self.setCentralWidget(cinDirec)
	def loadInverso(self):
		cinInv=CinInv.CinInv("Cinematica Inversa")
		self.setCentralWidget(cinInv)
	def loadTrayectora(self):
		pass
	def loadPrueba(self):
		pass
	def salir(self):
		sys.exit()
def main():
	app=QApplication(sys.argv)
	ventana=Principal("Proyecto de Robotica")
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()