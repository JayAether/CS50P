class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError('deposit exceeds capacity')
        else:
            self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError('cannot withdraw more than 0')
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('cannot have negitive capacity')
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
