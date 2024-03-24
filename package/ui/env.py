# Form implementation generated from reading ui file 'env.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from . import widgets_rc
class Ui_Cevre(object):
    def setupUi(self, Cevre):
        Cevre.setObjectName("Cevre")
        Cevre.resize(299, 215)
        Cevre.setMinimumSize(QtCore.QSize(299, 215))
        Cevre.setMaximumSize(QtCore.QSize(299, 215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/road.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Cevre.setWindowIcon(icon)
        Cevre.setStyleSheet("font: 700 11px \"Segoe UI\";\n"
"color:rgb(25,25,25);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Cevre)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=Cevre)
        self.label_6.setStyleSheet("font: 700 14pt \"Segoe UI\";")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(parent=Cevre)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(120, 0))
        self.label_8.setStyleSheet("height:13px;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label = QtWidgets.QLabel(parent=Cevre)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(120, 0))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=Cevre)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=Cevre)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=Cevre)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cevre_isim = QtWidgets.QLineEdit(parent=Cevre)
        self.cevre_isim.setObjectName("cevre_isim")
        self.verticalLayout.addWidget(self.cevre_isim)
        self.ruzgar_hizi = QtWidgets.QLineEdit(parent=Cevre)
        self.ruzgar_hizi.setObjectName("ruzgar_hizi")
        self.verticalLayout.addWidget(self.ruzgar_hizi)
        self.yol_egimi = QtWidgets.QLineEdit(parent=Cevre)
        self.yol_egimi.setObjectName("yol_egimi")
        self.verticalLayout.addWidget(self.yol_egimi)
        self.hava_yogunlugu = QtWidgets.QLineEdit(parent=Cevre)
        self.hava_yogunlugu.setObjectName("hava_yogunlugu")
        self.verticalLayout.addWidget(self.hava_yogunlugu)
        self.yercekimi = QtWidgets.QLineEdit(parent=Cevre)
        self.yercekimi.setStyleSheet("height:13px;")
        self.yercekimi.setObjectName("yercekimi")
        self.verticalLayout.addWidget(self.yercekimi)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(parent=Cevre)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ortam_kaydet = QtWidgets.QPushButton(parent=self.frame)
        self.ortam_kaydet.setMinimumSize(QtCore.QSize(141, 21))
        self.ortam_kaydet.setMaximumSize(QtCore.QSize(141, 21))
        self.ortam_kaydet.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ortam_kaydet.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.ortam_kaydet.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"font: 700 11px \"Segoe UI\";\n"
"color:rgb(210,210,210);\n"
"background-color: rgb(25,25,25);\n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(9, 9, 9);\n"
"background-color:rgb(239, 239, 239);\n"
"}\n"
"QPushButton:pressed {\n"
"color:rgb(9, 9, 9);\n"
"}")
        self.ortam_kaydet.setObjectName("ortam_kaydet")
        self.horizontalLayout_4.addWidget(self.ortam_kaydet)
        self.verticalLayout_8.addWidget(self.frame)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.retranslateUi(Cevre)
        QtCore.QMetaObject.connectSlotsByName(Cevre)

    def retranslateUi(self, Cevre):
        _translate = QtCore.QCoreApplication.translate
        Cevre.setWindowTitle(_translate("Cevre", "Çevre"))
        self.label_6.setText(_translate("Cevre", "Çevresel Faktörler"))
        self.label_8.setText(_translate("Cevre", "Ortam ismi"))
        self.label.setText(_translate("Cevre", "Rüzgar hızı  (km/s)"))
        self.label_2.setText(_translate("Cevre", "Yol eğimi  (açı)"))
        self.label_3.setText(_translate("Cevre", "Hava yoğunluğu (kg/m^3)"))
        self.label_4.setText(_translate("Cevre", "Yer çekimi ivmesi (m/s^2)"))
        self.ortam_kaydet.setText(_translate("Cevre", "KAYDET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cevre = QtWidgets.QDialog()
    ui = Ui_Cevre()
    ui.setupUi(Cevre)
    Cevre.show()
    sys.exit(app.exec())
