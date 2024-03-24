# Bismillahirrahmanirrahim
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from ui import mainWindow, env, vehicle, gearbox

class Pancar(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = mainWindow.Ui_VehicleDynamicsApp()
        self.ui.setupUi(self)

        self.ui.vehicle_entry.triggered.connect(self.openVehicle)
        self.ui.environment_entry.triggered.connect(self.openEnv)
        self.ui.gearbox_entry.triggered.connect(self.openGearbox)




    def openGearbox(self):
        self.window=QtWidgets.QDialog()
        self.ui=gearbox.Ui_Sanziman()
        self.ui.setupUi(self.window)
        self.window.show()
        print("gearbox done")

    def openVehicle(self):
        self.window=QtWidgets.QDialog()
        self.ui=vehicle.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


    def openEnv(self):
        self.window=QtWidgets.QDialog()
        self.ui=env.Ui_Cevre()
        self.ui.setupUi(self.window)
        self.window.show()
        print("environment done")

    

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ana_pencere = Pancar()
    ana_pencere.show()
    sys.exit(app.exec())

