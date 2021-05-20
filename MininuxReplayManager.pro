greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
QT -= gui

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    $$files(src/MininuxReplayManager/sources/*.cpp)

HEADERS += \
    $$files(src/MininuxReplayManager/include/*.h)

FORMS += \
    $$files(src/MininuxReplayManager/forms/*.ui)

RESOURCES += \
    $$files(src/MininuxReplayManager/res&ources/*.qrc) \
    src/MininuxReplayManager/resources/resources.qrc

INCLUDEPATH += src/MininuxReplayManager/include/

# Default rules for deployment.

linux-g++ {
    isEmpty(PREFIX) {
        PREFIX = /usr/local
    }

    target.path = $$PREFIX/bin

    desktop.files = misc/mininux-replay-manager.desktop
    desktop.path = $$PREFIX/share/applications/
    icon256.files = misc/mininux-replay-manager.svg
    icon256.path = $$PREFIX/share/icons/hicolor/256x256/apps/

    INSTALLS += desktop
    INSTALLS += icon256
}

!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    build_appimage.sh \
    misc/mininux-replay-manager.desktop

