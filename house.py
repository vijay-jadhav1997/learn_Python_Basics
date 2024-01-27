name = input("What's your name? ").strip().title()

# Do using 'if_else' statement:
if name == 'Gopal':
  print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
elif name == 'Dnyaneshwar':
  print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
elif name == 'Prakash':
  print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
elif name == 'Bhagwan':
  print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
elif name == 'Sarang':
  print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
elif name == 'Pradip':
  print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
elif name == 'Swapnil':
  print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
elif name == 'Mahesh':
  print(f"{name} Maharaj is student of Shree Bahinabai Sangeet Vidyalay, Shivoor")
elif name == 'Tukaram':
  print(f"{name} Maharaj is student of Shree Bahinabai Sangeet Vidyalay, Shivoor")
elif name == 'Avinash':
  print(f"{name} is student of Pravara Rural Engg. College, Loni")
elif name == 'Shubham':
  print(f"{name} is student of Sanjivani Engg. College, Kopargaon")
else:
  print(f"Who's {name}? ")

# Do using 'match' statement (equivalent to 'switch' statement in JS)

match name:
  case 'Gopal':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Dnyaneshwar':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Vijay':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Swapnil':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Pradip':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Prakash':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Bhagwan':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Sagar':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Ankush':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Krushna':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Rahul':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Mahesh':
    print(f"{name} Maharaj is student of Shree Bahinabai Sangeet Vidyalay, Shivoor")
  case 'Tukaram':
    print(f"{name} Maharaj is student of Shree Bahinabai Sangeet Vidyalay, Shivoor")
  case 'Avinash':
    print(f"{name} is student of Pravara Rural Engg. College, Loni")
  case 'Gitesh':
    print(f"{name} is student of Pravara Rural Engg. College, Loni")
  case 'Shubham':
    print(f"{name} is student of Sanjivani Engg. College, Kopargaon")
  case _:
    print(f"Who's {name}? ")


#* Yet precise way of writing above code using match statement:
match name :
  case 'Gopal' | 'Dnyaneshwar' | 'Swapnil' | 'Vijay' | 'Rahul' | 'Krushna' | 'Prakash' | 'Pradip' | 'Shastri' | 'Sagar' | 'Ankush' | 'Ravindra':
    print(f"{name} Maharaj is student of Shree Tukaram Maharaj student Hermitage, Shivoor")
  case 'Mahesh' | 'Tukaram':
    print(f"{name} Maharaj is student of Shree Bahinabai Sangeet Vidyalay, Shivoor")
  case 'Avinash' | 'Gitesh' | 'Pradumn' | 'Aditi':
    print(f"{name} is student of Pravara Rural Engg. College, Loni")
  case 'Shubham':
    print(f"{name} is student of Sanjivani Engg. College, Kopargaon")
  case _:
    print(f'Who\'s {name} ?')