def main():
  aassignment_operators()

"""Assignment operators (=, +=, -=, /=, //= etc.) """

#? Assignment operators are used to assign values to variables

def aassignment_operators():
  """Assignment operator combined with arithmetic and bitwise operators"""

  # Assignment: +=
  number = 5
  number += 3
  print(number)

  # Assignment: -=
  number = 5
  number -= 3
  print(number)

  # Assignment: *=
  number = 5
  number *= 3
  print(number)

  # Assignment: /=
  number = 8
  number /= 4
  print(number)

  # Assignment: %=
  number = 8
  number %= 3
  print(number)

  # Assignment: %=
  number = 5
  number %= 3
  print(number)

  # Assignment: //=
  number = 5
  number //= 3
  print(number)

  # Assignment: **=
  number = 5
  number **= 3
  print(number)

  # Assignment: &=
  number = 5  # 0b0101
  number &= 3  # 0b0011
  print(number)  # 0b0001

  # Assignment: |=
  number = 5  # 0b0101
  number |= 3  # 0b0011
  print(number)  # 0b0111

  # Assignment: ^=
  number = 5  # 0b0101
  number ^= 3  # 0b0011
  print(number)  # 0b0110

  # Assignment: >>=
  number = 5
  number >>= 3
  print(number)  # (((5 // 2) // 2) // 2)

  # Assignment: <<=
  number = 5
  number <<= 4
  print(number)  # 5 * 2 * 2 * 2 * 2 


if __name__ == "__main__":
  main()