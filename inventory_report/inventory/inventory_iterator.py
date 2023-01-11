from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        try:
            response = self.iterable[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return response
