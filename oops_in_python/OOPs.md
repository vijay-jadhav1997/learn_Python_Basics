## ✨ Learn Object Oriented Programming 💥

1. class (Ex, Student)
2. Instance of class (Ex, `viju = Student(name, age, std, roll_num)` here `viju` is a instance of the Student class )
3. Instance attributes/variables and class attributes
4. dunder methods (Ex, `.__init__()` & ` .__str__()`)
5. Instance methods (Ex, `.greet()`)
6. Inheritance

### **Classes vs Instances** :

- **_Classes_** allow we to create **user-defined** **_data structures_**.
- _Classes define functions_ called **_methods_**, which identify the behaviors and actions that an object created from the class can perform with its data.
- A **_class_** is a blueprint for how to define something. It doesn’t actually contain any data.
- While the _class_ is the _blueprint_, an **_instance_** is **_an object_** that’s built from a class and contains real data.
- A **_class_** is like a **form** or questionnaire. An **_instance_** is like a form that we’ve filled out with information.
- Just like many people can fill out the same form with their own unique information, we can create many instances from a single class.

---

### **Class Definition** :

> Python class names are written in CapitalizedWords notation by convention. Ex, Employee, IndianCars,...

- All class definitions start with the **_class_** keyword, then add the name of the class and a colon. ex, `class Employee:`, `class IndianCows:`
- We define the properties that all class objects must have in a method called **\_\_init\_\_()**.
- Every time we create a new class object, .\_\_init\_\_() sets the initial state of the object by assigning the values of the object’s properties. That is, .\_\_init\_\_() initializes each new instance of the class.
- We can give **\_\_init\_\_()** any number of parameters, but the **_first parameter_** will always be a **_variable_** called **_self_**.
- When we create **_a new class instance_**, then Python automatically passes the instance to the **_self_** parameter in **\_\_init\_\_()** so that Python can define the new **_attributes_** on the object.

```py
class Employee:
  office_branch = "India"
  def __init__(self, name, age):
    self.name = name
    self.age = age
```

- In the body of **\_\_init\_\_()** method, there are two statements using the **_self_** variable:
  1.  `self.name = name` creates an attribute called name and assigns the value of the name parameter to it.
  2.  `self.age = age` creates an attribute called age and assigns the value of the age parameter to it.
- Attributes created in **\_\_init\_\_()** are called **_instance attributes_** (ex, `name` & `age`). An instance attribute’s value is specific to a particular instance of the class.
- All Employee objects have a name and an age, but the **_values_** for the **_name_** and **_age attributes_** will vary depending on the **_Employee_** class instance.
- On the other hand, **_class attributes_** are attributes that have the **_same value_** for **_all class instances_** (Ex, `office_branch`).
  > **_class attributes_** vs **_instance attributes_**
  >
  > - Use **_class attributes_** to define properties that should have the same value for every class instance.
  > - Use **_instance attributes_** for properties that vary from one instance to another.

---

### **How Do we Instantiate a Class in Python?**

- Creating a new object from a class is called instantiating a class.
- We can create a new **_object_** by typing the name of the class, followed by opening and closing parentheses `Employee(arg1,arg2,...)`.
- To instantiate this Employee class, we need to provide values for name & age. If we don’t, then Python raises a TypeError:

```py
  class Employee:
    office_branch = "India"
    def __init__(self, name, age):
      self.name = name
      self.age = age

  Employee() # op: TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'.

  #To pass arguments to the name and age parameters, put values into the parentheses after the class name:
  raghav = Employee("Raghav Mohan", 25)
  shyam = Employee("Shyam Murti", 32)

  # After we create the Employee instances, we can access their 'instance attributes' using dot notation:
  print(raghav.name) #op: "Raghav Mohan"
  print(shyam.age) #op: 32

  # we can access 'class attributes' the same way:
  print(raghav.office_branch) #op: "India"
  print(shyam.office_branch) #op: "India"
```

- One of the biggest advantages of using **_classes_** to organize data is that instances are guaranteed to have the attributes we expect. All Empolyee instances have `.office_branch`, `.name`, and `.age` attributes, so we can use those attributes with confidence, knowing that they’ll always return a value.
- Although the attributes are guaranteed to exist, their values can change dynamically:

```py
  shyam.name = "Govind Damodar"
  print(shyam.name) #op: "Govind Damodar"
  raghav.age = 55
  print(raghav.age) #op: 55
  shyam.office_branch = "USA (Head Office)"
  print(shyam.office_branch) #op: "USA (Head Office)"

```

> The key takeaway here is that custom objects are mutable by default.
> An object is mutable if we can alter it dynamically. For example, lists and dictionaries are mutable, but strings and tuples are immutable.

---

### **Instance Methods**

- **_Instance methods_** are **_functions_** that we define inside a class and can only call on an instance of that class.
- Just like **.init()**, an **_instance method_** always takes **_self_** as its first parameter.

```py
  class Employee:
    office_branch = "India branch"

    def __init__(self, name, age):
      self.name = name
      self.age = age

    # Instance method:
    def greeting(self):
      return f"Jay Jay Ram Krushna Hari dear {self.name}! Welcome to {self.office_branch} office."

    # Another Instance method:
    def naam_kirtan(self, naam):
      return f"{self.name} sings '{naam}.'"

  vithu = Employee("Vitthal Patil", "28 Yug")
  vithu.greeting()  # "Jay Jay Ram Krushna Hari dear Vitthal Patil! Welcome to India branch office."

  vithu.naam_kirtan("Shree Dnyanoba mauli Tukaram") # Vitthal Patil says 'Shree Dnyanoba mauli Tukaram.'

```

- This Employee class has two instance methods:
  1. **_.greeting()_** returns a string displaying the name and the office_branch of the employee.
  2. **_naam_kirtan()_** has one parameter called `naam` and returns a string containing the employee’s name and the 'naam' that the employee sings.

```py
  print(vithu) # op: <__main__.Employee object at 0x00aeff70>
```

- When we print miles, we get a cryptic-looking message telling us that vithu is a Employee object at the memory address 0x00aeff70. This message isn’t very helpful.
- We can change what gets printed by defining a special instance method called **_.\_\_str\_\_()_**.

```py
  # when we change the name of the Employee class’s .greeting() method to .__str__():
  class Employee:
    office_branch = "India branch"
    # .....

    def __str__(self):
      return f"Jay Jay Ram Krushna Hari dear {self.name}! Welcome to {self.office_branch} office."

    # .....

  keerti = Employee("Keerti Pande", 30)
  print(keerti) # op: Jay Jay Ram Krushna Hari dear Keerti Pande! Welcome to India branch office.
```

- Methods like `.__init__()` and `.__str__()` are called **dunder methods** because they begin and end with double underscores.

---

### **How Do We Inherit From Another Class in Python?**

- **_Inheritance_** is the process by which one class takes on the attributes and methods of another. Newly formed classes are called **child classes**, and the classes that you derive child classes from are called **parent classes**.

```py
  class Parent:
    hair_color = "black"
    speak = ["Marathi"]

  class Child(Parent):
    speak = ["Marathi", "Hindi"] # Here, we have overridden the speak attribute, (Not a best practice...)

  print(parent.hair_color) # op: black
  print(child.hair_color) # op: black
  # Because child classes take on the attributes and methods of parent classes, Child.hair_color is also "black" without our explicitly defining that

  print(parent.speak)   # op : ["Marathi"]
  print(child.speak)  # op : ["Marathi", "Hindi"]
  # Because in Child class we overridden the speak attribute, (It is said to be bad practice ❌)
```

- Child classes can override or extend the attributes and methods of parent classes.
  > In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.

```py
  class Parent:
    languages_speak = ["Marathi"]
    #......
    def speak(self, language):
      return f"I speak {languages_speak[0]}"

  class Child(Parent):
    languages_speak = ["Marathi", "Hindi", "English"]
    #.....
    def speak(self, language="Sanskrut")
      return super().speak(language)

  child = Child()
  print(Child.languages_speak) # op: ["Marathi", "Hindi", "English"]
  # Because child classes take on the attributes and methods of parent classes, Child.hair_color is also "black" without our explicitly defining that
```

> All objects created from a child class are instances of the parent class,
