# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogGestorPersonal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(569, 548)
        Dialog.setMinimumSize(QtCore.QSize(569, 548))
        Dialog.setMaximumSize(QtCore.QSize(569, 548))
        Dialog.setWindowIcon(QtGui.QIcon("./graphics/icon.ico"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 40, 551, 16))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 261, 431))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tablaPersonal = QtGui.QTableWidget(self.groupBox)
        self.tablaPersonal.setGeometry(QtCore.QRect(10, 20, 241, 401))
        self.tablaPersonal.setProperty("showDropIndicator", False)
        self.tablaPersonal.setAlternatingRowColors(True)
        self.tablaPersonal.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaPersonal.setCornerButtonEnabled(True)
        self.tablaPersonal.setObjectName(_fromUtf8("tablaPersonal"))
        self.tablaPersonal.setColumnCount(2)
        self.tablaPersonal.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaPersonal.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaPersonal.setHorizontalHeaderItem(1, item)
        self.tablaPersonal.horizontalHeader().setStretchLastSection(True)
        self.tablaPersonal.verticalHeader().setVisible(False)
        self.tablaPersonal.verticalHeader().setStretchLastSection(False)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 60, 281, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(12, 20, 37, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.nombreNuevo = QtGui.QLineEdit(self.groupBox_2)
        self.nombreNuevo.setGeometry(QtCore.QRect(60, 20, 209, 20))
        self.nombreNuevo.setObjectName(_fromUtf8("nombreNuevo"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(12, 46, 42, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.apellidosNuevo = QtGui.QLineEdit(self.groupBox_2)
        self.apellidosNuevo.setGeometry(QtCore.QRect(60, 46, 209, 20))
        self.apellidosNuevo.setObjectName(_fromUtf8("apellidosNuevo"))
        self.addAPlantilla = QtGui.QPushButton(self.groupBox_2)
        self.addAPlantilla.setGeometry(QtCore.QRect(10, 80, 259, 23))
        self.addAPlantilla.setObjectName(_fromUtf8("addAPlantilla"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 270, 281, 221))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.turnosSeleccionada = QtGui.QTableWidget(self.groupBox_3)
        self.turnosSeleccionada.setGeometry(QtCore.QRect(10, 20, 261, 191))
        self.turnosSeleccionada.setAutoScroll(True)
        self.turnosSeleccionada.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.turnosSeleccionada.setObjectName(_fromUtf8("turnosSeleccionada"))
        self.turnosSeleccionada.setColumnCount(3)
        self.turnosSeleccionada.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.turnosSeleccionada.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.turnosSeleccionada.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.turnosSeleccionada.setHorizontalHeaderItem(2, item)
        self.turnosSeleccionada.horizontalHeader().setVisible(True)
        self.turnosSeleccionada.horizontalHeader().setDefaultSectionSize(50)
        self.turnosSeleccionada.horizontalHeader().setHighlightSections(False)
        self.turnosSeleccionada.horizontalHeader().setMinimumSectionSize(60)
        self.turnosSeleccionada.horizontalHeader().setStretchLastSection(True)
        self.turnosSeleccionada.verticalHeader().setStretchLastSection(False)
        self.aplicarButton = QtGui.QPushButton(Dialog)
        self.aplicarButton.setGeometry(QtCore.QRect(470, 510, 75, 23))
        self.aplicarButton.setObjectName(_fromUtf8("aplicarButton"))
        self.aceptarButton = QtGui.QPushButton(Dialog)
        self.aceptarButton.setGeometry(QtCore.QRect(390, 510, 75, 23))
        self.aceptarButton.setObjectName(_fromUtf8("aceptarButton"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(280, 180, 281, 81))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.eliminarButton = QtGui.QPushButton(self.groupBox_4)
        self.eliminarButton.setGeometry(QtCore.QRect(10, 20, 261, 23))
        self.eliminarButton.setObjectName(_fromUtf8("eliminarButton"))
        self.configTurnosNuevo = QtGui.QPushButton(self.groupBox_4)
        self.configTurnosNuevo.setGeometry(QtCore.QRect(10, 50, 261, 23))
        self.configTurnosNuevo.setObjectName(_fromUtf8("configTurnosNuevo"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Gestor de personal", None))
        self.label.setText(_translate("Dialog", "Gestor de personal", None))
        self.groupBox.setTitle(_translate("Dialog", "Plantilla", None))
        item = self.tablaPersonal.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nombre", None))
        item = self.tablaPersonal.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Apellidos", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Nuevo", None))
        self.label_2.setText(_translate("Dialog", "Nombre", None))
        self.label_3.setText(_translate("Dialog", "Apellidos", None))
        self.addAPlantilla.setText(_translate("Dialog", "Añadir a la plantilla", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Guardias activas", None))
        item = self.turnosSeleccionada.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Día", None))
        item = self.turnosSeleccionada.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Turno", None))
        item = self.turnosSeleccionada.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Especial", None))
        self.aplicarButton.setText(_translate("Dialog", "Aplicar", None))
        self.aceptarButton.setText(_translate("Dialog", "Aceptar", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Trabajador/a", None))
        self.eliminarButton.setText(_translate("Dialog", "Eliminar", None))
        self.configTurnosNuevo.setText(_translate("Dialog", "Modificar turnos", None))

