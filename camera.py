from picamera2 import Picamera2
import pprint

picam2 = Picamera2()
pprint.pprint(picam2.sensor_modes)
# print(picam2.sensor_modes[0])
# config = picam2.create_video_configuration(controls={"FrameDurationLimits": (40000, 40000)})
