class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("negative capacity")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("too much cookies")
        self._cookies += n

    def withdraw(self, n):
        if self._cookies < n:
            raise ValueError("Not enough cookies")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
