######## list in Python ############

#? Definition: A list in Python is a versatile and ordered collection of elements. It allows you to store and manipulate a sequence of items. Lists are mutable, meaning you can change their contents by adding, removing, or modifying elements.

#* Syntax: The basic syntax for creating a list in Python involves enclosing a sequence of elements within square brackets []:

#? Characteristics of Lists:
#* 1) Order: Lists maintain the order of elements, meaning the position of each element is preserved.
#* 2) Mutability: Lists are mutable, allowing you to modify their elements after creation.
#* 3) Heterogeneity: Lists can contain elements of different data types (e.g., integers, strings, floats).
#* 4) Indexing: Elements in a list are accessed using zero-based indexing. For example, my_list[0] accesses the first element.
#* 5) Dynamic Size: Lists in Python can dynamically grow or shrink in size as elements are added (using .append(element_value) method) or removed(using .remove(element_value) method).

students = ['JaY Shree Ram', 'Jay Shree Krushna', 'Jay Shree Vitthal', 'Jay Hari']

for i in students:
  print(i.replace(" ", "_").lower(), end=" ")

for i in range(len(students)):
  print(i ,students[i].replace(" ", "_").lower(), end=" ")


#! There are several ways to create a list in Python:
#? 1) Using Square Brackets: ex. my_list = [1, True, 2, -3, "hello", 5.0]

#? 2) Using the list() Constructor:
#        You can use the list() constructor to create a list. It can take any iterable as an argument and convert it to a list.
#* ex. another_list = list(range(5))

#? 3) List Comprehension:
#      List comprehensions provide a concise way to create lists. They allow you to specify the elements of a list using a compact expression.
#*  Ex. squares = [x**2 for x in range(5)]

#? 4) Using append() and extend() Methods: 
#*  You can start with an empty list and use the append() or extend() methods to add elements.
#*   empty_list = []
#*   empty_list.append(1)
#*   empty_list.extend([2, 3, 4])

#? 5) Using split() Method (for Strings):
#* If you have a string with values separated by a delimiter, you can use the split() method to create a list.
#*    string_values = "apple,banana,orange"
#*    fruit_list = string_values.split(',')

#? 6) Nested Lists: Lists can also contain other lists, creating nested structures.
#  Ex. nested_list = [[1, 2, 3], ['a', 'b', 'c']]



#* Creating a list
fruits = ["apple", "banana", "orange"]

#* Accessing elements
first_fruit = fruits[0]
print("First fruit:", first_fruit)

#* Modifying elements
fruits[1] = "grape"

#? Adding elements
fruits.append("kiwi")

#? Removing elements
fruits.remove("orange")

#* Displaying the modified list
print("Updated fruits list:", fruits)
