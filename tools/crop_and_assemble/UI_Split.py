# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Split.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(800, 900))
        Dialog.setMaximumSize(QtCore.QSize(800, 16777215))
        Dialog.setBaseSize(QtCore.QSize(400, 550))
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 791, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.chooseTexture = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.chooseTexture.setObjectName("chooseTexture")
        self.horizontalLayout_2.addWidget(self.chooseTexture)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 80, 791, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.chooseJSON = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.chooseJSON.setEnabled(False)
        self.chooseJSON.setCheckable(False)
        self.chooseJSON.setObjectName("chooseJSON")
        self.horizontalLayout_3.addWidget(self.chooseJSON)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 140, 791, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.JP = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.JP.setChecked(True)
        self.JP.setObjectName("JP")
        self.horizontalLayout.addWidget(self.JP)
        self.zh_TW = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.zh_TW.setObjectName("zh_TW")
        self.horizontalLayout.addWidget(self.zh_TW)
        self.EN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.EN.setObjectName("EN")
        self.horizontalLayout.addWidget(self.EN)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.Run = QtWidgets.QPushButton(Dialog)
        self.Run.setEnabled(False)
        self.Run.setGeometry(QtCore.QRect(0, 180, 791, 50))
        self.Run.setObjectName("Run")
        self.label_Image = QtWidgets.QLabel(Dialog)
        self.label_Image.setGeometry(QtCore.QRect(10, 220, 781, 671))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Image.sizePolicy().hasHeightForWidth())
        self.label_Image.setSizePolicy(sizePolicy)
        self.label_Image.setText("")
        self.label_Image.setScaledContents(True)
        self.label_Image.setObjectName("label_Image")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Texture Split"))
        self.label_2.setText(_translate("Dialog", "Texture Source"))
        self.chooseTexture.setText(_translate("Dialog", "Select"))
        self.label_3.setText(_translate("Dialog", "Source JSON"))
        self.chooseJSON.setText(_translate("Dialog", "Select"))
        self.label.setText(_translate("Dialog", "Output Folder:"))
        self.JP.setText(_translate("Dialog", "JP"))
        self.zh_TW.setText(_translate("Dialog", "zh_TW"))
        self.EN.setText(_translate("Dialog", "EN"))
        self.Run.setText(_translate("Dialog", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
