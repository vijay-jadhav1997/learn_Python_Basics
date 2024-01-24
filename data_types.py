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
print(type(decade))

statement = "I like classical music from the " + decade + "s."
statement2 = f"I like classical music from the {decade}s." #* literal assignment
print(statement)
print(statement2)