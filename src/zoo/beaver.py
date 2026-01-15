
# beaver.py

from .animal import Animal


class Elephant(Animal):
    def __init__(self, name="Meng"):
        super().__init__(name, species="Beaver")

    def sound(self):
        return "I love Hamilton!"

    def action(self):
        return "No comment..."
    
    def test_sound(self):
        assert self.sound == "I love Hamilton!"

    def test_action(self):
        assert self.action == "No comment..."
