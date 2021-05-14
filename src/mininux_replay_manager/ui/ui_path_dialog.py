# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'path_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PathDialog(object):
    def setupUi(self, PathDialog):
        if not PathDialog.objectName():
            PathDialog.setObjectName(u"PathDialog")
        PathDialog.resize(531, 457)
        self.gridLayout = QGridLayout(PathDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(PathDialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.replayDataFolder_Line = QLineEdit(PathDialog)
        self.replayDataFolder_Line.setObjectName(u"replayDataFolder_Line")

        self.gridLayout.addWidget(self.replayDataFolder_Line, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.userFolder_Label = QLabel(PathDialog)
        self.userFolder_Label.setObjectName(u"userFolder_Label")

        self.horizontalLayout_2.addWidget(self.userFolder_Label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.replayDataFolder_Select = QToolButton(PathDialog)
        self.replayDataFolder_Select.setObjectName(u"replayDataFolder_Select")

        self.gridLayout.addWidget(self.replayDataFolder_Select, 3, 3, 1, 1)

        self.userFolder_Select = QToolButton(PathDialog)
        self.userFolder_Select.setObjectName(u"userFolder_Select")

        self.gridLayout.addWidget(self.userFolder_Select, 6, 3, 1, 1)

        self.buttonBox = QDialogButtonBox(PathDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.replayData_Label = QLabel(PathDialog)
        self.replayData_Label.setObjectName(u"replayData_Label")

        self.horizontalLayout.addWidget(self.replayData_Label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.userFolder_Line = QLineEdit(PathDialog)
        self.userFolder_Line.setObjectName(u"userFolder_Line")

        self.gridLayout.addWidget(self.userFolder_Line, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.retranslateUi(PathDialog)
        self.buttonBox.rejected.connect(PathDialog.reject)
        self.buttonBox.accepted.connect(PathDialog.accept)

        QMetaObject.connectSlotsByName(PathDialog)
    # setupUi

    def retranslateUi(self, PathDialog):
        PathDialog.setWindowTitle(QCoreApplication.translate("PathDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("PathDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Before using this replay manager, you have to configure your paths:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Replay Data folder is usually located next to your dolphin AppImage or App. The replays are stored there.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">On Linux, the User Folder is usually in <span style=\" font-family:'Noto Sans Mono','monospace'; color:#000000;\">~/.local/sh"
                        "are/FasterPPlus</span>.<br />If you are on macOS, just select your dolphin App and i'll find the user folder inside.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">That's where P+ loads its replays.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Be sure to have launched at least a game to generate those directories</p></body></html>", None))
        self.userFolder_Label.setText(QCoreApplication.translate("PathDialog", u"User folder", None))
        self.replayDataFolder_Select.setText(QCoreApplication.translate("PathDialog", u"...", None))
        self.userFolder_Select.setText(QCoreApplication.translate("PathDialog", u"...", None))
        self.replayData_Label.setText(QCoreApplication.translate("PathDialog", u"ReplayData folder", None))
    # retranslateUi

