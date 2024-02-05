# 👨🏻‍💻 I'm Learning Python🐍 and👉🏻you!....

### 🔆 Table of Contents 📝

1. Getting Started
   - What is Python
   - Python Syntax
   - Variables
2. Operators
   - Arithmetic Operators (+, -, \_, /, //, %, \*\*)
   - Bitwise Operators (&, |, ^, >>, <<, ~)
   - Assignment Operators (=, +=, -=, /=, //= etc.)
   - Comparison Operator (==, !=, >, <, >=, <=)
   - Logical Operators (and, or, not)
   - Identity Operators (is, is not)
   - Membership Operators (in, not in)
3. Data Types
   - Numbers (including booleans)
   - Strings and their methods
   - Lists and their methods (including list comprehensions)
   - Tuples
   - Sets and their methods
   - Dictionaries
   - Type Casting
4. Control Flow
   - The if statement
   - The for statement (and range() function)
   - The while statement
   - The try statements
   - The break statement
   - The continue statement
5. Functions
   - Function Definition (def and return statements)
   - Scopes of Variables Inside Functions (global and nonlocal statements)
   - Default Argument Values
   - Keyword Arguments
   - Arbitrary Argument Lists
   - Unpacking Argument Lists (\_ and \*\* statements)
   - Lambda Expressions (lambda statement)
   - Documentation Strings
   - Function Annotations
   - Function Decorators
6. Classes
   - Class Definition (class statement)
   - Class Objects
   - Instance Objects
   - Method Objects
   - Class and Instance Variables
   - Inheritance
   - Multiple Inheritance
7. Modules
   - Modules (import statement)
   - Packages
8. Errors and Exceptions
   - Handling Exceptions (try statement)
   - Raising Exceptions (raise statement)
9. Files
   - Reading and Writing (with statement)
   - Methods of File Objects
10. Additions

    - The pass statement
    - Generators (yield statement)

11. Brief Tour of the Standard Libraries

    - Serialization (json library)
    - File Wildcards (glob library)
    - String Pattern Matching (re library)
    - Mathematics (math, random, statistics libraries)
    - Dates and Times (datetime library)
    - Data Compression (zlib library)

12. User input
    - Terminal input (input statement)

### Python Syntax :

1. **Python Identifiers** : In Python, an identifier is a name used to identify a **_variable, function, class, module, or any other object_**. Identifiers/variables are used to uniquely name entities in a program.
2. **Rules for Naming Identifiers** :
   - Identifiers (or variables) can only consist of alphanumeric characters (a-z, A-Z, 0-9) and underscores (\_).
   - They cannot start with a digit(0-9).
   - Certain words, known as reserved words or keywords (e.g., if, else, while, class), cannot be used as identifiers.
   - Python does not allow punctuation characters such as @, $, and % within identifiers.
3. **Naming conventions** for Python identifiers −

   - **_Python Class names_** start with an uppercase letter. **_All other identifiers_** start with a lowercase letter.

   ```py
      variable_name = 42   # see variable naming (snake_case)
      function_name = "hello" # see function naming (snake_case)
      class MyClass:  # see class naming (CamelCase)
         pass
   ```

   - Starting an identifier with a _single leading underscore_ indicates that the identifier is _private identifier_.
   - Starting an identifier with _two leading underscores_ indicates a _strongly private identifier_.
   - If the _identifier also ends with two trailing underscores_, the identifier is a _language-defined special name_.

4. **Python Lines & Indentation** :

   - Python programming provides no braces to indicate blocks code for class and function definitions or flow control Blocks of code are denoted by line indentation, which is rigidly enforced.
   - Python Multi-Line Statements : Statements in typically end with a new line. Python does, however, allow the use of line continuation character (\) to denote that the line should continue.

   ```py
      total_price = item_one + \
                     item_two + \
                     item_three
   ```

5. Quotation in Python : Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
6. Comments in Python: A hash sign (#) that is not inside a string literal begins a comment.

   ```py
      name = "Shree Ram" # This is again comment
      # This is a comment.
      '''
      This is a multiline
      comment.
      '''
   ```

7. Multiple Statements on a Single Line: The semicolon ( ; ) allows multiple statements on the single line given that neither statement starts a new code block.

   ```py
      import random; country = 'India'; random_char = random.choice(country)
      print(random_char)
   ```

8. Multiple Statement Groups as Suites: A group of individual statements, which make a single code block are called suites in Python. Compound or complex statements, such as if, while, def, and class require a header line and a suite.
   - Header lines begin the statement (with the keyword) and terminate with a colon ( : ) and are followed by one or more lines which make up the suite. For example −
   ```py
      if expression :
         suite
      elif expression :
         suite
      else :
         suite
   ```
