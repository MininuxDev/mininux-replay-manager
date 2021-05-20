#!/bin/sh

mkdir -p build
cd build || exit
qmake CONFIG+=release PREFIX=/usr TARGET=mininux-replay-manager ../MininuxReplayManager.pro
make
make INSTALL_ROOT=appdir install ; find appdir/
wget -c -nv "https://github.com/probonopd/linuxdeployqt/releases/download/continuous/linuxdeployqt-continuous-x86_64.AppImage"
chmod a+x linuxdeployqt-continuous-x86_64.AppImage
./linuxdeployqt-continuous-x86_64.AppImage --appimage-extract # for systems without fuse (chroots...)
./squashfs-root/AppRun appdir/usr/share/applications/mininux-replay-manager.desktop -appimage

echo "AppImage should be located in build/"
