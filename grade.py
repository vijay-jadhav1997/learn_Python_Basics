# get student score
score = float(input("Score : "))

#* if_else statement with "and -logical operator"
if score >= 90:
  print("Grade : O++")
elif score >= 80 and score < 90:
  print("Grade : O")
elif score >= 70 and score < 80:
  print("Grade : A+")
elif score >= 60 and score < 70:
  print("Grade : B+")
elif score >= 50 and score < 60:
  print("Grade : C+")
else:
  print("Grade : F; You are failed")

#* if_else statement 
if score >= 90:
  print("Grade ==> O++")
elif 80 <= score < 90:
  print("Grade ==> O")
elif 70 <= score < 80:
  print("Grade ==> A+")
elif 60 <= score < 70:
  print("Grade ==> B+")
elif 50 <= score < 60:
  print("Grade ==> C+")
else:
  print("Grade ==> F; You are failed")


#* Another way to reduce our code:
if score >= 90:
  print("==> Grade : O++")
elif score >= 80 :
  print("==> Grade : O")
elif score >= 70 :
  print("==> Grade : A+")
elif score >= 60 :
  print("==> Grade : B+")
elif score >= 50 :
  print("==> Grade : C+")
else:
  print("==> Grade : F; You are failed")