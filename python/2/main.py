from abc import ABC, abstractmethod


class GameObject(ABC):

    def init(self, object_id, name, X, Y):
        self.object_id = object_id
        self.__name = name
        self._X = X
        self._Y = Y

    def getID(self):
        print(self.__object_id)

    def getName(self):
        print(self.__name)

    def getX(self):
        print(self._X)

    def getY(self):
        print(self._Y)


class Attacker(ABC):

    @abstractmethod
    def attack(self, unit):
        """Атаковать указанного юнита."""
        raise NotImplementedError


class Moveable(ABC):

    @abstractmethod
    def move(self, X, Y):
        """Переместиться в новые координаты."""
        raise NotImplementedError


class Unit(GameObject, ABC):

    def __init(self, object_id, name, X, Y, hp):
        super().init(object_id, name, X, Y)
        self.hp = hp

    def is_Allive(self):
        return self.__hp > 0

    def getHp(self):
        return self.__hp

    def receiveDamage(self, damage):
        if self.__hp - damage >= 0:
            self.__hp -= damage
        else:
            self.__hp = 0


class Archer(Unit, Attacker, Moveable):

    def __init(self, object_id, name, X, Y, hp, damage):
        super().init(object_id, name, X, Y, hp)
        self.damage = damage

    def attack(self, unit):
        if self.is_Allive() and unit.is_Allive():
            unit.receiveDamage(self.__damage)

    def move(self, X, Y):
        if self.is_Allive():
            self._X = X
            self._Y = Y


class Building(GameObject, ABC):

    def __init(self, object_id, name, X, Y, built):
        super().init(object_id, name, X, Y)
        self.built = built

    def is_Built(self):
        return self.__built


class Fort(Building, Attacker):

    def __init(self, object_id, name, X, Y, built, damage):
        super().init(object_id, name, X, Y, built)
        self.damage = damage

    def attack(self, unit):
        if self.is_Built() and unit.is_Allive():
            unit.receiveDamage(self.__damage)


class MobileHouse(Building, Moveable):

    def __init(self, object_id, name, X, Y, built):
        super().init(object_id, name, X, Y, built)

    def move(self, X, Y):
        self._X = X
        self._Y = Y


archer1 = Archer(1, "Roma", 10, 20, 100, 30)
archer2 = Archer(2, "Sveta", 30, 40, 200, 50)

fort = Fort(3, "Fort", 10, 20, True, 70)

house = MobileHouse(4, "House", 5, 5, True)


print("HP Sveta:", archer2.getHp())

archer1.attack(archer2)
print("Roma атаковал Sveta")
print("HP Sveta:", archer2.getHp())

print()

print("HP Roma:", archer1.getHp())

fort.attack(archer1)
print("Fort атаковал Roma")
print("HP Roma:", archer1.getHp())

print()

print("Roma жив?", archer1.is_Allive())
print("Sveta жив?", archer2.is_Allive())

print()

print("Координаты Sveta до:")
archer2.getX()
archer2.getY()

archer2.move(50, 60)

print("Sveta переместился")
print("Координаты Sveta после:")
archer2.getX()
archer2.getY()

print()

print("Координаты дома до:")
house.getX()
house.getY()

house.move(100, 200)

print("Дом переместился")
print("Координаты дома после:")
house.getX()
house.getY()
