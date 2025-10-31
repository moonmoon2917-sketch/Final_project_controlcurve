try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore,	QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import os
import importlib
from . import Util as util
importlib.reload(util)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ICON_PATH = os.path.join(BASE_DIR, 'icon')
FONT_PATH = os.path.join(BASE_DIR, 'font', 'Adobe Dia.ttf')
FONT_ICON_PATH = os.path.join(BASE_DIR, 'font', 'pixelfont_6.ttf')
IMAGE_PATH = BASE_DIR

class MakeControlCurve(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(533, 600)
		self.setWindowTitle('☆*: .｡.  Cute Control Curve  .｡.:*☆')
		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)
		
		# ภาพพื้นหลัง
		image_path = IMAGE_PATH.replace("\\", "/") + "/image/sky.jpg"
		self.setStyleSheet(f'''
				QDialog {{
					background-image: url("{image_path}");
					background-repeat: no-repeat;
					background-position: center;
					background-attachment: fixed;
					background-size: cover;
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6E8CFB, stop:1 #3C467B);
				}}
			''')

		# ภาพหัวข้อ
		self.imageLabel =QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{IMAGE_PATH}/image/moon.jpg")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(500,150),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.main_layout.addWidget(self.imageLabel)

		# โหลดฟ้อนต์
		font_id = QtGui.QFontDatabase.addApplicationFont(FONT_PATH)
		if font_id != -1:
			font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
			print(f"Loaded font: {font_family}")
		else:
			font_family = 'Papyrus'  # ฟ้อนต์สำรองถ้าโหลดไม่สำเร็จ
			print("Failed to load custom font, using Arial instead.")

		self.Jeab_listW = QtWidgets.QListWidget()
		self.Jeab_listW.setIconSize(QtCore.QSize(60, 60))
		self.Jeab_listW.setSpacing(8)
		self.Jeab_listW.setViewMode(QtWidgets.QListView.IconMode)
		self.Jeab_listW.setMovement(QtWidgets.QListView.Static)
		self.Jeab_listW.setResizeMode(QtWidgets.QListView.Adjust)
		self.Jeab_listW.setStyleSheet("background: rgba(5, 0, 76, 0.31); border: none;")
		self.main_layout.addWidget(self.Jeab_listW)

		self.jeab_ButLay = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.jeab_ButLay)
		self.Jeab_CreateBut = QtWidgets.QPushButton('🌕 Create')
		self.Jeab_CreateBut.clicked.connect(self.OnClick)
		self.Jeab_CreateBut.setFont(QtGui.QFont(font_family, 16, QtGui.QFont.Bold))
		self.Jeab_CreateBut.setStyleSheet(
			'''
				QPushButton {
				background-color: #000B58;
				color: #FEB21A;
				border-radius: 10px;
				padding: 5px; 
				font-size: 35px;
				font-weight: bold;
				}
				QPushButton:hover {
					background-color: #6E8CFB;
				}
				QPushButton:pressed {
					background-color: navy;
				}
			'''
			)
		self.Jeab_CancelBut = QtWidgets.QPushButton('Cancel 🌙')
		self.Jeab_CancelBut.clicked.connect(self.close)
		self.Jeab_CancelBut.setFont(QtGui.QFont(font_family, 16, QtGui.QFont.Bold))
		self.Jeab_CancelBut.setStyleSheet(
			'''
				QPushButton {
				background-color: #000B58;
				color: #FEB21A;
				border-radius: 10px;
				padding: 5px; 
				font-size: 35px;
				font-weight: bold;
				}
				QPushButton:hover {
					background-color: #6E8CFB;
				}
				QPushButton:pressed {
					background-color: navy;
				}
			'''
			)

		self.jeab_ButLay.addWidget(self.Jeab_CreateBut)
		self.jeab_ButLay.addWidget(self.Jeab_CancelBut)

		self.initIconWidgets()

	def initIconWidgets(self):
		prims = ['GF1', 'GF2', 'GF3', 'GF4', 'GF5', 'GF6', 'GF7', 
		'GF8', 'GF9', 'GF10', 'GF11', 'GF12', 'GF13', 'GF14', 
		'GF15', 'GF16', 'GF17', 'GF18', 'GF19', 'GF20', 'GF21', 
		'GF22', 'GF23', 'GF24', 'GF25', 'GF26', 'GF27', 'GF28']
		
		font_id2 = QtGui.QFontDatabase.addApplicationFont(FONT_ICON_PATH)
		families = QtGui.QFontDatabase.applicationFontFamilies(font_id2)[0]
		item_font = QtGui.QFont(families, 16, QtGui.QFont.Bold)
		
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{prim}.png')))
			item.setFont(item_font)
			self.Jeab_listW.addItem(item)

	def OnClick(self):
		util.ChangeSelectedShapeCurve(self.Jeab_listW)

def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MakeControlCurve(parent=ptr)
	ui.show()