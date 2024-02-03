"""
#? Python is completely object oriented, and not "statically typed".
#? You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

#? Unlike other programming languages, Python has no command for
#? declaring a variable. A variable is created the moment you first assign a value to it.

#? A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

#? Rules for Python variables:
#? - A variable name must start with a letter or the underscore character.
#? - A variable name cannot start with a number.
#? - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
#? - Variable names are case-sensitive (age, Age and AGE are three different variables).
"""
#* In python variable never be any data type, but actually values are of different data type

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