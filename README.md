# Mininux Replay manager

Simple replay manager for the game Project+, compatible with Linux and macOS

## Installation
### direct binary download
Grab the App (macos) or Appimage (linux) from the [releases](https://github.com/MininuxDev/mininux-replay-manager/releases/)

## Building
Requirements: qt5
```
sudo apt install qt-default  # debian/ubuntu based distros
sudo pacman -S qt5-base  # Arch based distros
```
On other distros and mac, see https://www.qt.io/download

### Building appimage
Use the script `./build_appimage`

### Building standard binary

Generate makefile :
```
mkdir -p build
cd build
qmake CONFIG+=release ../MininuxReplayManager.pro
make
```
