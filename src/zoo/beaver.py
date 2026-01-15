
# beaver.py

from .animal import Animal


class Beaver(Animal):
    def __init__(self, name="Meng"):
        super().__init__(name, species="Beaver")

    def sound(self):
        return "I love Hamilton!"

    def action(self):
        return "No comment..."
    
Meng = Beaver(name="Meng")
    
def test_sound():
    assert Meng.sound() == "I love Hamilton!"

def test_action():
    assert Meng.action() == "No comment..."
