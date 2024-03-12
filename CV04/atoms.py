import playground
import random
from playground import Colors

class Atom:
    def __init__(self, x, y, rad, speed_x, speed_y, color):
        """
        Inicializator třídy Atom
        :param x: souřadnice X
        :param y: soouřadnice Y
        :param rad: poloměr
        :param color: barva
        """
        self.x = x
        self.y = y
        self.rad = rad
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        pass

    def to_tuple(self):
        """Vrátí n-tici hodnot
        příklad: x = 10, y = 12, rad = 15, color = 'green' -> (10,12,15,'green')
        """
        return self.x, self.y, self.rad, self.color
        pass

    def move(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.rad >= width or self.x - self.rad <= 0:
            self.speed_x *= -0.8

        if self.y + self.rad >= height or self.y - self.rad <= 0:
            self.speed_y *= -0.8
        pass

class FallDownAtom(Atom):
    g = 3
    damping = 0.8
    def move(self, width, height):
        self.speed_y += self.g
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.rad >= width or self.x - self.rad <= 0:
            self.speed_x *= -self.damping
        if self.y - self.rad <= 0:
            self.speed_y *= -self.damping
        elif self.y + self.rad >= height:
            self.y = height - self.rad
            self.speed_y *= -self.damping

class ExampleWorld(object):
    def __init__(self, size_x, size_y, count):
        self.width = size_x
        self.height = size_y
        self.atoms = []
        for i in range(count):
            atom = self.random_atom()
            self.atoms.append(atom)
    def random_atom(self):
        radius = random.randint(5, 20)
        x = random.randint(0, self.width - radius)
        y = random.randint(0, self.height - radius)
        speed_x = random.randint(-5, 5)
        speed_y = random.randint(-5, 5)
        color = random.choice([Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW])
        return FallDownAtom(x, y, radius, speed_x, speed_y, color)
        pass

    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.

        :param size_x: world size x dimension
        :param size_y: world size y dimension
        :return: tuple of atom objects, each containing (x, y, radius) coordinates
        """
        for atom in self.atoms:
            atom.move(self.width, self.height)
        return [atom.to_tuple() for atom in self.atoms]


if __name__ == '__main__':
    size_x, size_y, count = 720, 400, 50

    world = ExampleWorld(size_x, size_y, count)
    playground.run((size_x, size_y), world)
