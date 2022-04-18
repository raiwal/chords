# Description
Detect guitar chord using camera. Draw detected chordmap on the screen and draw recognized chord notes on the staff.

# Background
Basic guitar chords are quite easy to learn, but to get beginning guitar player familiar with the staff is not so easy. This program map recognized chords to chord map and display them in the staff.

# Hardware requirements
Jetson Nano and Jetson Nano compatible camera.

Setup your Jetson Nano following Nvidias instructions from: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro

# Software requirements
This program uses imagenet program on top of chord drawing so build Jetson inference project following instructions from: https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md


## Install

```
$ git clone git@github.com:raiwal/chords.git
```

## Run program
Here it is assumed that camera number is 0. 

```
$ cd chords
$ python3 src/main.py --model=model/resnet18.onnx  --input_blob=input_0 --output_blob=output_0 --labels=labels.txt  /dev/video0
```
Note: if you are using CSI camera use CSI://0 instead. 

# Supported chords 

Open position:
* A-minor 
* C-major
* D-minor
* E-minor
* G-major
* F-major

# Miscelanneus
* Training was done using Washburn D10, Fender Stratocaster, and Gibson Flying V.

* Pictures that I used for training can be found from https://drive.google.com/drive/folders/1pQMNR8BMq57_aXnF-raINfqNA64tZvgN?usp=sharing

* chords.py select which chords are drawn after detection.

* staff.py is responsible of drawing chords on the staff

* chordmap.py is responsible of drawing chords on the map

# Maintainer
Rainer Waltzer @raiwal

# Contributing
Rainer Waltzer @raiwal

# Licence 
Free for non-commercial usage
