import cv2
import numpy as np
import matplotlib.pyplot as plt
from typing import List
from pathlib import Path


colour = 255
origin = (0, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2

def load_raw_frames(fileHandle,cols,rows):
    movie_frames_arrays = []
    movie_buffer = np.fromfile(fileHandle, dtype=np.uint8)
    frames = int(np.shape(movie_buffer)[0]/(rows*cols))
    movie_frames_buffers = movie_buffer.reshape((frames,rows*cols))
    for i in movie_frames_buffers:
        movie_frames_arrays.append(i.reshape(rows,cols))
    return movie_frames_arrays

def add_frame_timestamp(frame, timestamp:float, frame_index:int=None):
    text = ''
    if frame_index is not None:
        text += f'Frame {frame_index}, '
    text += f'{round(timestamp*1000)} ms'
    cv2.putText(frame, text, origin, font, scale, colour, thickness)
    return frame

def add_frames_timestamps(frames_arrays:List, timestamps:List):
    im_list = []
    for ind, (frame,timestamp) in enumerate(zip(frames_arrays,timestamps)):   
        im_list.append(add_frame_timestamp(frame,timestamp,ind))
    return im_list

def filter_frame_by_timestamp(timestamp:float, timestamp_range=[-0.05,0.3]):
    if min(timestamp_range) < timestamp < max(timestamp_range):
        return True

def filter_frames_by_timestamps(frames_arrays:List, timestamps:List, timestamp_range=[-0.05,0.3]):
    im_list = []
    timestamp_list = []
    for frame,timestamp in zip(frames_arrays,timestamps):   
        if filter_frame_by_timestamp(timestamp,timestamp_range):
            im_list.append(frame)
            timestamp_list.append(timestamp)
    return im_list, timestamp_list

def export_individual_frames(directory, frames_arrays:List):
    directory.mkdir(exist_ok=True)
    for ind, frame in enumerate(frames_arrays):
        cv2.imwrite(str(Path(directory, f'{str(ind).zfill(2)}.png')), frame)

def export_mp4(outputfile, frames, cols,rows, fps:int=5):
    out = cv2.VideoWriter(outputfile, cv2.VideoWriter_fourcc(*'mp4v'), fps, (cols,rows), False)
    for i in frames:
        out.write(i)
    out.release()