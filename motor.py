import time
import math
import RPi.GPIO as GPIO


class StepperMotor():

    def __init__(self, pins):
        self.pins = pins
        self.resetPins()

    def resetPins(self, mode=GPIO.BCM):
        GPIO.setmode(mode)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def rotate(self, degrees):
        SEQUENCE = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1]
        ]

        numberOfSteps = int(abs(degrees) / float(360 / float(4096)))
        stepCount = len(SEQUENCE) - 1

        stepDir = int(math.copysign(1, degrees))

        maxValue = int(math.floor(numberOfSteps)) if stepDir == 1 else 0
        minValue = 0 if stepDir == 1 else int(math.floor(numberOfSteps))

        for step in range(minValue, maxValue, stepDir):
            row = step % stepCount
            for pin in range(0, len(self.pins)):
                GPIO.output(self.pins[pin], SEQUENCE[row][pin] == max(0, stepDir))

            time.sleep(0.001)

    @staticmethod
    def cleanup():
        GPIO.cleanup()
