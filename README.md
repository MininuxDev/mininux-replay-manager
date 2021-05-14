# Mininux Replay manager

Simple replay manager for the game Project+, compatible with Linux and macOS

## Installation
Just grab the AppImage/mac App with Python and the dependencies bundled from the [releases](https://github.com/MininuxDev/mininux-replay-manager/releases/)

On linux, you can also install with pip (>= python3.6 and qt5 required):

install qt5 :
```
sudo apt install qt5-default  # Debian
sudo pacman -S qt5-base  # Arch
```
install mininux-replay-manager :
```
pip3 install --user mininux-replay-manager  # install for your user
sudo pip3 install mininux-replay-manager  # instal for your whole system (not recommended)
```
You can now run `python3 -m mininux-replay-manager`

Running the module directly from the repo seems to work, but you need to have PySide2 installed 
