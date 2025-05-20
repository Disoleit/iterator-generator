
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        
    def __iter__(self):
        self.inner = -1
        self.outer = 0
        return self

    def __next__(self):
        self.inner += 1
        if self.inner >= len(self.list_of_lists[self.outer]):
            self.outer += 1
            self.inner = 0 
        if self.outer >= len(self.list_of_lists):
            raise StopIteration
        return self.list_of_lists[self.outer][self.inner]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()