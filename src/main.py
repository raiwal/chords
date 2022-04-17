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
# this was googlenet
parser.add_argument("--network", type=str, default="resnet-18", help="pre-trained model to load (see below for options)")
parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--headless", action='store_true', default=(), help="run without display")
parser.add_argument("--chord_extension", type=str, default="no", help="display fingering extended chord. Seventh or are currently supported")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

if opt.chord_extension == 'seventh':
	print("OK. Seventh is displayed")
if opt.chord_extension == 'ninth':
	print("OK. Ninth is displayed")

#print(opt.network)
#print(sys.argv)
#sys.exit(0)
# load the recognition network
net = jetson.inference.imageNet(opt.network, sys.argv)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)
font = jetson.utils.cudaFont()

# Load template for six string guitar
chord_template = jetson.utils.loadImage('../images/chord_chart_with_treble_clef.png')

# process frames until the user exits
while True:
	# chord_map = chord_template
	chord_map = jetson.utils.cudaMemcpy(chord_template)
	# capture the next image
	img = input.Capture()

	#jetson.utils.cudaOverlay()

	# classify the image
	class_id, confidence = net.Classify(img)

	# find the object description
	class_desc = net.GetClassDesc(class_id)
	# chordlayout.draw_C_major(chord_template)
	chords.chord_drawing(class_desc, chord_map, opt.chord_extension)

	# overlay the result on the image	
	font.OverlayText(img, img.width, img.height, "{:05.2f}% {:s}".format(confidence * 100, class_desc), 5, 5, font.White, font.Gray40)
	
	imgOutput = jetson.utils.cudaAllocMapped(width=1280, height=720, format=img.format)
	# Position chordmap 
	jetson.utils.cudaOverlay(img, imgOutput, 0,0)	# render the image
	jetson.utils.cudaOverlay(chord_map, imgOutput, 950, 450)	# render the chord map image
	output.Render(imgOutput)

	# update the title bar
	output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))

	# print out performance info
	# net.PrintProfilerTimes()

	# exit on input/output EOS
	if not input.IsStreaming() or not output.IsStreaming():
		break