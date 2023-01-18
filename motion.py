from settings import settings
import RPi.GPIO as GPIO

class MotionSensor:

    def __init__(self,pin:int):
        self.pin = pin
        self.setup()
    
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        GPIO.cleanup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin,GPIO.IN)

    def activated(self):
        check = GPIO.input(self.pin)
        return check

