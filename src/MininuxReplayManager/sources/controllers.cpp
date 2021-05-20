#include "controllers.h"
#include <QFile>
#include <QDir>
#include <QDebug>

bool moveReplay(const QString &replayDataPath, const QString &userDataPath, const QString &replayName) {
    QString replayPath = replayDataPath + "/" + replayName;
    QString destPath = userDataPath + "/collect.vff";
    qInfo() << "copying \"" << replayPath << "\" to \"" << destPath;
    QFile::remove(destPath);
    return QFile::copy(replayPath, destPath);
}

bool renameReplay(const QString &replayDataPath, const QString &oldReplayName, const QString &newReplayName) {
    return QFile::rename(replayDataPath + "/" + oldReplayName, replayDataPath + "/" + newReplayName);
}

bool deleteReplay(const QString &replayDataPath, const QString &replayName) {
    return QFile::remove(replayDataPath + "/" + replayName);
}
