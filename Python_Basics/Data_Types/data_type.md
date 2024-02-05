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
   true_bool = True
    false_bool = False
  ```
- **_float_** : Float, or "floating point number" is a number, positive or negative,
  containing one or more decimals.
  e.g. 5.0, 1.6, -20.5, 3.14
  ```py
  float_number = 7.0
  # Another way of declaring float is using float() function.
  float_number_via_function = float(7)
  float_negative = -35.59
  ```
- **_complex_** : e.g. 5+6j, 4-3j
  ```py
  complex_num1 = 5 + 3j
  complex_num2 = 7 - 3j
  result = complex_num1 * complex_num2
  print(result) # Output: 44 + 6j
  ```

### 2. Strings :

Strings in Python are sequences of characters and are treated as objects.

```py
  # String with double quotes.
  name_1 = "Shree Ram"
  # String with single quotes.
  name_2 = 'Shree Ram'
  print(name1 == name2)

  # \n means newline.
  multiline_string = 'First line.\nSecond line.'
  print(multiline_string)
```

##### str Methods:

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

6. **_str.split('x','y')_**: Splits the string into a list of substrings based on a specified delimiter (default is whitespace).

```py
slogan = "Jay Jawan-Jay Kisan-Jay Kamgar"
print(slogan.split("-")) # Output: ['Jay Jawan','Jay Kisan', 'Jay Kamgar']
```
