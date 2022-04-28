from gpiozero import MotionSensor, LED
#from time import sleep, time
from signal import pause

# Configurating Raspberry Pi GPIO pin

pir = MotionSensor(4)
red = LED(19)
yellow = LED(20)

# A function to detect motion
def on_motion():
        print('Motion detected!')
        red.off()
        yellow.on()

# A function when no motion is detected
def no_motion():
        print('No motion detected')
        print('No motion detected')
        red.on()
        yellow.off()

pir.when_motion = on_motion
pir.when_no_motion = no_motion

pause()

