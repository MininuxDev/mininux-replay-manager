import sys

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication
from mininux_replay_manager.main_window import MainWindow

def main():
    app = QApplication([])
    QCoreApplication.setOrganizationName("MininuxDev")
    QCoreApplication.setApplicationName("P+ Replay Manager")
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()