from abc import ABC, abstractmethod

class Clothes:

    def __init__(self, volume, height):
        self.volume = volume
        self.height = height

    @abstractmethod
    def material_calc(self):
        pass

class Coat(Clothes):

    def __init__(self, volume, height):
        self.volume = volume
        self.height = height

    @property
    def material_calc(self):
        material = self.volume / 6.5 + 0.5
        print(material)


class Suit(Clothes):

    def __init__(self, volume, height):
        self.volume = volume
        self.height = height

    @property
    def material_calc(self):
        material = 2 * self.height + 0.3
        print(material)

street_coat = Coat(2, 4)
business_suit = Suit(3, 3)

street_coat.material_calc
business_suit.material_calc