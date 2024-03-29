# Copyright Ramón Vila Ferreres
# ramonvilafer <at> gmail.com - 2019

import os
import pickle
import pprint
import shutil
import sys

from arrow import *
from PyQt4 import *
from PyQt4 import QtCore, QtGui

from CommonUtils import CommonUtils
from SocratesUI.DialogEditorTurnosPorEmpleado import \
    Ui_Dialog as Ui_DialogEditorTurnos
from windows import (DialogEditorTurnos, DialogGestorPersonal,
                     DialogPrimerInicio, DialogResSemestral, MainWindow)


class DialogEditorTurnos(QtGui.QDialog, Ui_DialogEditorTurnos, object):
   
    def __init__(self, selectedIndex, parent = None):

        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)
        
        self.userData = ""
        self.index = selectedIndex

        self.loadData()
        self.haGuardado = True

        self.trabajadorSeleccionado = self.userData["trabajadores"][self.index]
        self.calendarioDia = self.dateEdit.calendarWidget()
        
        # Por defecto se carga la fecha actual
        self.diaSeleccionado = Arrow.now()
        self.calendarioDia.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarioDia.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish))
        self.calendarioDia.setSelectedDate(CommonUtils.arrowToQdate(self.diaSeleccionado))
        self.calendarioDia.showSelectedDate()

        self.labelNombre.setText(self.trabajadorSeleccionado["nombre"])
        self.labelApellidos.setText(self.trabajadorSeleccionado["apellidos"])

        self.refrescarTodo()

        self.addButton.clicked.connect(self.anadirTurno)
        self.botonOk.clicked.connect(self.closeWindow)
        self.botonAplicar.clicked.connect(self.aplicarCambios)
        self.calendarioDia.clicked.connect(self.refrescarTodo)
        self.eliminarButton.clicked.connect(self.eliminarTurno)
    
    def closeWindow(self):
        if self.haGuardado == False:
            respuesta = CommonUtils.showMessageBox("Alerta", "Guardado", 
            "Has realizado cambios pero no los has guardado, ¿Quieres guardarlos?", 
            QtGui.QMessageBox.Warning)
            
            if respuesta == QtGui.QMessageBox.Ok:
                self.aplicarCambios()
            elif respuesta == QtGui.QMessageBox.Cancel:
                self.close()
        else:
            self.close()
    
    def aplicarCambios(self):
        CommonUtils.showMessageBox("Guardado", "Correcto", 
        "Los datos se han actualizado correctamente")

        CommonUtils.updateUserData(self.userData)
        self.haGuardado = True

    def loadData(self):
        self.userData = CommonUtils.getUserData()

    def anadirTurno(self):
        fecha = CommonUtils.qdateToArrow(self.dateEdit.date())
        tipoTurno = self.comboTurno.currentText()
        self.nuevoTurnoATrabajador(fecha, tipoTurno)
        self.refrescarTodo()

        self.haGuardado = False

    def eliminarTurno(self):
        rowIndex = self.guardiasTable.currentRow()
        self.guardiasTable.removeRow(rowIndex)

        del self.trabajadorSeleccionado["turnos"][rowIndex]
        CommonUtils.updateUserData(self.userData)

        self.haGuardado = False

    def nuevoTurnoATrabajador(self, date, tipo):
        turno = (f"{date.day}/{date.month}/{date.year}", tipo)

        self.trabajadorSeleccionado["turnos"].append(turno)
        CommonUtils.updateUserData(self.userData)

        self.haGuardado = False
    
    def cargarTablaTurnos(self):
        trabajadorSeleccionado = self.trabajadorSeleccionado
        turnosSeleccionados = trabajadorSeleccionado["turnos"]

        pprint.pprint(turnosSeleccionados, indent=4)

        totalTurnosValidos = 0
        turnosValidos = []

        for turno in turnosSeleccionados:
            # Si el mes actual y el del turno coinciden
            if (self.diaSeleccionado.month == CommonUtils.dateTupleToArrow(turno).month):
                totalTurnosValidos += 1
                turnosValidos.append(turno)

        # Resize table
        self.guardiasTable.setRowCount(totalTurnosValidos) 
 
        for numeroDeTurno in range(len(turnosValidos)):
            turnoActual = turnosValidos[numeroDeTurno]
            arrowDiaActual = CommonUtils.dateTupleToArrow(turnoActual)

            # Establecer el Nombre y apellido
            self.guardiasTable.setItem(numeroDeTurno, 0, QtGui.QTableWidgetItem(
                CommonUtils.formatForTable(f"{CommonUtils.getWeekDayName(arrowDiaActual.weekday())} {arrowDiaActual.day}")))

            self.guardiasTable.setItem(numeroDeTurno, 1, QtGui.QTableWidgetItem(CommonUtils.formatForTable(turnoActual[1])))
            self.guardiasTable.setItem(numeroDeTurno, 2, QtGui.QTableWidgetItem(
                CommonUtils.formatForTable(CommonUtils.esFechaEspecial(arrowDiaActual))))

            # Ajustar el tamaño de las columnas para que quepa todo el texto
            self.guardiasTable.resizeColumnsToContents()

    def refrescarTodo(self):
        self.diaSeleccionado = CommonUtils.qdateToArrow(self.calendarioDia.selectedDate())
        self.cargarTablaTurnos()
