# 1

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def some_method(self):
        print("Метод Singleton")


s1 = Singleton()
s2 = Singleton()

s1.value = 100

print(s2.value)
print(s1 is s2)

s1.some_method()

# 2
from abc import ABC, abstractmethod


class Logger(ABC):

    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):

    def log(self, message):
        print("Logging to file:", message)


class ConsoleLogger(Logger):

    def log(self, message):
        print("Logging to console:", message)


class LoggerFactory(ABC):

    @abstractmethod
    def create_logger(self):
        pass

    def log_message(self, message):
        logger = self.create_logger()
        logger.log(message)


class FileLoggerFactory(LoggerFactory):

    def create_logger(self):
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):

    def create_logger(self):
        return ConsoleLogger()


factory1 = FileLoggerFactory()
factory2 = ConsoleLoggerFactory()

factory1.log_message("Hello")
factory2.log_message("Hello")


# 3

from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):

    def paint(self):
        print("Windows button")


class MacButton(Button):

    def paint(self):
        print("Mac button")


class Checkbox(ABC):

    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox):

    def paint(self):
        print("Windows checkbox")


class MacCheckbox(Checkbox):

    def paint(self):
        print("Mac checkbox")


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application:

    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()


app1 = Application(WindowsFactory())
app1.paint()

app2 = Application(MacFactory())
app2.paint()

# 4

from abc import ABC, abstractmethod


class Pizza:

    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping

    def __str__(self):
        return f"Pizza(dough={self.dough}, sauce={self.sauce}, topping={self.topping})"


class PizzaBuilder(ABC):

    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_topping(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class HawaiianPizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("cross")

    def build_sauce(self):
        self.pizza.set_sauce("mild")

    def build_topping(self):
        self.pizza.set_topping("ham+pineapple")

    def get_result(self):
        return self.pizza


class PizzaDirector:

    def __init__(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


builder = HawaiianPizzaBuilder()
director = PizzaDirector(builder)

director.construct_pizza()

pizza = builder.get_result()

print(pizza)