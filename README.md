# Description
Program to recognize basic chords and after recognition suggest alternative chords.

This is based on jetson-inference course and 

# Run
python3 main.py --model=model/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=labels.txt /dev/video0

