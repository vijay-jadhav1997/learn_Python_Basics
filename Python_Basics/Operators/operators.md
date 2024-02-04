# Operators

- Arithmetic Operators (+, -, \*, /, //, %, \*\*)
- Bitwise Operators (&, |, ^, >>, <<, ~)
- Assignment Operators (=, +=, -=, /=, //= etc.)
- Comparison Operator (==, !=, >, <, >=, <=)
- Logical Operators (and, or, not)
- Identity Operators (is, is not)
- Membership Operators (in, not in)

### 1. Arithmetic Operators:

- Addition (+): Adds two values.

  ```py
  num1 = 20
  num2 = 10
  result = num1 + num2
  print(result) # Output: 30
  ```

- Substraction (-): Subtracts the right operand from the left operand.

  ```py
  num1 = 20
  num2 = 10
  result = num1 - num2
  print(result) # Output: 10
  ```

- Multiplication (\*): Multiplies two values.

  ```py
  num1 = 20
  num2 = 10
  result = num1 * num2
  print(result) # Output: 200
  ```

- Division (/): Divides the left operand by the right operand. Returns a floating-point number.

  ```py
  num1 = 20
  num2 = 10
  result = num1 / num2
  print(result) # Output: 2.0
  ```

- Modulud (%): Returns the remainder of the division of the left operand by the right operand.

  ```py
  num1 = 25
  num2 = 10
  result = num1 % num2
  print(result) # Output: 5
  ```

- Floor Division (//): Divides the left operand by the right operand and returns the largest integer less than or equal to the result.

  ```py
  num1 = 25
  num2 = 10
  result = num1 // num2
  print(result) # Output: 2
  ```

- Exponentiation (\*\*): Raises the left operand to the power of the right operand.

  ```py
  num1 = 2
  num2 = 4
  result = num1 ** num2 # 2 * 2 * 2 * 2
  print(result) # Output: 16
  ```

### 2. Bitwise Operators :

we will learn about bitwise operators later.

### 3. Assignment Operators:

- **Assignment (=) :** Assigns the value on the right to the variable on the left.

  ```py
  number = 50
  name = "Shree Ram"
  print(name, number) # output: Shree Ram, 50
  ```

- **Addition Assignment (+=) :** Adds the value on the right to the variable on the left and assigns the result to the variable.

  ```py
  num1 = 30
  print(num1) # output: 30
  num1 += 20 # it's equal to => num1 = num1 + 20
  print(num1) # output: 50
  ```

- **Subtraction Assignment (-=) :** Subtracts the value on the right from the variable on the left and assigns the result to the variable.

  ```py
  num1 = 30
  print(num1) # output: 30
  num1 -= 20 # it's equal to => num1 = num1 - 20
  print(num1) # output: 10
  ```

- **Multiplication Assignment (\*=) :** Subtracts the value on the right from the variable on the left and assigns the result to the variable.

  ```py
  num1 = 30
  print(num1) # output: 30
  num1 *= 10 # it's equal to => num1 = num1 * 10
  print(num1) # output: 300
  ```

- **Division Assignment (/=) :** Divides the variable on the left by the value on the right and assigns the result to the variable.

  ```py
  num1 = 30
  print(num1) # output: 30
  num1 /= 10 # it's equal to => num1 = num1 / 10
  print(num1) # output: 3
  ```
