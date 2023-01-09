#!/usr/bin/python

# native
import argparse
import datetime
import os
from subprocess import Popen
# external
import cv2

parser = argparse.ArgumentParser(
    description='Parallelize video frame interpolation with FFmpeg.')
parser.add_argument('inputVideo',
                    type=argparse.FileType('r'),
                    help='an input video file')
parser.add_argument('--split',
                    metavar='N',
                    type=int,
                    required=True,
                    help='number of tasks to generate equally')
parser.add_argument('-o, --outputDir',
                    metavar='NAME',
                    default='output',
                    help='name of the output directory, default=\'output\'')
parser.add_argument('--fps',
                    metavar='N',
                    type=int,
                    default=60,
                    help='target FPS, default=60')
parser.add_argument('--shutdown',
                    action='store_true',
                    help='shutdown computer after tasks are completed')

args = vars(parser.parse_args())

# create video capture object
videoData = cv2.VideoCapture(args['inputVideo'].name)
# count the number of frames
frames = videoData.get(cv2.CAP_PROP_FRAME_COUNT)
fps = videoData.get(cv2.CAP_PROP_FPS)
videoSeconds = round(frames / fps)
# calculate duration of the splitted parts
partsSeconds = round(videoSeconds / args['split'])
partsTime = datetime.timedelta(seconds=partsSeconds)

# create output dir if not exists
if os.path.isdir(args['o, __outputDir']) == False:
    os.makedirs(args['o, __outputDir'])

# create and write the input text file for ffmpeg concat
f = open(f"{args['o, __outputDir']}/list.txt", 'x')
for i in range(args['split']):
    f.write(f"file 'output{str(i).zfill(3)}.{args['fps']}fps.mp4'\n")
f.close()

# write batch file
f = open(f"{args['o, __outputDir']}/run.bat", 'x')
f.write(
    f"ffmpeg -i \".{args['inputVideo'].name}\" -c copy -map 0 -segment_time {partsTime} -f segment -reset_timestamps 1 output%%03d.mp4\n")

# launch all ffmpeg tasks in parallel
# continue only when everything is finished
f.write('(\n')
for i in range(args['split']):
    f.write(
        f"  start \"TASK {i+1}\" ffmpeg -i output{str(i).zfill(3)}.mp4 -crf 10 -vf \"minterpolate=fps={args['fps']}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1\" output{str(i).zfill(3)}.{args['fps']}fps.mp4\n")
f.write(') | pause\n')

f.write('timeout /t 3 /nobreak > nul\n')
f.write('ffmpeg -f concat -safe 0 -i list.txt -c copy final.mp4\n')

if args['shutdown']:
    f.write('timeout /t 3 /nobreak > nul\n')
    f.write('shutdown /s /f /t 0\n')
f.close()

# execute batch file
os.chdir(os.path.join(os.path.dirname(__file__), 'output'))
Popen('run.bat')
