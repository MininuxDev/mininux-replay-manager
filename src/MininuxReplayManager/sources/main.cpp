#include "mainwindow.h"
#include <QApplication>
#include <QDir>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    //Set working directory because apple...
    QDir bin(QCoreApplication::applicationDirPath());

    #if defined(Q_OS_MACOS)
        bin.cdUp(); bin.cdUp(); bin.cdUp();
    #endif

     QDir::setCurrent(bin.absolutePath());
    MainWindow w;
    w.show();
    return app.exec();
}
