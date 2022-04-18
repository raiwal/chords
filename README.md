# Description
Detect guitar chord using camera. Draw detected chordmap on the screen and draw notes on the stave.

# Background
Basic guitar chords are quite easy to learn, but to get beginning guitar player familiar with the stave is not so easy. This program map recognized chords to chord map and shows also how they look in the stave


# Requirements
## Hardware
Jetson Nano and Jetson Nano compatible camera.

Setup your Jetson Nano following Nvidias instructions from: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro

## Software
This program uses libraries from Jetson inference project. 
Build Jetson inference project following instructions from: https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md


## Install

```
$ git clone git@github.com:raiwal/chords.git
```

## Run program
```
$ cd chords
$ python3 src/main.py --model=model/resnet18.onnx  --input_blob=input_0 --output_blob=output_0 --labels=labels.txt  /dev/video0
```
Note: if you are using CSI camera use CSI://0 instead of /dev/video0

# Supported chords 

Open position:
* A-minor 
* C-major
* D-minor
* E-minor
* G-major
* F-major

# Miscelanneus
I ended up using Resnet-18 network. Training was done using Washburn D10, Fender Stratocaster, and Gibson Flying V.

Pictures that I used for training are https://drive.google.com/drive/folders/1pQMNR8BMq57_aXnF-raINfqNA64tZvgN?usp=sharing

# Maintainer
Rainer Waltzer @raiwal

# Contributing
Rainer Waltzer @raiwal

# Licence 
Free for non-commercial usage



