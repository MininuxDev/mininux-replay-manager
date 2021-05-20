#ifndef CONTROLLERS_H
#define CONTROLLERS_H

#include <QString>


bool moveReplay(const QString &replayDataPath, const QString &userDataPath, const QString &replayName);
bool renameReplay(const QString &replayDataPath, const QString &oldReplayName, const QString &newReplayName);
bool deleteReplay(const QString &replayDataPath, const QString &replayName);

#endif // CONTROLLERS_H
