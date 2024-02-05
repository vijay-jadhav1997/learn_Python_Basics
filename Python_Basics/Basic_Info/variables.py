"""
? Python is completely object oriented, and not "statically typed".
? You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

? Unlike other programming languages, Python has no command for declaring a variable.
? A variable is created the moment you first assign a value to it.

? A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

? Rules for Python variables:
? - A variable name must start with a letter or the underscore character.
? - A variable name cannot start with a numberor any special character like $, (, * % etc.
? - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
? - Variable names are case-sensitive (age, Age and AGE are three different variables).
? Python reserved keywords cannot be used naming the variable.
>> If the name of variable contains multiple words, we should use following naming pattern −
? snake_case: Use single underscore (_) character to separate words. Ex. km_per_hour, price_per_litre....
"""
#! In python 'variable' never be any data type, but 'values' are of different data types.

def py_variables():
  int_var = 55 #* Here "int_var" is not of any data type, but 55 which is value of "int_var" is 'int' data type
  str_var = "Jay Shree Ram" #* Here "str_var" is not of any data type, but "Jay Shree Ram" which is value of "str_var" is 'str' data type
  #* Same goes for any variable ....
  float_var = 4.50
  is_valid = True
  is_default_user = False
  students_list = ["Raghav", "Mohan", "Gopal", "Sham", "Madhav", "Rakesh", "Kanha", "Kartik"]
  movies_tuple = ("Border", "URI", "Vande Mataram", "Maa Barati")

  user_dict = {
    "id": 0,
    "user_name": "sham051997",
    "password": "sham@7991",
    "name": "Sham Trivedi",
    "age": 27,
    "is_educated" : True,
    "skills": ["web dev", "React", "Nodejs", "TailwindCSS", "git"]
  }

#! 3) Deleting Python Variables
def delete_var():
  #? Deleting Python Variables :
  # You can delete the reference to a number object by using the del statement.
  count = 15
  print(count)

  del count
  try:
    print(count)
  except NameError:
    print(NameError)


#? 4) Getting Type of a Variable:
def get_type_of_variable():
  name = "Jay Shree Krushna" # Creates a str variable
  int_num = 25 # Creates an int variable
  float_num = 25.25 # Creates a float variable
  # Creates a list variable
  user_list = ["Ganesh", "Mahesh", "Madhav", "Mukund", "Gopal", "Sham"]
  # Creates a dictionary(dict) variable
  employee_dict = {
    "name": "Raghav",
    "age": 32,
    "is_educated": True,
    "skills": ["web dev", "soft skills", "communication skill"]
  }
  score_tuple = (20, 15, 5, 18, 25, 22) # Creates a tuple variable

  print(type(name))
  print(type(int_num))
  print(type(float_num))
  print(type(user_list))
  print(type(employee_dict))
  print(type(employee_dict["is_educated"]))
  print(type(score_tuple))

#? 5) Casting Python Variables:
def cast_py_variables():
  str_num = str(20)  # str_num will be '20'
  number = int(20)  # number will be 20
  float_num = float(20)  # str_num will be 20.0

  print(f"str_num = {str_num}")
  print(f"number = {number}")
  print(f"float_num = {float_num}")

  
#? 6) Python Variables - Multiple Assignment:
def var_multi_assignment():
  numb1 = 20
  numb2 = 20
  numb3 = 20
  print(numb1, numb2, numb3)

  # Instead of separate assignments, you can do it in a single assignment statement as follows −
  num1 = num2 = num3 = 20
  print(num1, num2, num3)

  # In the following case, we have three variables with different values.
  # These separate assignment statements can be combined in one. You need to give comma separated variable names on left, and comma separated values on the right of = operator.
  name, pswd, education = "Mukesh", "mukesh@4635", "Mtech-mechanical"

  print(name, pswd, education)


#? 7) Constants in Python:
def const_in_python():
  """
  Python doesn't have any formally defined constants, 
  However you can indicate a variable to be treated as 
  a constant by using all-caps names with underscores. 
  For example, the name PI_VALUE indicates that you don't 
  want the variable redefined or changed in any way.
  """
  PI_VALUE = 3.14
  print( PI_VALUE)