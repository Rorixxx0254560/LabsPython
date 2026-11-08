# 1

from abc import ABC, abstractmethod


class AttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass


class SwordAttack(AttackStrategy):
    def attack(self):
        print("Атака мечом")


class BowAttack(AttackStrategy):
    def attack(self):
        print("Атака луком")


class Player:
    def __init__(self, strategy):
        self.strategy = strategy

    def attack(self):
        self.strategy.attack()


player = Player(SwordAttack())
player.attack()

player.strategy = BowAttack()
player.attack()


# 2

class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, level):
        if self.next_handler:
            self.next_handler.handle(level)


class Operator(Handler):
    def handle(self, level):
        if level == 1:
            print("Проблему решил оператор")
        else:
            super().handle(level)


class Manager(Handler):
    def handle(self, level):
        if level == 2:
            print("Проблему решил менеджер")
        else:
            super().handle(level)


class Director(Handler):
    def handle(self, level):
        if level == 3:
            print("Проблему решил директор")
        else:
            super().handle(level)


director = Director()
manager = Manager(director)
operator = Operator(manager)

operator.handle(3)


# 3

class MyIterator:
    def __init__(self, items):
        self.items = items
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < len(self.items):
            item = self.items[self.position]
            self.position += 1
            return item

        raise StopIteration


numbers = [10, 20, 30, 40]

iterator = MyIterator(numbers)

for number in iterator:
    print(number)