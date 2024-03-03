chant = "Jay Jay Shree Dnyanoba Mauli Tukaram"

name = "Govind"
age = 25

#?  The string interpolation operator (%), or modulo operator :
modulo_string = "I'm %s and %s years old"%(name, age)
print(modulo_string)
modulo_string = "I'm %(name)s and %(age)s years old"%{"name": "Raghav", "age": 30}
print(modulo_string)

"""
The conversion specifiers work as replacement fields. In the above example,
you use the %s combination of characters as a conversion specifier. 
The % symbol marks the start of the specifier, while the s letter is the conversion type and 
tells the operator that you want to convert the input object into a string.
"""

rounded_str = "Balance: $%.2f" % 5425.9292
print(rounded_str)
"""
In the above example, you use the %.2f conversion specifier to represent currency values. 
The 'f' letter tells the operator to convert to a floating-point number. 
The '.2' part defines the precision to use when converting the input. 
"""


#?  The str.format() method :
f_string1 = "I'm {} and {} years old".format(name, age)
print(f_string1)

"""
For the .format() method to work, you must provide replacement fields using curly brackets. 
If you use empty brackets, then the method interpolates its arguments into 
the target string based on position.
"""

f_string2 = "I'm {1} and {0} years old".format(age, name)
print(f_string2)

"""
In this example, we use numeric indices to manually define the order in which 
we want to interpolate the values that we pass as arguments to .format().
"""

f_string3 = "I'm {name} and {age} years old".format(name="Manmohan", age= 125)
print(f_string3)


str1 = "Jay Hari, {1}! You're {0} years old."

str1 = str1.format(age, name)

print(str1)


