class Calculation:
    def add(self, a, b):
        return a + b

    def reduce(self, a, b):
        return a - b

    def ride(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


if __name__ == '__main__':
    print(Calculation().add(1, 2))
