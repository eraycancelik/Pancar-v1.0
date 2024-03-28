# Bismillahirrahmanirrahim
from PyQt6 import QtWidgets
from package.ui import mainWindow, engine, env, vehicle, gearbox
from database import Environment_db,Gearbox_db,Vehicle_db
from utils import is_numeric,is_valid
import os
class Pancar(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = mainWindow.Ui_VehicleDynamicsApp()
        self.ui.setupUi(self)
        
    
        self.engine_tork_speed_list=self.ui.engine_torque_speed_list
        self.gearbox_list=self.ui.gearbox_list
        self.vehicle_list=self.ui.vehicle_list
        self.environment_list=self.ui.environment_list
    
        
    ################################################################### SIGNALS ###################################################################
        self.ui.vehicle_entry.triggered.connect(self.openVehicle)
        self.ui.environment_entry.triggered.connect(self.openEnv)
        self.ui.gearbox_entry.triggered.connect(self.openGearbox)
        self.ui.engine_entry.triggered.connect(self.openEngine)
        self.ui.gearbox_list_delete_button.clicked.connect(self.delete_gearbox)
        self.ui.env_list_delete_button.clicked.connect(self.delete_environment)
        self.ui.vehicle_list_delete_button.clicked.connect(self.delete_vehicle)
    ###############################################################################################################################################





    #################################################################### SLOTS ####################################################################
    
    
                                                        ##### LISTE ISLEMLERI #####
    def update_gearbox_list(self):
        gearbox_db = Gearbox_db()
        query_result = gearbox_db.get_gearboxes()
        self.gearbox_list.clear()
        if query_result:
            for gearbox in query_result:
                item_text = gearbox.gearbox_name
                list_item = QtWidgets.QListWidgetItem(item_text)
                self.gearbox_list.addItem(list_item)
        else:
            self.gearbox_list.addItem("Şanzıman kaydı bulunamadı.")
            
    def update_environment_list(self):
        environments_db=Environment_db()
        query_result = environments_db.get_environments()
        self.environment_list.clear()
        if query_result:
            for item in query_result:
                item_text = item.environment_name
                list_item = QtWidgets.QListWidgetItem(item_text)
                self.environment_list.addItem(list_item)
        else:
            self.environment_list.addItem("Ortam kaydı bulunamadı.")

    def update_vehicle_list(self):
        vehicle_db=Vehicle_db()
        query_result = vehicle_db.get_vehicles()
        self.vehicle_list.clear()
        if query_result:
            for item in query_result:
                item_text = item.vehicle_name
                list_item = QtWidgets.QListWidgetItem(item_text)
                self.vehicle_list.addItem(list_item)
        else:
            self.vehicle_list.addItem("Ortam kaydı bulunamadı.")
    
        
    def delete_gearbox(self):
        current_item = self.gearbox_list.currentItem()
        query=Gearbox_db()
        if current_item is not None:
            query.delete_gearbox(gearbox=current_item.text())
            print(f"{current_item.text()} is deleted")
        else:
            print("Herhangi bir öğe seçilmedi.")
        self.update_gearbox_list()
        
    def delete_environment(self):
        current_item = self.environment_list.currentItem()
        query=Environment_db()
        if current_item is not None:
            query.delete_environment(environment=current_item.text())
            print(f"{current_item.text()} is deleted")
        else:
            print("Herhangi bir öğe seçilmedi.")
        self.update_environment_list()
        
    def delete_vehicle(self):
        current_item = self.vehicle_list.currentItem()
        query=Vehicle_db()
        if current_item is not None:
            query.delete_vehicle(vehicle=current_item.text())
            print(f"{current_item.text()} is deleted")
        else:
            print("Herhangi bir öğe seçilmedi.")
        self.update_vehicle_list()

    def openEngine(self):
        self.engineWindow=QtWidgets.QDialog()
        self.ui=engine.Ui_Dialog()
        self.ui.setupUi(self.engineWindow)
        self.engineWindow.setModal(True)
        self.engineWindow.show()
        print("engine done")
        self.pushButton = self.engineWindow.findChild(QtWidgets.QPushButton, "kaydet")
        self.secPushButton = self.engineWindow.findChild(QtWidgets.QPushButton, "sec")
        self.secPushButton.clicked.connect(self.file)
        self.pushButton.clicked.connect(self.onEngineClicked)
        print("engine clicked")
        
    def onEngineClicked(self):
        print()
    
    def file(self):
        file_filter="Excel File (*.xlsx *.xls);"
        response=QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Motor hız-tork tablosu",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter="Excel File (*.xlsx *.xls)"
        )
        path=str(response[0])
        self.ui.label_3.setText(path)
        
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
        sanziman_ismi = self.ui.sanziman_ismi.text()
        vites_oranlari = self.ui.vites_oranlari.text()
        dif_oran = self.ui.dif_oran.text()
        ao_verimi = self.ui.ao_verimi.text()

        if not sanziman_ismi or not vites_oranlari or not dif_oran or not ao_verimi:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Tüm alanları doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
        elif is_valid(vites_oranlari) and is_numeric(dif_oran) and is_numeric(ao_verimi):
            gearbox_instance = Gearbox_db(
                gearbox_name=sanziman_ismi,
                gear_ratio_list=vites_oranlari,
                differential_gear_ratio=dif_oran,
                powertrain_efficiency=ao_verimi,
            )
            gearbox_instance.create_gearbox()
            self.gearboxWindow.close()
            self.update_gearbox_list()
            print("Şanzıman kaydedildi")  
            msg=QtWidgets.QMessageBox.information(
                self,
                "Başarılı",
                f"{sanziman_ismi} başarıyla kaydedilmiştir   ",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
            print("araç kaydettim")
        
        else:
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "İlgili alanları yalnızca sayısal değerlerle doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
                                  

    def onVehicleClicked(self):
        arac_ismi=self.ui.arac_ismi.text()
        arac_kutlesi=self.ui.arac_kutlesi.text()
        cf_aero=self.ui.cf_aero.text()
        izdusum_alan=self.ui.izdusum_alan.text()
        yuvarlanma_direnc=self.ui.yuvarlanma_direnc.text()
        teker_efektif_r=self.ui.teker_efektif_r.text()
        if  not arac_kutlesi or not cf_aero or not izdusum_alan or not yuvarlanma_direnc or not teker_efektif_r:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Tüm alanları doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
        elif is_numeric(arac_kutlesi) and is_numeric(cf_aero) and is_numeric(izdusum_alan) and is_numeric(yuvarlanma_direnc) and is_numeric(teker_efektif_r):
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
            self.update_vehicle_list()
            msg=QtWidgets.QMessageBox.information(
                self,
                "Başarılı",
                f"{arac_ismi} aracı başarıyla kaydedilmiştir   ",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
            print("araç kaydettim")
        
        else:
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "İlgili alanları yalnızca sayısal değerlerle doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return

    def onEnvClicked(self):
        cevre_isim=self.ui.cevre_isim.text()
        ruzgar_hizi=self.ui.ruzgar_hizi.text()
        yol_egimi=self.ui.yol_egimi.text()
        hava_yogunlugu=self.ui.hava_yogunlugu.text()
        yercekimi=self.ui.yercekimi.text()
        if  not cevre_isim or not ruzgar_hizi or not yol_egimi or not hava_yogunlugu or not yercekimi:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Tüm alanları doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
        elif is_numeric(ruzgar_hizi) and is_numeric(yol_egimi) and is_numeric(hava_yogunlugu) and is_numeric(yercekimi) :
            environment_instance = Environment_db(
            environment_name=cevre_isim,
            wind_speed=ruzgar_hizi,
            slope_angel_road=yol_egimi,
            air_density=hava_yogunlugu,
            gravitational_force=yercekimi,
        )
            environment_instance.create_environment()
            self.envWindow.close()
            self.update_environment_list()
            msg=QtWidgets.QMessageBox.information(
                self,
                "Başarılı",
                f"{cevre_isim} ortamı başarıyla kaydedilmiştir   ",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
            print("araç kaydettim")
        
        else:
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "İlgili alanları yalnızca sayısal değerlerle doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
    

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ana_pencere = Pancar()
    ana_pencere.show()
    ana_pencere.update_gearbox_list()
    ana_pencere.update_environment_list()
    ana_pencere.update_vehicle_list()
    sys.exit(app.exec())