#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *

class CinDirec(QWidget):
	"""docstring for CinDirec"""
	def __init__(self,titulo):
		super(CinDirec, self).__init__()
		self.setGeometry(30,30,300,200)
		self.titulo=QLabel(str(titulo),self)
		self.myLabel()
		self.myLine()
		self.botones()
		self.position()
	def myLabel(self):
		self.anguloBase=QLabel(u"Angulo Base α :",self)
		self.anguloHom=QLabel(u"Angulo Hombro Ө :",self)
		self.anguloCod=QLabel(u"Angulo Codo β :",self)
		self.img=QLabel(self)
		self.img.setPixmap(QPixmap.fromImage(QImage("img/cinDir.jpg")).scaled(200, 200,Qt.KeepAspectRatio))
	def botones(self):
		
	def myLine(self):
		self.alfa=QSpinBox(self)
		self.alfa.setMinimum(0)
		self.alfa.setMaximum(180)
		self.tita=QSpinBox(self)
		self.tita.setMinimum(0)
		self.tita.setMaximum(180)
		self.beta=QSpinBox(self)
		self.beta.setMinimum(0)
		self.beta.setMaximum(180)
	def position(self):
		self.titulo.setGeometry(10,10,100,40)
		self.anguloBase.setGeometry(10,60,100,40)
		self.anguloHom.setGeometry(10,120,100,40)
		self.anguloCod.setGeometry(10,180,100,40)
		self.alfa.setGeometry(130,60,100,40)
		self.tita.setGeometry(130,120,100,40)
		self.beta.setGeometry(130,180,100,40)
		self.img.setGeometry(250,40,200,200)