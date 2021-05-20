#ifndef PATHDIALOG_H
#define PATHDIALOG_H

#include <QDialog>
#include <QSettings>
#include "mainwindow.h"

QT_BEGIN_NAMESPACE
namespace Ui { class PathDialog; }
QT_END_NAMESPACE

class PathDialog : public QDialog
{
    Q_OBJECT

    public:
        PathDialog(MainWindow *parent = nullptr);
        ~PathDialog();

        std::tuple<QString, QString> getPaths();

    public slots:
        void setUserFolderPath();
        void setDolphinFolderPath();

    private:
        Ui::PathDialog *ui;

        void setUserFolderLineItalic(const bool &value);
        void setDolphinFolderLineItalic(const bool &value);
};

#endif // PATHDIALOG_H
