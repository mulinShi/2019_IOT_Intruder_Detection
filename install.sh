#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install git
sudo apt-get install python3-pip -y
sudo pip3 install numpy==1.16
sudo pip3 install keras
sudo pip3 install tensorflow 
sudo pip3 install matplotlib

# sudo pip3 install opencv-python==3.2.0.8
sudo mkdir opencv
cd opencv
sudo git clone https://github.com/openc
v/opencv.git
cd opencv
sudo mkdir build
cd build

sudo apt-get install build-essential -y
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev -y
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev -y
sudo cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local PYTHON3_EXECUTABLE = /usr/bin/python3 PYTHON_INCLUDE_DIR = /usr/include/python3.5 PYTHON_INCLUDE_DIR2 = /usr/include/i386-linux-gnu/python3.5m PYTHON_LIBRARY = /usr/bin/i386-linux-gnu-python3/libpython3.5m.so PYTHON3_NUMPY_INCLUDE_DIRS = /usr/local/lib/python3.5/dist-packages/numpy/core/include/ ..
sudo make
sudo make install