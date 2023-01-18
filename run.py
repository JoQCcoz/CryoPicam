from picamera2 import Picamera2
from picamera2.encoders import Encoder
from picamera2.outputs import FileOutput
import time
import sys
import io
import json
from settings import settings
from motion import MotionSensor
from pathlib import Path
from cam import apply_timestamp, meta
from process import load_raw_frames, filter_frames_by_timestamps, export_mp4, export_individual_frames, add_frames_timestamps

def prepare_outputs(run_name):
    directory = Path(settings.dataDir,run_name)
    directory.mkdir(parents=True)
    return directory


if __name__=="__main__":
    run_name = sys.argv[1]
    directory = prepare_outputs(run_name)

    picam2 = Picamera2()
    video_config = picam2.create_video_configuration(raw={'format':picam2.sensor_modes[1]['format'],'size':picam2.sensor_modes[1]['size']}, encode="raw", controls={"FrameDurationLimits": (8333, 8333)})
    picam2.configure(video_config)
    picam2.pre_callback = apply_timestamp
    encoder = Encoder()

    output = directory/'all_frames.raw'

    with MotionSensor(settings.sensorPin) as sensor:
        picam2.start_recording(encoder, str(output ))
        while sensor.activated():
            pass 
        print('Sensor activated!')
        start = time.time()
        time.sleep(1)
        picam2.stop_recording()

    print('Frames acquired, processing...')
    timestamps = [i-start for i in meta]
    with open(directory / 'meta.json','w') as f:
        json.dump([i-start for i in meta],f)
    with open(output,'r') as movie:
        movie_frames_arrays = load_raw_frames(movie,*picam2.sensor_modes[1]['size'])
    filtered_frames_arrays, filtered_timestamps = filter_frames_by_timestamps(movie_frames_arrays,timestamps)
    export_individual_frames(directory/'frames',filtered_frames_arrays)
    numbered_frames = add_frames_timestamps(filtered_frames_arrays,filtered_timestamps)
    export_mp4(str(directory/'movie.mp4'),filtered_frames_arrays, *picam2.sensor_modes[1]['size'])

        

        
        




