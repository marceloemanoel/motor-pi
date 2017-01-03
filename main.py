import sys
from motor import StepperMotor


try:
    VERTICAL_DEGREES = float(sys.argv[1])
    VERTICAL_MOTOR_PINS = [7, 8, 25, 24]
    verticalMotor = StepperMotor(VERTICAL_MOTOR_PINS)
    verticalMotor.rotate(VERTICAL_DEGREES)

    HORIZONTAL_DEGREES = float(sys.argv[2])
    HORIZONTAL_MOTOR_PINS = [2, 3, 4, 14]
    horizontalMotor = StepperMotor(HORIZONTAL_MOTOR_PINS)
    horizontalMotor.rotate(HORIZONTAL_DEGREES)
finally:
    StepperMotor.cleanup()
