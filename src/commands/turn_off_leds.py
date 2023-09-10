from .base import Command


class TurnOffLeds(Command):
    name = 'turn_off_leds'

    def execute(self):
        print('Turning off the LEDs')
