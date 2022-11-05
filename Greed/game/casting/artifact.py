from game.casting.actor import Actor
import pyray


class Artifact(Actor):
    """Create Rocks and Gems on the screen"""

    def __init__(self):
        super().__init__()
        self._message = ''

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message
