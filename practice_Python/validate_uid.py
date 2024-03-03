import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
  # n = int(input())
  uids = ["B1CD102354", "B1CDEF2354"]
  # for _ in range(n):
  #   employee_id = input()
  #   uids.append(employee_id)
  
  id_regex = r"\w{10}"
  id_regex = r"[A-Z]+"
  for id in uids:
      if re.search(id_regex, id):
        isvalid = "Valid"
        for i in id:
          if id.count(i) > 1:
            isvalid = "Invalid"
        print(isvalid)
      else:
        
        print("InValid")
         

if __name__ == "__main__":
  pass