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
        self.gearboxWindow=QtWidgets.QDialog()
        self.ui=gearbox.Ui_Sanziman()
        self.ui.setupUi(self.gearboxWindow)
        self.gearboxWindow.setModal(True)
        self.gearboxWindow.show()
        print("gearbox done")
        self.pushButton = self.gearboxWindow.findChild(QtWidgets.QPushButton, "sanziman_kaydet")
        self.pushButton.clicked.connect(self.onGearClicked)



    def openVehicle(self):
        self.vehicleWindow=QtWidgets.QDialog()
        self.ui=vehicle.Ui_Dialog()
        self.ui.setupUi(self.vehicleWindow)
        self.vehicleWindow.setModal(True)
        self.vehicleWindow.show()
        print("vehicle done")
        self.pushButton = self.vehicleWindow.findChild(QtWidgets.QPushButton, "arac_kaydet")
        self.pushButton.clicked.connect(self.onVehicleClicked)


    def openEnv(self):
        self.envWindow=QtWidgets.QDialog()
        self.ui=env.Ui_Cevre()
        self.ui.setupUi(self.envWindow)
        self.envWindow.setModal(True)
        self.envWindow.show()
        print("environment done")
        self.pushButton = self.envWindow.findChild(QtWidgets.QPushButton, "ortam_kaydet")
        self.pushButton.clicked.connect(self.onEnvClicked)

        
    def onGearClicked(self):
        self.gearboxWindow.close()
        print("şanzıman kaydettim")
    def onVehicleClicked(self):
        self.vehicleWindow.close()
        print("araç kaydettim")
    def onEnvClicked(self):
        self.envWindow.close()
        print("çevre kaydettim")
    

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ana_pencere = Pancar()
    ana_pencere.show()
    sys.exit(app.exec())

