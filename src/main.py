import jetson.inference
import jetson.utils
import chords
import argparse
import sys

# parse the command line
parser = argparse.ArgumentParser(description="Classify basic guitarchords from a live camera stream using an image recognition DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.imageNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="resnet-18", help="pre-trained model to load (see below for options)")
parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")

# Upper left corner coordinates for drawn chordmap
chordmap_location_x = 30
chordmap_location_y = 37
# confidence information location from top left corner
confidence_location_x = 5
confidence_location_y = 5

try:
	opt = parser.parse_known_args()[0]
except:
	parser.print_help()
	sys.exit(0)

# load the recognition network
net = jetson.inference.imageNet(opt.network, sys.argv)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv) 
font = jetson.utils.cudaFont()

# Load template for six string guitar
chord_template = jetson.utils.loadImage('../images/chord_chart_with_treble_clef.png')

# process frames until the user exits
while True:
	chord_map = jetson.utils.cudaMemcpy(chord_template)
	# capture the next image
	img = input.Capture()

	# classify the image
	class_id, confidence = net.Classify(img)

	# find the object description
	class_desc = net.GetClassDesc(class_id)

	chords.chord_drawing(class_desc, chord_map)

	# overlay the result on the image	
	font.OverlayText(img, img.width, img.height, "{:05.2f}% {:s}".format(confidence * 100, class_desc), confidence_location_x, confidence_location_y, font.Black, font.Gray40)
	
	imgOutput = jetson.utils.cudaAllocMapped(width=opt.width, height=opt.height, format=img.format)
	# Position chordmap with the camera image
	jetson.utils.cudaOverlay(img, imgOutput, 0,0)
	jetson.utils.cudaOverlay(chord_map, imgOutput, chordmap_location_x, chordmap_location_y)	
	output.Render(imgOutput)

	# update the title bar net.GetNetworkName()
	output.SetStatus("{:s} | Network {:.0f} FPS".format("Basic chords", net.GetNetworkFPS()))

	# exit on input/output EOS
	if not input.IsStreaming() or not output.IsStreaming():
		break
