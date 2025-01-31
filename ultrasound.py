import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)  # GPIO25 as Trig
GPIO.setup(27, GPIO.IN)   # GPIO27 as Echo

# Define a function called distance
def distance():
    # Produce a 10us pulse at Trig
    GPIO.output(25, 1)
    time.sleep(0.00001)
    GPIO.output(25, 0)

    # Measure pulse width (i.e. time of flight) at Echo
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(27) == 0:
        StartTime = time.time()  # Capture start of high pulse

    while GPIO.input(27) == 1:
        StopTime = time.time()  # Capture end of high pulse

    ElapsedTime = StopTime - StartTime
    # Compute distance in cm, from time of flight
    Distance = (ElapsedTime * 34300) / 2  # Speed of sound = 34300 cm/s
    return Distance

# Main loop
while True:
    print("Measured distance = {0:0.1f} cm".format(distance()))
    time.sleep(1)
