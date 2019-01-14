#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *

class CinInv(QWidget):
	"""docstring for CinInv"""
	def __init__(self, titulo):
		super(CinInv, self).__init__()
		self.titulo=QLabel(str(titulo),self)
		self.setGeometry(30,40,300,200)
		self.position()
	def position(self):
		self.titulo.setGeometry(10,10,100,40)

		