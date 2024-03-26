# Bismillahirrahmanirrahim
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from package.ui import mainWindow, env, vehicle, gearbox
from database import Environment_db,Gearbox_db,Vehicle_db

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
        gearbox_instance = Gearbox_db(
            gearbox_name="aryonddan geldik ",
            gear_ratio_list="3.21,2.85,2.5,2.2,1.7,1.4,3.2",
            differential_gear_ratio=2.9,
            powertrain_efficiency=78,
        )
        gearbox_instance.create_gearbox()
        self.gearboxWindow.close()
        print("şanzıman kaydettim")

    def onVehicleClicked(self):
        vehicle_instance = Vehicle_db(
            vehicle_name="aryonddan geldik",
            vehicle_mass=2500.0,
            c_aero=0.3,
            af_projection_area=5.0,
            rolling_resistance=0.01,
            r_dynamic_rolling=0.02,
        )
        vehicle_instance.create_vehicle()
        self.vehicleWindow.close()
        print("araç kaydettim")
        
    def onEnvClicked(self):
        environment_instance = Environment_db(
            environment_name="ben de aryonddan geldim",
            wind_speed=10,
            slope_angel_road=12,
            air_density=0.3,
            gravitational_force=9.8,
        )
        environment_instance.create_environment()
        self.envWindow.close()
        print("çevre kaydettim")
    

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ana_pencere = Pancar()
    ana_pencere.show()
    sys.exit(app.exec())

