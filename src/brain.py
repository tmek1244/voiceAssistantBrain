import json
from dataclasses import dataclass, field

from commands.base import Command
from commands import COMMANDS


@dataclass
class Brain:
    commands_by_name: dict[str, Command] = field(default_factory=dict)
    commands_config_path: str = 'commands/config.json'

    def read_commands_from_file(self):
        with open(self.commands_config_path) as file:
            commands_config = json.load(file)
        print(commands_config)
        print(COMMANDS)
        for command_name, config in commands_config.items():
            for nickname in config['nicknames']:
                self.commands_by_name[nickname] = COMMANDS[command_name]
        print(self.commands_by_name)
    
    def add_new_nickname(self, command_name: str, nickname: str):
        self.commands_by_name[nickname] = COMMANDS[command_name]

        with open(self.commands_config_path) as file:
            commands_config = json.load(file)
        commands_config[command_name]["nicknames"].append(nickname)

        with open(self.commands_config_path, 'w') as file:
            json.dump(commands_config, file, indent=4)        
