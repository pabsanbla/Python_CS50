class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        add = self.size + n
        if add > self.capacity:
            raise(ValueError)
        else:
            self.size = add

    def withdraw(self, n):
        if n > self.size:
            raise(ValueError)
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise(ValueError)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

