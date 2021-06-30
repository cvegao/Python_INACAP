class Card:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Unit(Card):
    def __init__(self, name, cost, resilience, power):
        super().__init__(name, cost)
        self.resilience = resilience
        self.power = power

    def attack(self, target):
        target.resilience -= self.power
        return self


class Effect(Card):
    def __init__(self, name, cost, stat, magnitude):
        super().__init__(name, cost)
        self.stat = stat
        self.magnitude = magnitude

    def play(self, target):
        if isinstance(target, Unit):
            if self.stat == "resilience":
                target.resilience += self.magnitude
            else:
                target.power += self.magnitude
            if self.magnitude < 0:
                print("Lower the target's", self.stat, "by", abs(self.magnitude))
            else:
                print("Raise the target's", self.stat, "by", self.magnitude)
        else:
            raise Exception("Target must be an unit!")
        return self


def create_units():
    return [Unit("Ninja Cinturón Rojo", 3, 4, 3),
            Unit("Ninja Cinturón Negro", 4, 4, 5)]


def create_effects():
    return [Effect("Algoritmo Duro", 2, "resilience", 3),
            Effect("Promesa no Manejada", 1, "resilience", -2),
            Effect("Programación en Pareja", 3, "power", 2)]

