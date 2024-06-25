# WRITE YOUR CODE HERE
def swap(dictionary):
  swapped_dict = {}
  try:
    for key, value in dictionary.items():
      swapped_dict[value] = key
  except TypeError:
    return "Cannot swap the keys and values for this dictionary"
  return swapped_dict


