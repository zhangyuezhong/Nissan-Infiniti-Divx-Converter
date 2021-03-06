#!/usr/bin/env python

# Convert input file to AVI via ffmpeg for use in Nissan/Infiniti Nav units
# Assumes that ffmpeg is installed

import argparse
import subprocess

# Get the argument from command line and store it as the inputfile var
parser = argparse.ArgumentParser(description='Convert a file for use in Nissan Infiniti Nav')
parser.add_argument("inputarg", metavar='C', type=str, nargs=1,
                    help='a filename for conversion via ffmpeg')
args = parser.parse_args()

# Convert the input argument from a list to a string named "inputfile"
inputfile = ''.join(args.inputarg)

# These are the arguments used by ffmpeg to do the conversion
ffmpegargs = " -f avi -r 29.97 -vcodec libxvid -vtag xvid -vf scale=704:-1 -aspect 16:9 -maxrate 8000k -b:v 6000k -qmin 3 -qmax 5 -bufsize 4096 -mbd 2 -bf 2 -trellis 1 -flags +aic -cmp 2 -subcmp 2 -g 300 -acodec ac3 -ar 48000 -aq 2"

# Remove the file extension using '.' as a separator, replace it with avi
sep = '.'
outputfile = inputfile.rsplit(sep, 1)[0] + ".avi"

# Run ffmpeg with the inputfile, the outputfile and the arguments specified above
command = "ffmpeg -i" + " \"" + inputfile + "\" " + ffmpegargs + " \"" + outputfile + "\""
print("Command to run: %s" % command)
subprocess.call(command, shell=True)
