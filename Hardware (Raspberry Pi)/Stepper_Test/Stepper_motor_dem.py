import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)  # Disable warnings

# Define GPIO pins connected to the stepper motor.
step_pins = [17, 18]

# Set up GPIO channels
GPIO.setmode(GPIO.BCM)
for pin in step_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

# Define the sequence of control signals for full-step mode
step_count = len(step_pins)
seq = []
seq.append([1, 0, 0, 0])
seq.append([0, 1, 0, 0])
seq.append([0, 0, 1, 0])
seq.append([0, 0, 0, 1])

# Define variables to control the speed and rotation direction.
step_dir = 1  # Set to 1 or -1
step_time = 0.005  # Time to wait (in seconds)

try:
    while True:  # Loop until Ctrl+C
        for i in range(step_count):
            # Set each pin
            for pin in range(2):
                GPIO.output(step_pins[pin], seq[i][pin])
            time.sleep(step_time)
except KeyboardInterrupt:
    # Ctrl+C was pressed, clean up and exit
    GPIO.cleanup()
