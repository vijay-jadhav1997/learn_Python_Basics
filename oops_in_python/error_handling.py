mydict = {'a': 1, 'b': 2}

try:
  print(2/0)
except (ZeroDivisionError, Exception):
  # print(Exception.)
  print(Exception.args)



def make_delim_line(list_to_join, delim):

  try:
    formatted_line = delim.join(list_to_join)
  except TypeError:
    raise TypeError("make_delim_line(): arg1 must be a list or tuple")
  return formatted_line

# fline = make_delim_line([100, 200], ',')