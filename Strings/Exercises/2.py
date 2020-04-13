# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

str = 'google.com'

dicttionary = {}
for n in str:
  keys = dicttionary.keys()
  if n in keys:
    dicttionary[n] += 1
  else:
    dicttionary[n] = 1

print(dicttionary) 

