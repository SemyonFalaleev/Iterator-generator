class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def _flatten(self, list_):
        for item in list_:
            if isinstance(item, list):
                self._flatten(item)
            else:
                self.flat_list.append(item)

    def __iter__(self):
        self.flat_list = []
        self._flatten(self.list)    
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= len(self.flat_list):
            raise StopIteration
        item = self.flat_list[self.cursor]
        self.cursor += 1
        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
