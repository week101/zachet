class FlattenIterator:
    def __init__(self, nested_container):
        self._items = nested_container[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        while self._items:
            element = self._items.pop()
            if type(element) is list:
                self._items.extend(element[::-1])
            else:
                return element
        raise StopIteration


nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)