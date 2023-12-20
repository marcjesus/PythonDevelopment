class SquaresIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max_value:
            raise StopIteration
        else:
            result = self.current ** 2
            self.current += 1
            return result


# Using the iterator
squares = SquaresIterator(5)  # It will generate squares of numbers from 0 to 4

for square in squares:
    print(square)

#OUTPUT 0 1 4 9 16
