# print 'jay hari'  
# print("Jay Hari to All of devotees of Hari & Har ....!")

# Ask user for their name
name = input("What's your name? ")

#* Remove all unnecessary whatspaces from string using '.strip()' string method
name = name.strip().title()
userName = name.title().strip()

#* Capitalize each word of string using '.title()' method: Return a version of the string where each word is titlecased.
# name = name.title()

#? method chaining ".strip().title()" :

# Say Jay Hari to user
#* 1) 1st method:
# print("Jay Hari, " + name)

#* 2) 2st method:
# print("Jay Hari, ", name)

#* 3) 3rd method: using f"${varName}"
print(f"Jay Hari, {name}" + " Govind") 
print(f"Jay Hari, {userName}" ) 