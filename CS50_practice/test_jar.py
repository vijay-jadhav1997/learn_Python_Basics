from jar import Jar
import pytest


def main():
  test_init()
  test_str()
  test_deposite()
  test_withdraw()


def test_init():
  jar = Jar()
  assert jar.capacity == 12
  jar.capacity = 20
  assert jar.capacity == 20

  # test If capacity is a non-negative int, should instead raise a ValueError.
  with pytest.raises(ValueError):
    jar = Jar(-10)
    


def test_str():
  jar = Jar(25)
  assert str(jar) == ""
  jar.deposit(1)
  assert str(jar) == "🍪"
  jar.deposit(5)
  assert str(jar) == "🍪🍪🍪🍪🍪🍪"
  jar.deposit(10)
  assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
  jar.withdraw(11)
  assert jar.__str__() == "🍪🍪🍪🍪🍪"


def test_deposite():
  jar = Jar(50)
  assert jar._size == 0
  jar.deposit(12)
  assert jar._size == 12
  jar.deposit(10)
  assert jar._size == 22
  with pytest.raises(ValueError):
    cooky_jar = Jar(20)
    cooky_jar.deposit(25)


def test_withdraw():
  jar = Jar(50)
  jar.deposit(50)
  jar.withdraw(10)
  assert jar._size == 40
  jar.withdraw(10)
  assert jar._size == 30
  jar.withdraw(30)
  assert jar._size == 0

  with pytest.raises(ValueError):
    jar.withdraw(5)

  with pytest.raises(ValueError):
    cooky_jar = Jar(50)
    cooky_jar.deposit(25)
    cooky_jar.withdraw(50)



if __name__ == "__main__":
  main()
