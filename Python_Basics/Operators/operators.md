# Operators

- Arithmetic Operators (+, -, \*, /, //, %, \*\*)
- Bitwise Operators (&, |, ^, >>, <<, ~)
- Assignment Operators (=, +=, -=, /=, //= etc.)
- Comparison Operator (==, !=, >, <, >=, <=)
- Logical Operators (and, or, not)
- Identity Operators (is, is not)
- Membership Operators (in, not in)

---

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

---

### 2. Bitwise Operators :

we will learn about bitwise operators later.

---

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

- **Modulus Assignment (%=) :** Computes the modulus of the variable on the left by the value on the right and assigns the result to the variable.

  ```py
  num1 = 30
  print(num1) # output: 30
  num1 %= 8 # it's equal to => num1 = num1 % 8
  print(num1) # output: 6
  ```

- **Floor Division Assignment (//=) :**
- **Exponentiation Assignment (\*\*=) :**

---

### 4. Comparison Operator:

These comparison operators are commonly used in conditional statements (if, elif, else) and other contexts where we need to check the relationship between two values.

- **Equal to (==) :** Returns True if the values on both sides are equal.
  ```py
    print(20 == 20) # Output: True
    print(20 == 10) # Output: False
  ```
- **Not Equal to (!=):** Returns True if the values on both sides are not equal.

  ```py
    print(20 != 10) # Output: True
    print(20 != 20) # Output: False
  ```

- **Greater Than (>):** Returns True if the value on the left is greater than the value on the right.

  ```py
   print(20 > 10) # Output: True
   print(20 > 20) # Output: False
   print(20 > 30) # Output: False
  ```

- **Less Than (<):** Returns True if the value on the left is less than the value on the right.

  ```py
    print(20 < 30) # Output: True
    print(20 < 20) # Output: False
    print(20 < 10) # Output: False
  ```

- **Greater Than or Equal to (>=):** Returns True if the value on the left is greater than or equal to the value on the right.

  ```py
    print(20 >= 10) # Output: True
    print(20 >= 20) # Output: True
    print(20 >= 30) # Output: False
  ```

- **Less Than or Equal to (<=):** Returns True if the value on the left is less than or equal to the value on the right.
  ```py
    print(20 <= 30) # Output: True
    print(20 <= 20) # Output: True
    print(20 <= 10) # Output: False
  ```

### 5. Logical Operators:

- **'and' Operator:** Returns True if both operands are true; otherwise, it returns False.
  - True and True => True
  - True and False => False
  - False and True => False
  - False and False => False
  ```py
    print(True and True) # outpu: True
    print(False and True) # outpu: False
    print(True and False) # outpu: False
    print(False and False) # outpu: False
  ```
- **'or' Operator:** Returns True if at least one of the operands is true; it returns False if both operands are false.

  - True and True => True
  - True and False => True
  - False and True => True
  - False and False => False

  ```py
    print(True or True) # outpu: True
    print(False or True) # outpu: True
    print(True or False) # outpu: True
    print(False or False) # outpu: False
  ```

  ```

  ```

- **'not' Operator:** Returns the opposite of the operand's boolean value. If the operand is True, not returns False; if the operand is False, not returns True.
  - True and True => True
  - True and False => True
  - False and True => True
  - False and False => False
  ```py
    print(not True) # outpu: False
    print(not False) # outpu: True
  ```

### 6. Identity Operators:

Identity operators in Python are used to compare the memory addresses of two objects. They check whether two variables reference the same object in memory.

- **'is' Operator:** Returns True if both operands refer to the same object in memory; otherwise, it returns False.

  ```py
  list1 = ["Jay", "Hari", "Radhe", "Gopal"]
  list2 = ["Jay", "Hari", "Radhe", "Gopal"]
  list3 = list1

  print(list1 is list2) # Output: False
  print(list1 is list3) # Output: True

  if list1 is list3:
    print("Both variables reference the same list.")
  ```

- **'is not' Operator:** Returns True if both operands do not refer to the same object in memory; it returns False if they do.

  ```py
  list1 = ["Jay", "Hari", "Radhe", "Gopal"]
  list2 = ["Jay", "Hari", "Radhe", "Gopal"]
  list3 = list1

  print(list1 is not list2) # Output: True
  print(list1 is not list3) # Output: False
  print(list1 is list3) # Output: True

  if list1 is not list2:
    print("Both variables do not reference the same list, even though they contain same values/elements.")
  ```

### 7. Membership Operators :

Membership operators in Python are used to test whether a value is a member of a sequence or collection. These operators check for the presence or absence of a value within a container.

- **'in' Operator:** Returns True if a specified value is found in the sequence (list, tuple, string, set, or dictionary); otherwise, it returns False.

```py
  numbers = [1,2,3,4,5,6,7,8,9,10]
  if 8 in numbers:
    print(f"'8' presents in {numbers}")

  registered_usernames = ["user1", "user2", "user3"]

  username = input("Enter your username: ")

  if username in registered_usernames:
    print("Access granted!")
  else:
    print("Invalid username. Access denied.")
```

- **'not in' Operator:** Returns True if a specified value is not found in the sequence; it returns False if the value is present.

```py
  numbers = [1,2,3,4,5,6,7,8,9,10]
  if 15 not in numbers:
    print(f"'15' doesn't present in {numbers}")

  blocked_emails = ["spam@example.com", "phishing@example.com", "junk@example.com"]

  email = input("Enter your email address: ")

  if email not in blocked_emails:
    print("Email accepted!")
  else:
    print("Sorry, this email is blocked.")
```
