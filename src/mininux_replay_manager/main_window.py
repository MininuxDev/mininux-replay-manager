import os, sys

from PySide2.QtCore import QSettings
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QMainWindow, QFileSystemModel, QMessageBox, QInputDialog

from mininux_replay_manager.ui.ui_main_window import Ui_MainWindow
from mininux_replay_manager.path_dialog import PathDialog
from mininux_replay_manager import controllers


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setPaths_Button.clicked.connect(self.set_paths)
        self.useReplay_Button.clicked.connect(self.use_replay)
        self.deleteReplay_Button.clicked.connect(self.delete_replay)
        self.renameReplay_Button.clicked.connect(self.rename_replay)

        self.settings = QSettings()

        self.replay_data_model = QFileSystemModel()
        self.replay_data_model.setRootPath(self.replay_data_path)
        self.user_data_model = QFileSystemModel()
        self.user_data_model.setRootPath(self.user_data_path)

        if self.replay_data_path:
            self.replayFolder_ListView.setModel(self.replay_data_model)
            self.replayFolder_ListView.setRootIndex(self.replay_data_model.index(self.replay_data_path))
        if self.user_data_path:
            self.userData_ListView.setModel(self.user_data_model)
            self.userData_ListView.setRootIndex(self.user_data_model.index(self.user_data_path))

    def set_paths(self):
        path_dialog = PathDialog(self)
        path_dialog.setModal(True)
        if path_dialog.exec_() == path_dialog.Accepted:
            replay_data_path, user_folder_path = path_dialog.get_paths()
            self.settings.setValue("paths/replay_data", replay_data_path)

            if sys.platform == "darwin" and os.path.splitext(user_folder_path)[1] == ".app":
                print("User selected a mac app, searching for true user folder...")
                if os.path.exists(os.path.join(user_folder_path, "Contents", "Resources", "User")):
                    print("Folder found")
                    user_folder_path = os.path.join(user_folder_path, "Contents", "Resources", "User")
            self.settings.setValue("paths/user_folder", user_folder_path)
            self.replay_data_model.setRootPath(self.replay_data_path)
            self.replayFolder_ListView.setRootIndex(self.replay_data_model.index(self.replay_data_path))
            self.user_data_model.setRootPath(self.user_data_path)
            self.userData_ListView.setRootIndex(self.user_data_model.index(self.user_data_path))

    @property
    def replay_data_path(self):
        return self.settings.value("paths/replay_data")

    @property
    def user_folder_path(self):
        return self.settings.value("paths/user_folder")

    @property
    def user_data_path(self):
        return os.path.join(self.settings.value("paths/user_folder"), "Wii", "title", "00010000", "52534245", "data") \
            if self.settings.value("paths/user_folder") else None

    def get_selected_replay_name(self):
        return self.replayFolder_ListView.selectionModel().currentIndex().data(Qt.DisplayRole)


    def use_replay(self):
        if not (self.replay_data_path and self.user_data_path):
            self.set_paths()
        else:
            replay_name = self.get_selected_replay_name()
            if replay_name:
                controllers.move_replay(self.replay_data_path,
                                        self.user_data_path, replay_name)
                QMessageBox.information(self, self.tr("Replay selection"), self.tr("Replay selection done "
                                                                                   "successfuly. You can now open P+."))
            else:
                self.warn_no_replay_selected()

    def rename_replay(self):
        if not self.replay_data_path:
            self.set_paths()
        else:
            replay_name = self.get_selected_replay_name()
            if replay_name:
                new_name, _ = QInputDialog.getText(self, self.tr("Rename replay"), self.tr("New name :"), text=replay_name)
                if _:
                    controllers.rename_replay(self.replay_data_path, replay_name, new_name)
            else:
                self.warn_no_replay_selected()

    def delete_replay(self):
        if not self.replay_data_path:
            self.set_paths()
        else:
            replay_name = self.get_selected_replay_name()
            if replay_name:
                response = QMessageBox.question(self, self.tr("Delete replay"),
                                                self.tr("Are you sure you want to remove the replay ") +
                                                f"\"{self.get_selected_replay_name()}\"?", QMessageBox.Yes, QMessageBox.Cancel)
                if response == QMessageBox.Yes:
                    controllers.delete_replay(self.settings.value("paths/replay_data"), replay_name)
            else:
                self.warn_no_replay_selected()

    def warn_no_replay_selected(self):
        QMessageBox.warning(self, self.tr("Replay selection"), self.tr("You must first select a replay !"))