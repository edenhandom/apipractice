# WRITE YOUR CODE HERE
import json
def compare(file1, file2):
  with open(file1, 'r') as file1, open(file2, 'r') as file2:
    dict1 = json.load(file1)
    dict2 = json.load(file2)

    if dict1 == dict2:
      return 'The dictionaries are equal'
    else:
      count1 = len(dict1)
      count2 = len(dict2)
      if count1 > count2:
        return 'Dictionary 1 is longer than dictionary 2'
      elif len(dict2) > len(dict1):
        return 'Dictionary 2 is longer than dictionary 1'
      else:
        return 'Dictionary 1 and dictionary 2 have the same length'
# test code below
# test code below
if __name__ == "__main__":
  import sys
  
  file1 = sys.argv[1]
  file2 = sys.argv[2]

  print(compare(file1, file2))