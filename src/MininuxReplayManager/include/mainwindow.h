#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSettings>
#include <QFileSystemModel>
#include <QDir>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT
    public:
        enum PathValidity { PathValid, PathNotSet, PathDoesNotExist, UserDataNotFound, ReplayDataNotFound };

        MainWindow(QWidget *parent = nullptr);
        ~MainWindow();

        const QString getReplayDataPath();
        const QString getUserFolderPath();
        const QString getUserDataPath();
        const QString getDolphinFolderPath();

        PathValidity isDolphinFolderValid();
        PathValidity isReplayDataPathValid();
        PathValidity isUserFolderPathValid();
        PathValidity isUserDataPathValid();

        bool askCreateReplayDataDir();
        void enableAction(const bool &value);

    public slots:
        void setPaths();
        void useReplay();
        void renameReplay();
        void deleteReplay();

    private:
        Ui::MainWindow *ui;
        QSettings *m_settings;

        QFileSystemModel *m_replayDataModel;
        QFileSystemModel *m_userDataModel;

        std::tuple<PathValidity, PathValidity> refreshPaths();

        QString getSelectedReplayName();
        void warnNoReplaySelected();
        void updateLastUsedReplayLabel();
};
#endif // MAINWINDOW_H
