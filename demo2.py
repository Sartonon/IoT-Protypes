import RPi.GPIO as GPIO
import time

LED = 20
TUNNISTIN = 23
PAINIKE = 19
AUTO_PUNAINEN = 26
AUTO_KELTAINEN = 13
AUTO_VIHREA = 6
JALKA_PUNAINEN = 16
JALKA_VIHREA = 21

GPIO.setmode (GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(PAINIKE, GPIO.IN)
GPIO.setup(TUNNISTIN, GPIO.IN)
GPIO.setup(AUTO_KELTAINEN, GPIO.OUT)
GPIO.setup(AUTO_PUNAINEN, GPIO.OUT)
GPIO.setup(AUTO_VIHREA, GPIO.OUT)
GPIO.setup(JALKA_PUNAINEN, GPIO.OUT)
GPIO.setup(JALKA_VIHREA, GPIO.OUT)

loppu = time.time() + 60
GPIO.output(AUTO_VIHREA, 1)
GPIO.output(JALKA_PUNAINEN, 1)

def autoVihreastaPunaiseksi():
	time.sleep(2)
	GPIO.output(AUTO_KELTAINEN, 1)
	GPIO.output(AUTO_VIHREA, 0)
	time.sleep(1)
	GPIO.output(AUTO_PUNAINEN, 1)
	GPIO.output(AUTO_KELTAINEN, 0)
	time.sleep(2)
	GPIO.output(JALKA_VIHREA, 1)
	GPIO.output(JALKA_PUNAINEN, 0)
	GPIO.output(LED, 0)

def autoPunaisestaVihreaksi():
	GPIO.output(JALKA_VIHREA, 0)
	GPIO.output(JALKA_PUNAINEN, 1)
	time.sleep(2)
	GPIO.output(AUTO_KELTAINEN, 1)
	time.sleep(2)
	GPIO.output(AUTO_KELTAINEN, 0)
	GPIO.output(AUTO_PUNAINEN, 0)
	GPIO.output(AUTO_VIHREA, 1)

def hoidaValot():
	autoVihreastaPunaiseksi()
	time.sleep(2)
	autoPunaisestaVihreaksi()

while time.time() < loppu:
	if GPIO.input(PAINIKE):
		GPIO.output(LED, 1)
		valotHoidettu = False
		loppu3 = time.time() + 20
		while time.time() < loppu3:
			time.sleep(1)
			if not GPIO.input(TUNNISTIN):
				hoidaValot()
				valotHoidettu = True
				break
		if not valotHoidettu:
			hoidaValot()

	time.sleep(0.1) # ilman tata prossukaytto 100%

GPIO.output(JALKA_PUNAINEN, 0)
GPIO.output(JALKA_VIHREA, 0)
GPIO.output(AUTO_PUNAINEN, 0)
GPIO.output(AUTO_PUNAINEN, 0)
GPIO.output(AUTO_KELTAINEN, 0)
GPIO.cleanup()
