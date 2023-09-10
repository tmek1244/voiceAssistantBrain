from .base import Command


class TurnOnLeds(Command):
    name = 'turn_on_leds'

    def execute(self):
        print('Turning on the LEDs')
