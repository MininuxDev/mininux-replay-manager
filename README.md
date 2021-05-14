# Mininux Replay manager

Simple replay manager for the game Project+, compatible with Linux and macOS

## Installation
### direct binary download
Just grab the Linux binary/Mac App (the the dependencies are bundled inside) from the [releases](https://github.com/MininuxDev/mininux-replay-manager/releases/)

### Install package
On linux (it may work on mac but i couldn't test it), you can also install with pip (>= python3.6 and qt5 required):

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
You can now run `python3 -m mininux_replay_manager`
