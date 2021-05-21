#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <QMessageBox>
#include <QInputDialog>
#include "controllers.h"
#include "pathdialog.h"

MainWindow::MainWindow(QWidget *parent): QMainWindow(parent),
    ui(new Ui::MainWindow),
    m_settings(new QSettings("MininuxReplayManager.ini", QSettings::IniFormat, this)),
    m_replayDataModel(new QFileSystemModel(this)),
    m_userDataModel(new QFileSystemModel(this))
{
    qInfo() << "Using Qsettings file:" << m_settings->fileName();
    qInfo() << "Paths:";
    qInfo() << "   ReplayData path: " << getReplayDataPath();
    qInfo() << "   UserData path: " << getUserDataPath();

    ui->setupUi(this);
    QMenuBar *bar = new QMenuBar(ui->menuBar);
    QMenu *menuHelp = new QMenu("Help", bar);

    QAction *aboutQtAct = new QAction("About Qt", bar);
    menuHelp->addAction(aboutQtAct);
    bar->addMenu(menuHelp);
    connect(aboutQtAct, &QAction::triggered, this, QApplication::aboutQt);
    ui->menuBar->setCornerWidget(bar);

    updateLastUsedReplayLabel();

    ui->replayData_ListView->setModel(m_replayDataModel);
    ui->userData_ListView->setModel(m_userDataModel);

    auto [replayDataStatus, userDataStatus] = refreshPaths();
    if (replayDataStatus==PathNotSet or userDataStatus==PathNotSet) {
        setPaths();
    }
}

MainWindow::~MainWindow()
{
    delete ui;
    delete m_settings;
    delete m_replayDataModel;
    delete m_userDataModel;
}

std::tuple<MainWindow::PathValidity, MainWindow::PathValidity> MainWindow::refreshPaths() {
    enableAction(false);

    PathValidity replayDataStatus = isReplayDataPathValid();

    switch (replayDataStatus) {
        case PathValid: {
            break;
        }

        case ReplayDataNotFound: {
            if (askCreateReplayDataDir()) {
                replayDataStatus = PathValid;
            } else {
                QString errorMsg = tr("Error: Dolphin Folder \"") + getDolphinFolderPath() + tr("\" does not contain ReplayData folder.");
                qCritical() << errorMsg;
                QMessageBox::critical(this, tr("Path not found"), errorMsg);
            }
            break;
        }
        case PathNotSet: {
            qInfo() << "dolphin_folder path is not set.";
            break;
        }

        case PathDoesNotExist: {
            QString errorMsg = tr("Error: Dolphin Folder \"") + getDolphinFolderPath() + tr("\" does not exist. Set the paths again");
            qCritical() << errorMsg;
            QMessageBox::critical(this, tr("Path not found"), errorMsg);
            break;
        }

        default:
            break;
    }

    m_replayDataModel->setRootPath(getReplayDataPath());
    ui->replayData_ListView->setRootIndex(m_replayDataModel->index(getReplayDataPath()));

    PathValidity userDataStatus = isUserDataPathValid();

    switch (userDataStatus) {
        case PathValid: {

            break;
        }

        case UserDataNotFound: {
            QString errorMsg = tr("Error: User Folder \"") + getUserFolderPath() + tr("\" does not contain P+ data. Have you launched P+ at least once ? Also check that the paths are correct.");
            qCritical() << errorMsg;
            QMessageBox::critical(this, tr("Path not found"), errorMsg);
            break;
        }

        case PathNotSet: {
            qInfo() << "user_foler path is not set.";
            break;
        }

        case PathDoesNotExist: {
            QString errorMsg = tr("Error: User Folder \"") + getUserFolderPath() + tr("\" does not exist. Have you launched P+ at least once ? Also check that the paths are correct.");
            qCritical() << errorMsg;
            QMessageBox::critical(this, tr("Path not found"), errorMsg);
            break;
        }

        default:
            break;
    }

    m_userDataModel->setRootPath(getUserDataPath());
    ui->userData_ListView->setRootIndex(m_userDataModel->index(getUserDataPath()));

    if (replayDataStatus==PathValid and userDataStatus==PathValid) {
        enableAction(true);
    }

    return {replayDataStatus, userDataStatus};
}

// Slots definitions
void MainWindow::setPaths()
{
    PathDialog *path_dialog = new PathDialog(this);
    if (path_dialog->exec() == path_dialog->Accepted){
        auto [dolphinFolderPath, userFolderPath] = path_dialog->getPaths();

        m_settings->setValue("paths/dolphin_folder", dolphinFolderPath);
        m_settings->setValue("paths/user_folder", userFolderPath);
    }
    if (isDolphinFolderValid()==PathNotSet or isUserFolderPathValid()==PathNotSet) {
        QMessageBox::warning(this, tr("Paths not set"), tr("This replay manager won't work unless all the paths are set correctly!"));
    }
    refreshPaths();
}

bool MainWindow::askCreateReplayDataDir() {
    QMessageBox::StandardButton response = QMessageBox::question(this, tr("ReplayData not found"), tr("ReplayData directory at ") + getDolphinFolderPath() + tr(" not found. If you have not saved any replay yet, it's normal and I can create the directory for you. Otherwise you should check the paths again.\nCreate ReplayData directory ?"));
    if (response==QMessageBox::Yes) {
        if (QDir(getDolphinFolderPath()).mkdir("ReplayData")) {
            return true;
        }
        if (!isReplayDataPathValid()) {
            QString errorMsg = tr("Could not create ReplayData directory");
            qCritical() << errorMsg;
            QMessageBox::critical(this, tr("Something went wrong..."), errorMsg);
        }
    }
    return false;
}

void MainWindow::useReplay()
{
    QString replayName = getSelectedReplayName();
    if (!replayName.isEmpty()) {
        if (::moveReplay(getReplayDataPath(), getUserDataPath(), replayName)) {
            m_settings->setValue("last_used_replay", getSelectedReplayName());
            updateLastUsedReplayLabel();
            QMessageBox::information(this, tr("Success"), tr("Replay copied into P+ data successfully ! You can now view it in Vault --> Replays."));
        } else {
            QString errorMsg = tr("Error: Could not copy replay \"") + replayName + "\"";
            QMessageBox::critical(this, tr("Something went wrong..."), errorMsg);
        }
    } else warnNoReplaySelected();
}

void MainWindow::renameReplay()
{
    QString oldName = getSelectedReplayName();
    if (!oldName.isEmpty()) {
        QString newName;
        bool ok = true;
        while (newName.isEmpty() and ok) {
            newName = QInputDialog::getText(this, tr("Rename Replay"), tr("New name: "), QLineEdit::Normal, oldName, &ok);
        }

        if (ok) {
            if (!::renameReplay(getReplayDataPath(), oldName, newName)) {
                QString errorMsg = tr("Error: Could not rename replay \"") + oldName + "\" to \"" + newName + "\"";
                qCritical() << errorMsg;
                QMessageBox::critical(this, tr("Something went wrong..."), errorMsg);
            }
        }
    } else warnNoReplaySelected();
}

void MainWindow::deleteReplay()
{
    QString replayName = getSelectedReplayName();
    if (!replayName.isEmpty()) {
        QMessageBox::StandardButton response = QMessageBox::question(this, tr("Delete replay confirmation"), tr("Are you sure you want to remove the file \"") + getReplayDataPath() + "/" + replayName + "\" ?");
        if (response==QMessageBox::Yes) {
            ::deleteReplay(getReplayDataPath(), replayName);
        }
    } else warnNoReplaySelected();
}

// Shortcut functions
void MainWindow::enableAction(const bool &value) {
    ui->useReplay_Button->setEnabled(value);
    ui->renameReplay_Button->setEnabled(value);
    ui->deleteReplay_Button->setEnabled(value);
    ui->replayData_ListView->setEnabled(value);
    ui->userData_ListView->setEnabled(value);
}

const QString MainWindow::getDolphinFolderPath() {
    return m_settings->value("paths/dolphin_folder").toString();
}

const QString MainWindow::getReplayDataPath() {
    if (!getDolphinFolderPath().isEmpty()) {
        return m_settings->value("paths/dolphin_folder").toString() + "/ReplayData";
    } else return "";
}

const QString MainWindow::getUserFolderPath() {
    return m_settings->value("paths/user_folder").toString();
}

const QString MainWindow::getUserDataPath() {
    if (!getUserFolderPath().isEmpty()) {
        #if defined(Q_OS_MACOS)
            return getUserFolderPath() + "/Contents/Resources/User/Wii/title/00010000/52534245/data/";
        #else
            return getUserFolderPath() + "/Wii/title/00010000/52534245/data/";
        #endif
    } else return "";
}

MainWindow::PathValidity MainWindow::isDolphinFolderValid() {
    if (!getDolphinFolderPath().isEmpty()) {
        if (QDir(getDolphinFolderPath()).exists()) {
            return MainWindow::PathValid;
        } else return PathDoesNotExist;
    } else return PathNotSet;
}

MainWindow::PathValidity MainWindow::isReplayDataPathValid() {
    if (isDolphinFolderValid() == PathValid) {
        if (QDir(getReplayDataPath()).exists()) {
            return PathValid;
        } else return ReplayDataNotFound;
    } else return isDolphinFolderValid();
}

MainWindow::PathValidity MainWindow::isUserFolderPathValid() {
    if (!getUserFolderPath().isEmpty()) {
        if (QDir(getUserFolderPath()).exists()) {
            return PathValid;
        } else return PathDoesNotExist;
    } else return PathNotSet;
}

MainWindow::PathValidity MainWindow::isUserDataPathValid() {
    if (isUserFolderPathValid() == PathValid) {
        if (QDir(getUserDataPath()).exists()) {
            return PathValid;
        } else return UserDataNotFound;
    } else return isUserFolderPathValid();
}


QString MainWindow::getSelectedReplayName() {
    return ui->replayData_ListView->selectionModel()->currentIndex().data(Qt::DisplayRole).toString();
}

void MainWindow::warnNoReplaySelected()
{
    QMessageBox::warning(this, tr("No replay selected"), tr("You have to select a replay first !"));
}

void MainWindow::updateLastUsedReplayLabel() {
    if (!m_settings->value("last_used_replay").toString().isEmpty()) {
        ui->lastUsedReplay_Label->setText(tr("(Last used replay : \"") + m_settings->value("last_used_replay").toString() + "\")");
    } else {
        ui->lastUsedReplay_Label->setText(tr("(Last used replay : None)"));
    }

}
