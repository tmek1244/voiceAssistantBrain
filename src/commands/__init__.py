from .base import Command

from .turn_on_leds import TurnOnLeds
from .turn_off_leds import TurnOffLeds


COMMANDS: dict[str, Command] = {
    cls.name: cls for cls in [
        TurnOnLeds,
        TurnOffLeds,
    ]
}
