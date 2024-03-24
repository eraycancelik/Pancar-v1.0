# Form implementation generated from reading ui file 'gearbox.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from . import widgets_rc

class Ui_Sanziman(object):
    def setupUi(self, Sanziman):
        Sanziman.setObjectName("Sanziman")
        Sanziman.resize(328, 192)
        Sanziman.setMinimumSize(QtCore.QSize(328, 192))
        Sanziman.setMaximumSize(QtCore.QSize(328, 192))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/gearbox2.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Sanziman.setWindowIcon(icon)
        Sanziman.setStyleSheet("font: 700 11px \"Segoe UI\";\n"
"color:rgb(25,25,25);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Sanziman)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_16 = QtWidgets.QLabel(parent=Sanziman)
        self.label_16.setStyleSheet("font: 700 12pt \"Segoe UI\";")
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(parent=Sanziman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(120, 0))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=Sanziman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(161, 0))
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_14 = QtWidgets.QLabel(parent=Sanziman)
        self.label_14.setMinimumSize(QtCore.QSize(120, 0))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(parent=Sanziman)
        self.label_15.setMinimumSize(QtCore.QSize(120, 0))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sanziman_ismi = QtWidgets.QLineEdit(parent=Sanziman)
        self.sanziman_ismi.setObjectName("sanziman_ismi")
        self.verticalLayout.addWidget(self.sanziman_ismi)
        self.vites_oranlari = QtWidgets.QLineEdit(parent=Sanziman)
        self.vites_oranlari.setObjectName("vites_oranlari")
        self.verticalLayout.addWidget(self.vites_oranlari)
        self.dif_oran = QtWidgets.QLineEdit(parent=Sanziman)
        self.dif_oran.setObjectName("dif_oran")
        self.verticalLayout.addWidget(self.dif_oran)
        self.ao_verimi = QtWidgets.QLineEdit(parent=Sanziman)
        self.ao_verimi.setObjectName("ao_verimi")
        self.verticalLayout.addWidget(self.ao_verimi)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.frame_2 = QtWidgets.QFrame(parent=Sanziman)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sanziman_kaydet = QtWidgets.QPushButton(parent=self.frame_2)
        self.sanziman_kaydet.setMinimumSize(QtCore.QSize(141, 21))
        self.sanziman_kaydet.setMaximumSize(QtCore.QSize(141, 21))
        self.sanziman_kaydet.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sanziman_kaydet.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.sanziman_kaydet.setStyleSheet("QPushButton{\n"
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
        self.sanziman_kaydet.setObjectName("sanziman_kaydet")
        self.horizontalLayout_4.addWidget(self.sanziman_kaydet)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Sanziman)
        QtCore.QMetaObject.connectSlotsByName(Sanziman)

    def retranslateUi(self, Sanziman):
        _translate = QtCore.QCoreApplication.translate
        Sanziman.setWindowTitle(_translate("Sanziman", "Şanzıman"))
        self.label_16.setText(_translate("Sanziman", "Şanzıman Parametreleri"))
        self.label_10.setText(_translate("Sanziman", "Şanzıman ismi"))
        self.label_11.setText(_translate("Sanziman", "Vites oranları (3.45,2,3 şeklinde)"))
        self.label_14.setText(_translate("Sanziman", "Diferansiyel dişli oranı"))
        self.label_15.setText(_translate("Sanziman", "Aktarma organları verimi"))
        self.sanziman_kaydet.setText(_translate("Sanziman", "KAYDET"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Sanziman = QtWidgets.QDialog()
#     ui = Ui_Sanziman()
#     ui.setupUi(Sanziman)
#     Sanziman.show()
#     sys.exit(app.exec())
