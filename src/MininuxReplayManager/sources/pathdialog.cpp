#include "pathdialog.h"
#include "ui_pathdialog.h"
#include <QFileDialog>
#include <QDebug>

PathDialog::PathDialog(MainWindow *parent): QDialog(parent),
    ui(new Ui::PathDialog)
{
    ui->setupUi(this);

    #ifdef Q_OS_MACOS
        ui->userFolder_Label->setText(tr("Dolphin.app"));
    #endif
    // use settings value, otherwise use default value

    if (parent->isDolphinFolderValid()!=MainWindow::PathNotSet){
        ui->dolphinFolder_Line->setText(parent->getDolphinFolderPath());
    } else {
        setDolphinFolderLineItalic(true);
        //QDir defaultDolphinFolderDir = QDir(".");
        //defaultDolphinFolderDir.makeAbsolute();
        ui->dolphinFolder_Line->setText(QDir(".").path());
    }

    if (parent->isUserDataPathValid()!=MainWindow::PathNotSet) {
        ui->userFolder_Line->setText(parent->getUserFolderPath());
    } else {
        setUserFolderLineItalic(true);
        #if defined(Q_OS_MACOS)
            //QDir defaultUserFolderDir = QDir("./Dolphin.app");
            //defaultUserFolderDir.makeAbsolute();
            ui->userFolder_Line->setText(QDir("./Dolphin.app").path());
        #elif defined(Q_OS_LINUX)
            ui->userFolder_Line->setText(QDir::home().path() + "/.local/share/FasterPPlus/");
        #else
            ui->userFolder_Line->setText("");
        #endif
    }
}

PathDialog::~PathDialog()
{
    delete ui;
}

std::tuple<QString, QString> PathDialog::getPaths()
{
   return {ui->dolphinFolder_Line->text(), ui->userFolder_Line->text()};
}

void PathDialog::setUserFolderPath()
{
    #if defined(Q_OS_MACOS) // On mac, we have to use getOpenFileName coz macos considers .app folders as files...
        QString path = QFileDialog::getOpenFileName(this, tr("Select Dolphin App"), ui->userFolder_Line->text());
    #else
         QString path = QFileDialog::getExistingDirectory(this, tr("Select Dolphin Folder"), ui->userFolder_Line->text());
    #endif

    if (!path.isNull()) {
        setUserFolderLineItalic(false);
        ui->userFolder_Line->setText(path);
    }
}

void PathDialog::setDolphinFolderPath()
{
    QString path = QFileDialog::getExistingDirectory(this, tr("Select Dolphin App Path"), ui->dolphinFolder_Line->text(), QFileDialog::ShowDirsOnly);

    if (!path.isNull()) {
        setDolphinFolderLineItalic(false);
        ui->dolphinFolder_Line->setText(path);
    }
}

void PathDialog::setUserFolderLineItalic(const bool &value) {
    QFont font;
    font.setItalic(value);
    ui->userFolder_Line->setFont(font);
}

void PathDialog::setDolphinFolderLineItalic(const bool &value) {
    QFont font;
    font.setItalic(value);
    ui->dolphinFolder_Line->setFont(font);
}

