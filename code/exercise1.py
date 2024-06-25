def find_key(d, v):
  keys = list(d.keys())
  values = list(d.values())
  index = values.index(v)
  return keys[index]

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  key = find_key(example_dict, (9, 10))
  print(key)