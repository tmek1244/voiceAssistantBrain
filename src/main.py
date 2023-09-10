from flask import Flask

from brain import Brain


app = Flask(__name__)


@app.post('/audio')
def receive_audio():
    ...


if __name__ == "__main__":
    brain = Brain()

    brain.read_commands_from_file()
    # brain.add_new_nickname('turn_on_leds', 'turn on the lights')
