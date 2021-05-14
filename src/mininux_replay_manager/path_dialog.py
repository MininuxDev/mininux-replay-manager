import sys

from PySide2.QtCore import QSettings
from PySide2.QtGui import QFont
from mininux_replay_manager.ui.ui_path_dialog import Ui_PathDialog
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox


class PathDialog(QDialog, Ui_PathDialog):
    def __init__(self, parent):
        super(PathDialog, self).__init__(parent)
        self.setupUi(self)

        settings = QSettings()
        self.replayDataFolder_Line.setText(settings.value("paths/replay_data"))
        a = settings.value("paths/user_folder")
        if settings.value("paths/user_folder"):
            self.userFolder_Line.setText(settings.value("paths/user_folder"))
        elif sys.platform == "linux":
            font = QFont()
            font.setItalic(True)
            self.userFolder_Line.setFont(font)
            self.userFolder_Line.setText("~/.local/share/FasterPPlus")

        self.replayDataFolder_Select.clicked.connect(self.set_replay_data_path)
        self.userFolder_Select.clicked.connect(self.set_user_path)

    def get_paths(self):
        return self.replayDataFolder_Line.text(), self.userFolder_Line.text()

    def set_user_path(self):
        if sys.platform == "darwin":
            path = QFileDialog.getOpenFileName(self, self.tr("Select Dolphin App"), self.userFolder_Line.text())[0]
        else:
            path = QFileDialog.getExistingDirectory(self, self.tr("Select User directory"), self.userFolder_Line.text())
        if path:
            font = QFont()
            font.setItalic(False)
            self.userFolder_Line.setFont(font)
            self.userFolder_Line.setText(path)

    def set_replay_data_path(self):
        path = QFileDialog.getExistingDirectory(self, self.tr("Select Replay Data directory"), self.replayDataFolder_Line.text())
        if path:
            self.replayDataFolder_Line.setText(path)