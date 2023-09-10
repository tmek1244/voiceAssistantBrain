from dataclasses import dataclass


@dataclass
class Command:
    name: str

    def execute(self):
        raise NotImplementedError()
