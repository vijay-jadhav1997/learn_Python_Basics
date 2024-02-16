# 💥 Data Type is Python :

- Numbers: int, float (including booleans)
- Strings and their methods
- Lists and their methods (including list comprehensions)
- Tuples
- Sets and their methods
- Dictionaries
- Type Casting

#### Python has various built-in data types:

    |Data Type   |   Examples                     |
    |:-----      |  :-----------                  |
    |Numeric     |  int, float, complex           |
    |String      |  str                           |
    |Sequence    |  list, tuple, range            |
    |Binary      |  bytes, bytearray, memoryview  |
    |Mapping     |  dict                          |
    |Boolean     |  bool                          |
    |Set         |  set, frozenset                |
    |None        |  NoneType                      |

### 1. Numbers:

There are three numeric types in Python:

- **_int_** : Int, or integer, is a whole number(without decimals), positive or negative,of unlimited length.
  e.g. 2, 4, 20, -10, 576, -89827735

  ```py
    # literal assignment:
    int_num = 25

    # constructor function:
    int_num2 = int(25)

    positive_int = 1
    negative_int = -3255522
    big_int = 35656222554887711
    # Another way to declare integer using 'int()' Fn.
    num = int(56)
    num2 = int('56')
    print(num2, type(num2))
  ```

- **_bool_** : Booleans represent the truth values False and True. The two objects representing the values
  False and True are the only Boolean objects. The Boolean type is a subtype of the integer type,
  and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the
  exception being that when converted to a string, the strings "False" or "True" are returned,
  respectively.
  (e.g. False and True, acting like 0 and 1)

  ```py
    # literal assignment:
    bool_val = True

    # constructor function:
    bool_val2 = bool(True)

    true_bool = True
    false_bool = False
  ```

- **_float_** : Float, or "floating point number" is a number, positive or negative,
  containing one or more decimals.
  e.g. 5.0, 1.6, -20.5, 3.14

  ```py
    # literal assignment:
    float_num = 25.5

    # constructor function:
    float_num2 = float(25.5)

    float_number = 7.0
    # Another way of declaring float is using float() function.
    float_number_via_function = float(7)
    float_negative = -35.59
  ```

- **_complex_** : e.g. 5+6j, 4-3j

  ```py
    # literal assignment:
  complex_num1 = 5 + 3j
  complex_num2 = 7 - 3j

  # constructor function:
  comp_num = complex(3+2j)

  print(comp_num.real) # op: 3.0
  print(comp_num.imag) # op: 2.0

  result = complex_num1 * complex_num2
  print(result) # Output: 44 + 6j
  ```

  **_Built-in Functions for Number :_**

  1. **_abs(number)_** : returns the absolute value of a given number. The result is always a non-negative value.

  ```py
    print(abs(-20)) # OP: 20
    print(abs(-5.5)) # OP: 5.5
    print(abs(101.9)) # OP: 101.9
  ```

  2. **round(number, n)\_** : round a floating-point number to a specified number of decimal places or to the nearest integer.

  ```py
    print(round(20.553, 2)) # OP: 20.55
    print(round(20.553)) # OP: 21
    print(round(5.6, 2)) # OP: 5.6
    print(round(1234, -2)) # OP: 1200
    print(round(1264, -2)) # OP: 1300
    print(round(1224, -3)) # OP: 1000
    print(round(1724, -3)) # OP: 2000
  ```

---

## Python Sequence Data Type:

- Sequence is a collection data type. It is an ordered collection of items. Items in the sequence have a positional index starting with 0. Ex. String Data Type, List Data Type & Tuple Data Type.
  > Python sequences are bounded and iterable - Whenever we say an iterable in Python, it means a sequence data type (for example, a list).

### 2. Strings :

- Strings in Python are sequences of characters and an object of str class.

```py
  # literal assignment:
  user = "Madhav"

  # constructor function:
  user2 = str("Mohan")

  # String with double quotes.
  name_1 = "Shree Ram"
  # String with single quotes.
  name_2 = 'Shree Ram'
  print(name1 == name2)

  #

  # \n means newline.
  multiline_string = 'First line.\nSecond line.'
  print(multiline_string)
```

- Python strings cannot be changed/modified — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

**_String indexing, Slicing and concatenation_** : Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

- The plus (+) sign is the string concatenation operator and the asterisk (\*) is the repetition operator in Python. For example −

```py
  chant = "Radhe_Radhe"
  print(chant)  # Output: Radhe_Radhe
  print(chant[0])  # Output: R
  print(chant[2:5])  # Output: dhe
  print(chant[2:])  # Output: dhe_Radhe
  print(chant[:5])  # Output: Radhe
  print(chant[:])  # Output: Radhe_Radhe

  print(chant[:-1])  # Output: Radhe_Radh
  print(chant[-6:-1])  # Output: _Radh
  print(chant[-11:-6])  # Output: Radhe

  print(chant * 2) # Output: Radhe_RadheRadhe_Radhe
  print(chant + "_Govind") # Output: Radhe_Radhe_Govind
  print("Jay_Shree_" + chant + "_Govind") # Output: Jay_Shree_Radhe_Radhe_Govind

```

**String Methods** :

1. **_str.lower()_**: Converts all characters in the string to lowercase.

```py
name = "ShreE KruShna"
print(name.lower()) # Output: 'shree krushna'
```

2. **_str.upper()_**: Converts all characters in the string to uppercase.

```py
name = "ShreE KruShna"
print(name.upper()) # Output: 'SHREE KRUSHNA'
```

3. **_str.capitalize()_**: Converts all characters in the string to uppercase.

```py
greeting = "namaStE to EVErYbodY!"
print(greeting.capitalize()) # Output: 'Namaste to everybody!'
```

4. **_str.title()_**: Converts all characters in the string to uppercase.

```py
greet = "jAy ShReE RaDHe KrUshNa"
print(greet.title()) # Output: 'Jay Shree Radhe Krushna'
```

5. **_str.strip()_**: Removes leading and trailing whitespace from the string.

```py
slogan = "  Jay Hind!  "
print(name.strip()) # Output: 'Jay Hind!'
```

6. **_str.replace('x','y')_**: Replaces a 'x' substring with 'y' substring.

```py
slogan = "Jay Jawan!"
print(slogan.replace('Jawan', 'Kisan' )) # Output: 'Jay Kisan!'
```

7. **_str.split('x','y')_**: Splits the string into a list of substrings based on a specified delimiter (default is whitespace).

```py
slogan = "Jay Jawan-Jay Kisan-Jay Kamgar"
print(slogan.split("-")) # Output: ['Jay Jawan','Jay Kisan', 'Jay Kamgar']
```

8. **_str.startswith(prefix)_**: Returns True if the string starts with the specified prefix, otherwise False.

```py
slogan = "Jay Jawan-Jay Kisan-Jay Kamgar"
print(slogan.startswith("Jay")) # Output: True
print(slogan.startswith("Shree")) # Output: False
```

9. **_str.endswith(prefix)_**: Returns True if the string ends with the specified suffix, otherwise False.

```py
greet = "Jay Shree Ram Krshna Hari"
print(greet.endswith("Hari")) # Output: True
print(greet.endswith("Jay")) # Output: False
```

10. **_str.find(substring)_**: Returns the lowest index in the string where the specified substring is found, otherwise -1.

```py
greet = "Jay Jay Ram Jay Shree Seeta Ram"
print(greet.find("Jay")) # Output: 0
print(greet.find("Ram")) # Output: 7
print(greet.find("Krushna")) # Output: -1
```

11. **_separator.join(iterable)_**: Concatenates elements of an iterable with the string as a separator. where-

- separator: ex. "-", ",", "\_", "/",or any symbol/punctuation mark.
- iterable can be list, tuple, set, etc. But Value stored must be strings.

```py
iterable = ["Sham", "Madhav", "Mohan","Mukund"]
result = "-".join(iterable)
print(result) # Output: "Sham-Madhav-Mohan-Mukund"

iter = ("Sham", "Madhav", "Mohan","Mukund")
result2 = "-".join(iter)
print(result2) # Output: "Sham-Madhav-Mohan-Mukund"
```

12. **_str.isalpha()_**: Returns True if all characters in the string are alphabetic.

```py
  name = "madhav"
  print(name.isalpha()) # Output: True
  print("Arun20".isalpha()) # Output: False
```

13. **_str.isdigit()_**: Returns True if all characters in the string are digits.

```py
  str_num = "625"
  print(str_num.isdigit()) # Output: True
  print("Feb2024".isdigit()) # Output: False
```

14. **_str.isalnum()_**: Returns True if all characters in the string are alphanumeric (letters or numbers).

```py
  user_name = "Sham625"
  print(user_name.isalnum()) # Output: True
  print("Feb".isalnum()) # Output: True
  print("Feb2024".isalnum()) # Output: True
  print("2024".isalnum()) # Output: True

  print("Feb-2024".isalnum()) # Output: False
  print("github.com".isalnum()) # Output: False
```

15. Some more string methods that returns True/False => str.isspace(), str.islower(), str.isupper(), str.startswith("prefix"), str.endswith("suffix")

```py
  print(" ".isspace()) # Output: True
  print("feb-2023".islower()) # Output: True
  print("MAY 2024".isupper()) # Output: True
  print("Har Har Mahadev".startswith("Har")) # Output: True
  print("Har Har Mahadev".endswith("Mahadev")) # Output: True

  print("R a m".isspace()) # Output: False
  print("Feb-2023".islower()) # Output: False
  print("May 2024".isupper()) # Output: False
  print("Har Har Mahadev".startswith("Maha")) # Output: False
  print("Har Har Mahadev".endswith("Har")) # Output: False
```

16. **_Some interesing str methods_** : str.center(width,"fillchar"), str.ljust(width, "fillchar"), str.rjust(width, "fillchar"),

### 3. List Data Type :

- Python list contains items separated by commas and enclosed within square brackets ([]).
- All the items in the list can be of different data type.
- A list in Python is an object of list class.
- lists are mutable.
- The values stored in a Python list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (\*) is the repetition operator.

```py
  my_list = ['jay hari', True, 30, "Mohan", 55.5]
  tiny_list = ['radhe govind', 101]
  print(my_list) # op: ['jay hari', True, 30, "Mohan", 55.5]
  print(my_list[0]) # op: jay hari
  print(my_list[1:3]) # op: [ True, 30]
  print(my_list[2:]) # op: [ 30, "Mohan", 55.5]
  print(my_list[:4]) # op: [ 'jay hari', True, 30, "Mohan"]

  print(tiny_list * 2) # op: [ 'radhe govind', 101, 'radhe govind', 101]
  print(my_list + tiny_list) # op: [ 'jay hari', True, 30, "Mohan", 55.5, 'radhe govind', 101]
```

### 4. Tuple Data Type :

- Python tuple is another sequence data type that is similar to a list.
- A Python tuple consists of a number of values separated by commas enclosed within parentheses (...).
- tuples cannot be updated (immutable). Tuples can be thought of as read-only lists.
- A tuple is an object of tuple class.
- Data items separated by comma without any enclosing symbols are treated as a tuple by default.

```py
  my_skills = ("html", "css", "javascript", "react", "tailwindcss", "git_github", "npm", "redux_toolkit")
  my_tuple = "Shree Mahadev", [1,2,3], False, 20.5

  print(my_tuple) # op: ("Shree Mahadev", [1,2,3], False, 20.5)
  print(my_skills) # op: ("html", "css", "javascript", "react", "tailwindcss", "git_github", "npm", "redux_toolkit")
```

### 5. Dictionary Data Type:

- Python dictionary consist of 'key:value' pairs.
- Where 'key' can be almost any Python data type, but are usually numbers or strings. 'Values', on the other hand, can be any arbitrary Python object (str, list, number, tuple, set, fn, dict, etc).
- The 'key:value' pairs are separated by comma and put inside curly brackets {}.
- Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).

```py
 my_dict = {}
 # here we assigning value using square braces ([])
 my_dict ['one'] = "Jay Shree Radhe"
 my_dict [2] = "Jay Shree Krushna"

 # declare tiny_dict
  tiny_dict = {'name': "Raghav", "code": 9876, 'position': "CEO"}

  # Access value using square braces ([]):
  print(my_dict ['one']) # op: Jay Shree Radhe
  print(my_dict [2]) # op: Jay Shree Krushna
  print(my_dict ['position']) # op: CEO
  print(tiny_dict) # op: {'name': "Raghav", "code": 9876, 'position': "CEO"}
```

- Python's **dictionary is not a sequence**.
- It is a **collection of items** but each item (key:value pair) is not identified by positional index as in string, list or tuple. Hence, **slicing operation cannot be done on a dictionary**.
- **_Dictionary is a mutable object_**, so it is possible to perform add, modify or delete actions with corresponding functionality defined in dict class.

### 5. Dictionary Data Type:

- Set is a Python implementation of set as defined in Mathematics.
- A set in Python is a collection, but is not an indexed or ordered collection as string, list or tuple.
- An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

```py
  my_set = {"Jay Hari", 21, True, 3.14}
  print(my_set) # op: {'Jay Hari', 3.14, 21, True}
  # Note that items in the set collection may not follow the same order in which they are entered. The position of items is optimized by Python to perform operations over set as defined in mathematics.
```

- A set can store only immutable objects such as number (int, float, complex or bool), string or tuple.
- If you try to put a list or a dictionary in the set collection, Python raises a TypeError.

> > **Hashing** is a mechanism in computer science which enables quicker searching of objects in computer's memory. Only **_immutable objects_** are **_hashable_**.

- Even if a set doesn't allow mutable items, the set itself is mutable. Hence, add/delete/update operations are permitted on a set object, using the methods in built-in set class.

---

## Python Type Casting:

From a programming point of view, a type casting refers to converting an object of one type into another. Here, we shall learn about type casting in Python Programming.

> > Python Type Casting is a process in which we convert a literal of one data type to another data type. Python supports two types of casting − implicit and explicit.

### 1. Python Implicit Casting:

When any language compiler/interpreter automatically converts object of one type into other, it is called automatic or implicit casting.

- Python is a strongly typed language. It doesn't allow automatic type conversion between unrelated data types. Ex, a string cannot be converted to any number type.
- However, an integer can be cast into a float.
- Other languages such as JavaScript is a weakly typed language, where an integer is coerced into a string for concatenation.

1. **Implicit int to float casting** :
   Note that memory requirement of each data type is different. For example, an integer object in Python occupies 4 bytes of memory, while a float object needs 8 bytes because of its fractional part. Hence, Python interpreter doesn't automatically convert a float to int, because it will result in loss of data. On the other hand, int can be easily converted into float by setting its fractional part to 0.

- Implicit _int_ to _float_ casting takes place when any arithmetic operation on _int_ and _float_ operands is done.

```py
  price = 25
  charges = 10.5
  print(price + charges) # op: 35.5
```

- In implicit type casting, a Python object with lesser byte size is upgraded to match the bigger byte size of other object in the operation.
- For example, a Boolean object is first upgraded to int and then to float, before the addition with a floating point object.

```py
bool_one = True # As we know => True is equal to 1.
bool_zero = False  # and False is equal to 0.
float_one = 1.0
# Adding bool value to float value:
sum = bool_one + float_one
print(sum)  # output: 2.0
print(True + False)  # output: 1
print(20.5 + False)  # output: 20.5
print(1 + True)  # output: 2

```

### 2. Python Explicit Casting:

Although automatic or implicit casting is limited to int to float conversion, you can use Python's built-in functions int(), float() and str() to perform the explicit conversions such as string to integer.

1. **Python int() Function**:

   - Python's built-in int() function converts an integer literal to an integer object, a float to integer, and a string to integer if the string itself has a valid integer literal representation.

```py
# Using int() with an int object as argument is equivalent to declaring an int object directly.
ten = int(10)
tenth = 10
# some investigation
# boolean to integer
print(int(True)) # op: 1
print(int(False)) # op: 0

# float to integer
print(int(5.5)) # op: 5
print(int(1.0)) # op: 1

# String to integer
print(int("5.5")) # Raises ValueError: invalid literal for int().
print(float("5.5")) # op: 5.5
print(int("1")) # op: 1
print(int("50")) # op: 50

# Binary String to Integer: (The string should be made up of 1 and 0 only, and the base should be 2.)
print(int("1011",2)) # op: 11
print(int("10111",2)) # op: 23
print(int("0110", 2)) # op: 6

# Octal String to Integer: (The string should only contain 0 to 7 digits, and the base should be 8.)
print(int("20",8)) # op: 16
print(int("40",8)) # op: 32
print(int("5", 8)) # op: 5
print(int("6", 8)) # op: 6
print(int("7", 8)) # op: 7
print(int("10", 8)) # op: 8

# Hexa-Decimal String to Integer : (The string should contain only the Hexadecimal symbols i.e., 0-9 and A, B, C, D, E or F. Base should be 16.)
print(int("2A9", 8)) # op: 681
print(int("10", 8)) # op: 8
```

2. **Python float() Function**:

   - The float() is a built-in function in Python. It returns a float object if the argument is a float literal, integer or a string with valid floating point representation.

```py
  # both are same
  number = 20.0
  num = float(20)
  print(number, num) # output: 20.0, 20.0
  print(float(1)) # op: 1.0
  print(float(1.2)) # op: 1.2
  print(float("2.2")) # op: 2.2

  # string to float : if the string contains a valid floating point number, otherwise ValueError is raised.
  print(float("25.5")) # op: 25.5
  print(float("12,25.5")) # op: ValueError: could not convert string to float: 12,25.5

  # string to float conversion, the sceientific notation of floating point.
  print(float("1.00E4")) # OP: 10000.0
  print(float("200.00E-2")) # OP: 2.0
  print(float("525.00E-5")) # OP: 0.00525
```

3. **Python str() Function**:
   The str() function returns the string representation of any Python object.
   - The str() function has three parameters. First **_required parameter_** (or argument) is the object whose string representation we want. Other two operators, encoding and errors, are optional.

```py
  # str() fn convert any py data type object to str object
  # bool to str
  print(str(True)) # op: 'True'
  print(str(False)) # op: 'False'
  # int to str
  print(str(200)) # op: '200'
  print(str(5+5)) # op: '10'
  # float to str
  print(str(5.5)) # op: '5.5'
  print(str(2/5)) # op: '0.4'
  # Floating points in scientific notations using E or e and with positive or negative power are converted to string with str() function.
  print(str(2.5E3)) # op: '2500.0'
  print(str(225E-4)) # op: '0.0225'

  # str to str
  print(str("Rs:200.00₹")) # op: 'Rs:200.00₹'
```

4. **Conversion of Sequence Types**:
   List, Tuple and String are Python's sequence types. They are ordered or indexed collection of items.
   - A **_string_** and **_tuple_** can be converted into a **_list object_** by using the list() function.
   - Similarly, the **_tuple() function_** converts a **_string_** or **_list_** to a **_tuple object_**.

```py
  mylist = [1,2,3,4,5]
  mytuple = ("Jay", "Shree", "Om")
  string = "JayHari"

  # to list from str & tuple -
  print(list(string)) # op: ['J', 'a', 'y', 'H', 'a', 'r', 'i']
  print(list(mytuple)) # op: ["Jay", "Shree", "Om"]

  # to tuple from str & list -
  print(tuple(string)) # op:('J', 'a', 'y', 'H', 'a', 'r', 'i')
  print(tuple(mylist)) # op: (1,2,3,4,5)

  # just practice str.join() fn
  print("".join(string)) # op: JayHari
  print("_".join(string)) # op: J_a_y_H_a_r_i
  print("".join(list(string))) # op: JayHari
  print("_".join(list(string))) # op: J_a_y_H_a_r_i
```
