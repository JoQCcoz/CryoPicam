from picamera2 import MappedArray
import time

meta = []

def apply_timestamp(request): 
    timestamp = time.time()
    with MappedArray(request, "raw") as m: 
        meta.append(timestamp)


