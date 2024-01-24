####  ##### ####### ######## ########### ######### ###### ####
#? String data type:
fName = "Jay Shree Ram"
lName = "Jay Shree Krushna"
#* Here, fName is variable name and "Jay Shree Ram" is a the value of variable.
#* variable name => lName
#* 'lName' variable value => "Jay Shree Krushna"



#? literal assignment:
userName = 'Jay Shree Ram'

# print(f"'{userName}' is popular and holy slogan in Bharatiy Culture.") # f"{varName}"

# print(fName, lName, sep="-", end="")
# print(fName, lName)
# print(fName, lName, sep="-")
# print(fName, lName, sep="-", end="**")
# print(fName, lName, end=" ")

#? to check data type using following ways:
# print(type(userName))
# print(type(userName) == str)
# print(isinstance(userName, str))

#? constructor fn for string:
user = str("Jay_Shree_Vitthal")
# print(type(user))
# print(type(user) == str)
# print(isinstance(user, str))

#? Concatetion of strings:
fullName = fName + " " + lName

# print(fullName)

fullName += "@JayHari"
# print(fullName)

#? Casting a number to a string:
decade = str(1990)
# print(type(decade))

statement = "I like classical music from the " + decade + "s."
statement2 = f"I like classical music from the {decade}s." #* literal assignment
# print(statement)
# print(statement2)

#? Multiple lines :
multiple = '''
Jay Hari, How are You?       

I was     really missed    you.
                     Ok. All good?
''' 

# print(multiple)


#? Escaping special characters using '\' backward slash:
sentense = 'I\'m Vijay, aspiring to become skilled full stack developer.\n I would like to cooperate with your project.\n\t Please, consider me for next meet!'
# print(sentense)

#? String methods:
myFav = 'har har mahadev'
#* 1) .lower(): Return a copy of the string converted to lowercase.
# print(myFav.lower()+ "Jay Shree Ram")

#* 2) .upper() : Return a copy of the string converted to uppercase.
# print(myFav.upper()+ "Jay Shree Ram")

#* 3) .title() : Return a version of the string where each word is titlecased.
# print(myFav.title()+ "Jay Shree Ram")

#* 4) .strip() : Return a copy of the string with leading and trailing whitespace removed.
# print(myFav.strip()+ " Jay Shree Ram")

#* 5) .replace("old subString", "new subStirng"): Return a copy with all occurrences of substring old replaced by new.
# print(myFav.replace("mahadev", "gange") + " Jay Shree Ram")

#? method chaining:  str.replace().lower().strip().title()
# print(myFav.strip().title() + " Jay Shree Ram")
# print(myFav.replace("mahAdev", "gange").strip().title() + " Jay Shree Ram")
# print(myFav.strip().title().replace("Mahadev", "Gange") + " Jay Shree Ram")

#! len(): Return the number of items in a container.
# print(len(myFav))
myFav += "         "
# print(len(myFav))
myFav = "         " + myFav
myFav = myFav.strip()
# print(len(myFav))
# print(len(myFav.strip()))

#! Build a menu 
heading = "Menu".upper()
#* 6) .center(width, "="): Return a centered string of length width.
#* 7) .ljus(width, "="): Return a left-justified string of length width.
#* 8) .rjust(width, "="): Return a right-justified string of length width.
# print(heading.center(20, '='))
# print("Milk".ljust(16, ".") + "₹".rjust(5, " "))
# print("Coffee".ljust(16, ".") + "₹".rjust(5, " "))
# print("Tea".ljust(16, ".") + "₹".rjust(5, " "))
# print("Sugacane Juice".ljust(16, ".") + "₹".rjust(5, " "))


#? string index values :
# print(myFav[0])
# print(myFav[1])
# print(myFav[-1])
# print(myFav[-2])
# print(myFav[-3])
# print(myFav[0:])
# print(myFav[1:])
# print(myFav[3:])
# print(myFav[7:])
# print(myFav[7:-3])
# print(myFav[0:-7])

#? Some string methods returns boolean data:
#* 9) str.startswith("sub-string"): returns true/false according to presence of starting of str with sub-string.
# print(myFav.startswith('h'))
# print(myFav.startswith('e'))
# print(myFav.startswith('har'))

#* 10) str.endswith("sub-string"): returns true/false according to presence of ending of str with sub-string.
# print(myFav.endswith('h'))
# print(myFav.endswith('e'))
# print(myFav.endswith('har'))


