#!/usr/bin/env bash
mkdir -p build/appimage
cd build/appimage || exit

echo "Building AppDir..."

wget -c "https://github.com/niess/python-appimage/releases/download/python3.9/python3.9.4-cp39-cp39-manylinux1_x86_64.AppImage"
chmod +x python*-manylinux1_x86_64.AppImage
rm -rf squashfs-root/
./python*-manylinux1_x86_64.AppImage --appimage-extract
squashfs-root/AppRun -m pip install --ignore-installed --prefix squashfs-root/opt/python3.9 mininux-replay-manager pyside2  # install mininux-replay-manager in appdir
cp ../../appimage/Apprun squashfs-root/AppRun # replace AppRun so that it launches mininux-replay-manager
rm squashfs-root/usr/share/metainfo/*
rm squashfs-root/usr/share/applications/*
rm squashfs-root/*.desktop
cp ../../appimage/com.Mininux.ReplayManager.desktop squashfs-root/usr/share/applications/
ln -s usr/share/applications/com.Mininux.ReplayManager.desktop squashfs-root/com.Mininux.ReplayManager.desktop
cp ../../appimage/com.Mininux.ReplayManager.appdata.xml squashfs-root/usr/share/metainfo/
echo "Shrinking AppDir..."
# Shrink appimage
rm -rf squashfs-root/usr/lib/libsqlite3.so.0
rm -rf squashfs-root/usr/share/tcltk
rm -rf squashfs-root/opt/python3.*/include
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/pip
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/pip-21.1.1.dist-info
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/Qt/libexec
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/lib-dynload/{_ssl.cpython-*,_hashlib.cpython-*}
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/{Qt3D*,QtLocation*,QtMultimedia*,QtSensors*,QtSerialPort*,QtTextToSpeech*,QtDataVisualization*,QtSql*,QtSvg*,QtWeb*,QtPrintSupport*,QtQml*,QtQuick*,QtNetwork*,QtOpenGL*,QtCharts*,QtConcurrent*,QtXml*,QtTest*,QtScxml*,QtScript,QtRemoteObjects*,QtPositioning*,QtHelp*,QtX11Extras*,QtUiTools*}
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/{glue,designer,uic,pyside2-lupdate,rcc,examples,include,qml}
#rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/Qt/lib/{libQt5EglFsKmsSupport.so.5,libQt5RemoteObjects.so.5,libQt5EglFSDeviceIntegration.so.5,libQt5Bluetooth.so.5,libQt5Charts.so.5,libQt5DataVisualization.so.5,libQt5Designer*,libQt5Gamepad.so.5,libQt5Multimedia.so.5,libQt5Location.so.5,libQt53D*,libQt5Web*,libQt5TextToSpeech.so.5,libQt5Svg.so.5,libQt5Sql.so.5,libQt5SerialPort.so.5,libQt5Sensors.so.5,libQt5Quick*,libQt5Qml*,libQt5DBus.so.5,libQt5Help.so.5,libQt5Multimedia*,libQt5PrintSupport.so.5,libQt5Purchasing.so.5,libQt5SerialBus.so.5,libQt5Xml*,libQt5OpenGL.so.5,libQt5Pdf*,libQt5Concurrent.so.5,libQt5Network*,libQt5Bodymovin.so.5,libQt5XcbQpa.so.5,libQt5X11Extras.so.5,libQt5Test.so.5,libQt5PositioningQuick.so.5,libQt5Positioning.so.5,libQt5Nfc.so.5,libQt5Script*,libQt5Scxml.so.5}
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/Qt/plugins/{gamepads,audio,geometryloaders,geoservices,mediaservice,playlistformats,position,sensorgestures,sensors,sqldrivers,texttospeech,webview,designer,assetimporters,bearer,canbus,egldeviceintegrations,generic,inconengines,imageformats,platforminputcontexts,printsupport,qmltooling,renderers,renderplugins,sceneparsers}
find squashfs-root/opt/python3.*/lib/python3.*/site-packages/Pyside2/Qt/plugins/platforms/ -type f -not -name libqxcb.so -delete
find squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/Qt/translations/ -type f -not -name qt_* -delete
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/Qt/resources
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/Qt/qml
rm -rf squashfs-root/opt/python3.*/lib/python3.*/site-packages/PySide2/Qt/translations/qtwebengine_locales
rm -rf squashfs-root/opt/python3.*/lib/python3.*/ensurepip
rm -rf squashfs-root/opt/python3.*/lib/python3.*/idlelib
rm -rf squashfs-root/opt/python3.*/lib/python3.*/sites-packages/setuptools
rm -rf squashfs-root/opt/python3.*/lib/python3.*/sites-packages/shiboken2/docs

echo "Building AppImage..."
export VERSION=$(cat squashfs-root/opt/python3.9/lib/python3.9/site-packages/mininux_replay_manager-*.dist-info/METADATA | grep "^Version:.*" | cut -d " " -f 2)
wget -c https://github.com/$(wget -q https://github.com/probonopd/go-appimage/releases -O - | grep "appimagetool-.*-x86_64.AppImage" | head -n 1 | cut -d '"' -f 2)
chmod +x appimagetool-*.AppImage
./appimagetool-*-x86_64.AppImage -o squashfs-root/
mv Mininux_Replay_Manager*.AppImage ../../dist/
echo "Your AppImage is in dist/"