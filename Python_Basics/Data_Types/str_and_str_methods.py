"""Strings """
#?  Besides numbers, Python can also manipulate strings, which can be
#?  expressed in several ways. They can be enclosed in single quotes ('...')
#?  or double quotes ("...") with the same result.

"""
Quotations in Python
Python accepts single (''), double ("") and triple ('' or "") quotes to denote string literals, as long as the same type of quote starts and ends the string.
The triple quotes are used to span the string across multiple lines.
"""
def quotation_in_python():
    word = 'word'
    print (word)

    sentence = "This is a sentence."
    print (sentence)

    paragraph = """This is a paragraph. It is
    made up of multiple lines and sentences."""
    print (paragraph)



def string_type():
  """String type"""

  # String with double quotes.
  name_1 = "John"
  # String with single quotes.
  name_2 = 'John'
  # Strings created with different kind of quotes are treated the same.
  if name_1 == name_2:
    print(f"name_1 '{name_1}' is equal to name_2 '{name_2}'")
  if name_1 is name_2:
    print(f"name_1 '{name_1}' has a same reference in memory location as of name_2 '{name_2}'")
     
  print(name_1 == name_2)
  print(isinstance(name_1, str))
  print(isinstance(name_2, str))

  # \ symbol can be used to escape quotes.
  # use \' to escape the single quote or use double quotes instead.
  single_quote_string = 'doesn\'t'
  double_quote_string = "doesn't"

  print(single_quote_string == double_quote_string)

  # \n means newline.
  multiline_string = 'First line.\nSecond line.'
  # Without print(), \n is included in the output.
  # But with print(), \n produces a new line.
  print(multiline_string == 'First line.\nSecond line.')

  # Strings can be indexed, with the first character having index 0.
  # There is no separate character type; a character is simply a string
  # of size one. Note that since -0 is the same as 0, negative indices
  # start from -1.
  word = 'Python'
  print(word[0])  # Output: 'P' First character.
  print(word[5])  # Output: 'n' Fifth character.
  print(word[-1]) # Output: 'n' Last character.
  print(word[-2]) # Output: 'o' Second-last character.
  print(word[-6]) # Output: 'P' Sixth from the end or zeroth from the beginning.

  print(isinstance(word[0], str))

  #* In addition to indexing, slicing is also supported. While indexing is
  #* used to obtain individual characters, slicing allows you to obtain substring:
  print(word[0:2]) # Output: 'Py' Characters from position 0 (included) to 2 (excluded).
  print(word[2:5]) # Output: 'tho' Characters from position 2 (included) to 5 (excluded).

  #? Note how the start is always included, and the end always excluded.
  # This makes sure that s[:i] + s[i:] is always equal to s:
  print(word[:2] + word[2:]) # Output: 'Python' => String concatanation
  print(word[:4] + word[4:]) # Output: 'Python' => String concatanation

  #* Slice indices have useful defaults; an omitted first index defaults to
  #* zero, an omitted second index defaults to the size of the string being sliced.
  print(word[:2]) # 'Py' Character from the beginning to position 2 (excluded).
  print(word[4:]) # 'on' - Characters from position 4 (included) to the end.
  print(word[-2:]) # 'on' Characters from the second-last (included) to the end.

  # One way to remember how slices work is to think of the indices as
  # pointing between characters, with the left edge of the first character
  # numbered 0. Then the right edge of the last character of a string of n
  # characters has index n, for example:
  #
  # +---+---+---+---+---+---+
  #  | P | y | t | h | o | n |
  #  +---+---+---+---+---+---+
  #  0   1   2   3   4   5   6
  # -6  -5  -4  -3  -2  -1

  # Attempting to use an index that is too large will result in an error.
  not_existing_character = word[42]
  print( not_existing_character) # Output: Index Error: string index out of range

  # However, out of range slice indexes are handled gracefully when used
  # for slicing:
  print(word[:42])  # Output: 'Python'
  print(word[4:42]) # Output: 'on'
  print(word[42:])  # Output: ''

  #! Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
  word[0] = 'J'
  print(word[0]) #* Output=> TypeError: 'str' object does not support item assignment

  #* If you need a different string, you should create a new one:
  print('J' + word[1:])  # Output: 'Jython'
  print(word[:2] + 'py') # Output: 'Pypy'

  #? The built-in function len() returns the length of a string:
  characters = 'supercalifragilisticexpialidocious'
  print(len(characters)) # Output: 34

  # String literals can span multiple lines. One way is using triple-quotes: """..."""
  # or '''...'''. End of lines are automatically included in the string, but it’s possible
  # to prevent this by adding a \ at the end of the line. The following example:
  multi_line_string = '''\
      First line
      Second line
  '''

  print(multi_line_string)


def string_operators():
  """Basic operations

  Strings can be concatenated (glued together) with the + operator,
  and repeated with *: 3 times 'un', followed by 'ium'
  """

  print(3 * 'Har ' + 'Mahadev')  # Output: Har Har Har Mahadev

  # 'Py' 'thon'
  word = 'Py' 'thon'
  print(word) # Output: 'Python'

  # This feature is particularly useful when you want to break long strings:
  text = (
      'Put several strings within parentheses '
      'to have them joined together.'
  )
  print(text) # Output: Put several strings within parentheses to have them joined together.

  # If you want to concatenate variables or a variable and a literal, use +:
  prefix = 'Py'
  print(prefix + 'thon') # Output: 'Python'


def string_methods():
  """String methods"""

  greeting_string = "Jay Jay Shree Radhe"

  # The strip() method removes any whitespace from the beginning or the end.
  string_with_whitespaces = " Jay Maa Bharati! "
  print(string_with_whitespaces.strip()) # Output: Jay Maa Bharati!

  # The len() method returns the length of a string.
  print(len(greeting_string)) # Output: 19

  # The lower() method returns the string in lower case.
  print(greeting_string.lower()) == 'jay jay rhree radhe'

  # The upper() method returns the string in upper case.
  print(greeting_string.upper()) == 'JAY JAY SHREE RADHE'

  # The replace() method replaces a string with another string.
  print(greeting_string.replace('Radhe', 'Ram')) # Output: Jay Jay Shree Ram

  # The split() method splits the string into substrings if it finds instances of the separator and return new list.
  print(greeting_string.split(" ")) # Output: ["Jay", "Jay", "Shree", "Radhe"]

  # Converts the first character to upper case
  print('upper case letter at the beginning'.capitalize()) #Output: 'Upper case letter at the beginning'

  # Returns the number of times a specified value occurs in a string.
  print('count the \'t\' character in the sentense'.count('t')) # Output: 6

  # Searches the string for a specified value and returns the position of where it was found.
  print("Jay Jay Ram Krushna Hari Vitthal Keshava".find('Vitthal')) # Output: 25

  # Converts the first character of each word to upper case
  print('Shree ram jay ram jay jay ram'.title()) # Output: Shree Ram Jay Ram Jay Jay Ram

  # Joins the elements of an iterable to the end of the string.
  my_tuple = ('Mohan', 'Sham', 'Madhav')
  print(', '.join)(my_tuple) # Output: 'Mohan, Sham, Madhav'
  my_list = ['Mohan', 'Sham', 'Madhav']
  print('_'.join)(my_list) # Output: 'Mohan_Sham_Madhav'

  # Returns True if all characters in the string are upper case.
  print('NARAYAN'.isupper()) # Output: True
  print(not 'Govind'.isupper()) # Output: True

  # Check if all the characters in the text are letters.
  print('JayShreeGanesh'.isalpha()) # Output: True
  print(not 'Jay Shree Ganesh 23'.isalpha()) # Output: True

  # Returns True if all characters in the string are decimals.
  print('1234'.isdigit(), '1234'.isdecimal()) # output: True
  print(not 'Abc21453'.isdigit(), not 'Abc21453'.isdecimal()) # output: True 
  print('Abc21453'.isdigit(), 'Abc21453'.isdecimal()) # output: False (contain 'Abc')
  print('21.453'.isdigit(), '21.453'.isdecimal()) # output: False  (contains a dot '.')


def string_formatting():
  """String formatting.

  Often you’ll want more control over the formatting of your output than simply printing
  space-separated values. There are several ways to format output
  """

  # To use formatted string literals, begin a string with f or F before the opening quotation
  # mark or triple quotation mark. Inside this string, you can write a Python expression
  # between { and } characters that can refer to variables or literal values.
  year = 2018
  event = 'conference'

  print(f'Results of the {year} {event}') # Output: 'Results of the 2018 conference'.

  # The str.format() method of strings requires more manual effort. You’ll still use { and } to
  # mark where a variable will be substituted and can provide detailed formatting directives,
  # but you’ll also need to provide the information to be formatted.
  yes_votes = 42_572_654  # equivalent of 42572654
  no_votes = 43_132_495   # equivalent of 43132495
  percentage = yes_votes / (yes_votes + no_votes)

  print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)) # Output: ' 42572654 YES votes  49.67%'

  # When you don’t need fancy output but just want a quick display of some variables for debugging
  # purposes, you can convert any value to a string with the repr() or str() functions. The str()
  # function is meant to return representations of values which are fairly human-readable, while
  # repr() is meant to generate representations which can be read by the interpreter (or will
  # force a SyntaxError if there is no equivalent syntax). For objects which don’t have a
  # particular representation for human consumption, str() will return the same value as repr().
  # Many values, such as numbers or structures like lists and dictionaries, have the same
  # representation using either function. Strings, in particular, have two distinct
  # representations.

  greeting = 'Jay Shree Radhe!'
  first_num = 10 * 3.25
  second_num = 200 * 200

  print(str(greeting)) # Output: 'Jay Shree Radhe!'
  print(repr(greeting)) # Output: "'Jay Shree Radhe!'"
  print(str(1/7)) # Output: '0.14285714285714285'

  # The argument to repr() may be any Python object:
  print(repr((first_num), second_num, ('spam', 'eggs'))) # Output: "(32.5, 40000, ('spam', 'eggs'))"

  #? Formatted String Literals:
  #* Formatted string literals (also called f-strings for short) let you include the value of
  #* Python expressions inside a string by prefixing the string with f or F and writing
  #* expressions as {expression}.

  #* An optional format specifier can follow the expression. This allows greater control over how
  #* the value is formatted. The following example rounds pi to three places after the decimal.
  pi_value = 3.14159
  print(f'The value of pi is {pi_value:.3f}.') # Output: 'The value of pi is 3.142.'
  print(f'The value of pi is {pi_value:.2f}.') # Output: 'The value of pi is 3.14.'

  # Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
  # This is useful for making columns line up:
  table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
  table_string = ''
  for name, phone in table_data.items():
    ustable_string += f'{name:7}==>{phone:7d}'

  print(table_string) # ('Sjoerd ==>   4127' 'Jack   ==>   4098' 'Dcab   ==>   7678')

  # The String format() Method

  # Basic usage of the str.format() method looks like this:
  print('We are {} who say "{}!"'.format('knights', 'Ni')) # 'We are knights who say "Ni!"'

  # The brackets and characters within them (called format fields) are replaced with the objects
  # passed into the str.format() method. A number in the brackets can be used to refer to the
  # position of the object passed into the str.format() method
  print('{0} and {1}'.format('spam', 'eggs')) # 'spam and eggs'
  print('{1} and {0}'.format('spam', 'eggs')) # 'eggs and spam'

  # If keyword arguments are used in the str.format() method, their values are referred to by
  # using the name of the argument.
  formatted_string = 'This {food} is {adjective}.'.format(
      food='spam',
      adjective='absolutely horrible'
  )

  print(formatted_string) # 'This spam is absolutely horrible.'

  # Positional and keyword arguments can be arbitrarily combined
  formatted_string = 'The story of {0}, {1}, and {other}.'.format(
      'Bill',
      'Manfred',
      other='Georg'
  )

  print(formatted_string) # 'The story of Bill, Manfred, and Georg.'

  # If you have a really long format string that you don’t want to split up, it would be nice if
  # you could reference the variables to be formatted by name instead of by position. This can be
  # done by simply passing the dict and using square brackets '[]' to access the keys

  table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
  formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

  print(formatted_string) # 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

  # This could also be done by passing the table as keyword arguments with the ‘**’ notation.
  formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
