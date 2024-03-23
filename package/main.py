# Bismillahirrahmanirrahim
from PyQt6 import QtCore, QtGui, QtWidgets
from ui import mainWindow
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    VehicleDynamicsApp = QtWidgets.QMainWindow()
    ui = mainWindow.Ui_VehicleDynamicsApp()
    ui.setupUi(VehicleDynamicsApp)
    VehicleDynamicsApp.show()

#     ui.enginev_vehiclev.setStyleSheet(
#         """
#     QPushButton{
#         border-radius:2px;
#         color:rgb(230,230,230);
#         font: 9pt "Gill Sans MT";
#         background-color: rgb(20,20,20);
#         cursor:pointer;
#         border: 1px solid rgb(168, 168, 168);
#     }
# """
#     )
    sys.exit(app.exec())