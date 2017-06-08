import picamera
import RPi.GPIO as GPIO
import time
from time import sleep

TUNNISTIN = 13

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

# camera.capture('kuva.jpg')

# camera.start_recording('video.h264')
# sleep(15)
# camera.stop_recording()

GPIO.setmode (GPIO.BCM)
GPIO.setup(TUNNISTIN, GPIO.IN)

loppu = time.time() + 5

while time.time() < loppu:
  if GPIO.input(TUNNISTIN):
    print("Liiketta")
    camera.capture('kuva.jpg')
  if not GPIO.input(TUNNISTIN):
    print("Ei Liiketta")

  sleep(0.1)

GPIO.cleanup()
