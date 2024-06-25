# WRITE YOUR CODE HERE
# specific key is moved to bottom!!!!

def move_to_bottom(your_dict, target):
  if target not in your_dict:
    return 'The key is not in the dictionary'
  target_value = your_dict[target]
  del your_dict[target]
  your_dict[target] = target_value
  return your_dict
    

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 1)
  print(example_dict)