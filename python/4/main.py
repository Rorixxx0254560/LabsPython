# 1

from abc import ABC, abstractmethod


class SortingStrategy(ABC):

    @abstractmethod
    def sort(self, array):
        pass


class BubbleSortStrategy(SortingStrategy):

    def sort(self, array):
        print("Сортировка пузырьком")


class QuickSortStrategy(SortingStrategy):

    def sort(self, array):
        print("Быстрая сортировка")


class Sorter:

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_array(self, array):
        self.strategy.sort(array)


sorter = Sorter()

sorter.set_strategy(BubbleSortStrategy())
sorter.sort_array([5, 3, 8, 4, 2])

sorter.set_strategy(QuickSortStrategy())
sorter.sort_array([5, 3, 8, 4, 2])


# 2


from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    @abstractmethod
    def handle_request(self, request):
        pass


class HandlerA(Handler):

    def handle_request(self, request):
        if request == "A":
            print("HandlerA обработал запрос")
        elif self.next_handler:
            self.next_handler.handle_request(request)


class HandlerB(Handler):

    def handle_request(self, request):
        if request == "B":
            print("HandlerB обработал запрос")
        elif self.next_handler:
            self.next_handler.handle_request(request)


handler_a = HandlerA()
handler_b = HandlerB()

handler_a.set_next_handler(handler_b)

handler_a.handle_request("A")
handler_a.handle_request("B")

# 3

class ArrayIterator:

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


array = [10, 20, 30, 40, 50]

iterator = ArrayIterator(array)

for item in iterator:
    print(item)