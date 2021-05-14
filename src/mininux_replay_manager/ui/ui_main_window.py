# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(971, 702)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.setPaths_Button = QPushButton(self.centralwidget)
        self.setPaths_Button.setObjectName(u"setPaths_Button")

        self.verticalLayout.addWidget(self.setPaths_Button)

        self.useReplay_Button = QPushButton(self.centralwidget)
        self.useReplay_Button.setObjectName(u"useReplay_Button")

        self.verticalLayout.addWidget(self.useReplay_Button)

        self.renameReplay_Button = QPushButton(self.centralwidget)
        self.renameReplay_Button.setObjectName(u"renameReplay_Button")

        self.verticalLayout.addWidget(self.renameReplay_Button)

        self.deleteReplay_Button = QPushButton(self.centralwidget)
        self.deleteReplay_Button.setObjectName(u"deleteReplay_Button")

        self.verticalLayout.addWidget(self.deleteReplay_Button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.replayFolder_ListView = QListView(self.centralwidget)
        self.replayFolder_ListView.setObjectName(u"replayFolder_ListView")

        self.gridLayout.addWidget(self.replayFolder_ListView, 1, 0, 1, 1)

        self.userFolderList_Header = QLabel(self.centralwidget)
        self.userFolderList_Header.setObjectName(u"userFolderList_Header")

        self.gridLayout.addWidget(self.userFolderList_Header, 0, 1, 1, 1)

        self.instructions_Label = QLabel(self.centralwidget)
        self.instructions_Label.setObjectName(u"instructions_Label")

        self.gridLayout.addWidget(self.instructions_Label, 2, 0, 1, 2)

        self.userData_ListView = QListView(self.centralwidget)
        self.userData_ListView.setObjectName(u"userData_ListView")
        self.userData_ListView.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout.addWidget(self.userData_ListView, 1, 1, 1, 1)

        self.replayLis_Header = QLabel(self.centralwidget)
        self.replayLis_Header.setObjectName(u"replayLis_Header")

        self.gridLayout.addWidget(self.replayLis_Header, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mininux Replay Manager", None))
        self.setPaths_Button.setText(QCoreApplication.translate("MainWindow", u"Set Paths", None))
        self.useReplay_Button.setText(QCoreApplication.translate("MainWindow", u"Use selected Replay", None))
        self.renameReplay_Button.setText(QCoreApplication.translate("MainWindow", u"Rename selected Replay", None))
        self.deleteReplay_Button.setText(QCoreApplication.translate("MainWindow", u"Delete selected Replay", None))
        self.userFolderList_Header.setText(QCoreApplication.translate("MainWindow", u"User data folder:", None))
        self.instructions_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Instructions:</p><p>Click on &quot;Set Paths&quot; and set the paths according to your P+ installation.</p><p>Chose the replay you want to use, and hit &quot;Use selected Replay&quot;. You can now open P+ and find your replay in Vault &gt; replays</p><p>You can also delete replays, or rename them.</p></body></html>", None))
        self.replayLis_Header.setText(QCoreApplication.translate("MainWindow", u"Replay folder:", None))
    # retranslateUi

