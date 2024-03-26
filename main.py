# Bismillahirrahmanirrahim
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from package.ui import mainWindow, env, vehicle, gearbox
from database import Environment_db,Gearbox_db,Vehicle_db
# from PySide6.QtWidgets import QMessageBox
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
        # self.sanziman_ismi=self.gearboxWindow.sanziman_ismi.text()
        sanziman_ismi=self.ui.sanziman_ismi.text()
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

    # def onGearClicked(self):
    #     sanziman_ismi=self.ui.sanziman_ismi.text()
    #     vites_oranlari=self.ui.vites_oranlari.text()
    #     dif_oran=self.ui.dif_oran.text()
    #     ao_verimi=self.ui.ao_verimi.text()
    #     gearbox_instance = Gearbox_db(
    #         gearbox_name=sanziman_ismi,
    #         gear_ratio_list=vites_oranlari,
    #         differential_gear_ratio=dif_oran,
    #         powertrain_efficiency=ao_verimi,
    #     )
    #     gearbox_instance.create_gearbox()
    #     self.gearboxWindow.close()     

    def onGearClicked(self):
        try:
            sanziman_ismi = self.ui.sanziman_ismi.text()
            vites_oranlari = self.ui.vites_oranlari.text()
            dif_oran = self.ui.dif_oran.text()
            ao_verimi = self.ui.ao_verimi.text()

            gearbox_instance = Gearbox_db(
                gearbox_name=sanziman_ismi,
                gear_ratio_list=vites_oranlari,
                differential_gear_ratio=dif_oran,
                powertrain_efficiency=ao_verimi,
            )
            gearbox_instance.create_gearbox()
            self.gearboxWindow.close()

            print("Şanzıman kaydedildi")
        except Exception as e:
            print("Hata:", e)
            reply = QMessageBox()
            reply.setText("Eksik veya hatalı bilgi girdiniz")
            reply.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = reply.exec()
            if x == QMessageBox.StandardButton.Ok:
                print("OK düğmesine tıklandı")
        print("şanzıman kaydettim")
        
    def onVehicleClicked(self):
        arac_ismi=self.ui.arac_ismi.text()
        arac_kutlesi=self.ui.arac_kutlesi.text()
        cf_aero=self.ui.cf_aero.text()
        izdusum_alan=self.ui.izdusum_alan.text()
        yuvarlanma_direnc=self.ui.yuvarlanma_direnc.text()
        teker_efektif_r=self.ui.teker_efektif_r.text()
        vehicle_instance = Vehicle_db(
            vehicle_name=arac_ismi,
            vehicle_mass=arac_kutlesi,
            c_aero=cf_aero,
            af_projection_area=izdusum_alan,
            rolling_resistance=yuvarlanma_direnc,
            r_dynamic_rolling=teker_efektif_r,
        )
        vehicle_instance.create_vehicle()
        self.vehicleWindow.close()
        print("araç kaydettim")
        
    def onEnvClicked(self):
        cevre_isim=self.ui.cevre_isim.text()
        ruzgar_hizi=self.ui.ruzgar_hizi.text()
        yol_egimi=self.ui.yol_egimi.text()
        hava_yogunlugu=self.ui.hava_yogunlugu.text()
        yercekimi=self.ui.yercekimi.text()
        environment_instance = Environment_db(
            environment_name=cevre_isim,
            wind_speed=ruzgar_hizi,
            slope_angel_road=yol_egimi,
            air_density=hava_yogunlugu,
            gravitational_force=yercekimi,
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

