############ Jay Shree Ram krushna Hari ###############
#? how to define dictionary
#? 1) Literal method
band = {
  "langauge" : "Python",
  "framework": "django"
}

#? 2) using 'dict()' Constructor:
newdict = dict(name= "Madhav", std= "10th", roll_numb = 122)

# print(band)
# print(newdict)

#? Access items:
print(band["langauge"])
print(band.get("framework"))

#? list all keys
band.keys()
# print(band.keys())

#? list all values
# print(band.values())

#? list of key/value pairs as tuples
# print(band.items())

#? verify a key exist
print("langauge" in band)
print("lang" in band)

#? Change Values
band["framework"] = "flask"
band.update({"ismultithreaded": False})
# print(band)

#? Remove items
band.pop("ismultithreaded")
# print(band)

#? Delete and clear
band["music"] = "Indian classical"
del band["music"]
newdict.clear()
# print(newdict)
# print(band)

#? copy dictionaries:
band["music"] = "Indian classical"
band2 = band  #* creates a reference, but not a copy.
del band2["music"]
# print(band)
# print(band2)

band["music"] = "Indian classical"
band3 = band.copy()  #* here, it creates copy 
# del band["music"]
# print(band)
# print(band3)
#? create copy using constructor function
band4 = dict(band) 


