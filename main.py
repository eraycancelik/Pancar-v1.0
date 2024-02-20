from PyQt6 import QtCore, QtGui, QtWidgets
from package.ui import mainWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    VehicleDynamicsApp = QtWidgets.QMainWindow()
    ui = mainWindow.Ui_VehicleDynamicsApp()
    ui.setupUi(VehicleDynamicsApp)
    VehicleDynamicsApp.show()
    sys.exit(app.exec())