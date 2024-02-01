import random

def main():
  get_random_choice()
  shuffle_list()


#! Learn Random Module
#? 1) Functions for sequences:

#* i) random.choice(seq) : returns a random element from the non-empty sequence 'seq'.
#     "seq" can be => str, list, tuples, etc. (i.e. Works with any iterable (lists, tuples, strings, etc.))
def get_random_choice():
  random_element = random.choice([1, 2, 3, True, "Jay Hari", 25])
  random_num = random.choice(range(1,100))
  toss = random.choice(["Head", "Tail"])
  print(random_element, random_num, toss)
  return toss

#* ii) random.shuffle(x) : Shuffle list x in place, and return None.
#     x can be =>  list, tuples, etc. 
def shuffle_list():
  range_object = range(5, 25) # we can't directly random.shuffle(range_object)
  list_object = list(range_object)
  random.shuffle(list_object)


#* iii) random.sample(population, k, *, counts=None)
# Return a 'k' length of list of unique elements chosen from the population sequence. Used for random sampling without replacement.
# Returns a 'new list' containing elements from the population while leaving the original population unchanged.
def sample_list():
  scores = [1,2,3,2,3,4,5,2,1,4,2,5]
  sample_scores = random.sample(scores, 6)
  print(sample_scores)
   # possible result => sample_scores = [3,5,4,2,3,2] and len(sample_scores) is 6 (i.e. equal to 'k') 
   # scores = [1,2,3,2,3,4,5,2,1,4,2,5] (i.e. it will remain unchanged)


#? 2) Functions for integers:

#*  1) random.randrange(stop) and/or random.randrange(start, stop[, step])
#* Return a randomly selected element from range(start, stop, step).
def get_random_integer():
  random_int1 = random.randrange(200)
  print(random_int1) # possible result => 1, 2, 3, 4, 5, 6, 7, 8, 9,....and 199.
  random_int = random.randrange(1,25, 2)
  print(random_int) # possible result => 1, 3, 5, 7, 9,....and 24.
  random_int2 = random.randrange(50,100, 5)
  print(random_int2) # possible result => 50, 55, 60, 65, 70, 75, 80, 85, 90,....and 99.


#*  2) random.randint(a, b) :
#*   Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
def get_random_integer():
  random_int1 = random.randrange(200)
  print(random_int1) # possible result => 1, 2, 3, 4, 5, 6, 7, 8, 9,....and 199.
  random_int = random.randrange(1,25, 2)
  print(random_int) # possible result => 1, 3, 5, 7, 9,....and 24.
  random_int2 = random.randrange(50,100, 5)
  print(random_int2) # possible result => 50, 55, 60, 65, 70, 75, 80, 85, 90,....and 99.
  
  

if __name__ == "__main__":
  main()