1

from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def get_balance(self):
        pass


class RealBankAccount(BankAccount):

    def get_balance(self):
        print("Баланс: 15000 рублей")


class BankAccountProxy(BankAccount):

    def __init__(self, pin):
        self.account = RealBankAccount()
        self.pin = pin

    def get_balance(self):
        if self.pin == "1234":
            self.account.get_balance()
        else:
            print("Неверный PIN-код")


account1 = BankAccountProxy("1234")
account2 = BankAccountProxy("0000")

account1.get_balance()
account2.get_balance()

2

from abc import ABC, abstractmethod


class USB_C(ABC):

    @abstractmethod
    def charge(self):
        pass


class OldCharger:

    def charge_micro_usb(self):
        print("Зарядка через Micro-USB")


class ChargerAdapter(USB_C):

    def __init__(self, charger):
        self.charger = charger

    def charge(self):
        self.charger.charge_micro_usb()


old_charger = OldCharger()

adapter = ChargerAdapter(old_charger)

adapter.charge()

3

from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def move(self):
        pass


class Car(Transport):

    def move(self):
        print("Автомобиль едет")


class Boat(Transport):

    def move(self):
        print("Лодка плывёт")


class Controller(ABC):

    def __init__(self, transport):
        self.transport = transport

    @abstractmethod
    def control(self):
        pass


class ManualController(Controller):

    def control(self):
        print("Ручное управление:")
        self.transport.move()


class AutoController(Controller):

    def control(self):
        print("Автоматическое управление:")
        self.transport.move()


car = Car()
boat = Boat()

control1 = ManualController(car)
control2 = AutoController(car)
control3 = ManualController(boat)
control4 = AutoController(boat)

control1.control()
control2.control()
control3.control()
control4.control()