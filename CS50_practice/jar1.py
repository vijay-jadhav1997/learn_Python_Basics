class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = int(capacity)
        self._size = 0

    def __str__(self):
        return f"{self._size * "🍪"}"

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError(f"Exeeding the capacity ({self._capacity}) of jar")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError(f"Insufficient amount of cookies in jar, only available {self._size}")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    j = Jar(25)
    print(j.size)


if __name__ == "__main__":
    main()
