# Write a Python program to calculate the length of a string
def lengthOfString(string):
  print(len(string))

def length_of_string(str):
  count = 0
  for c in str:
    count += 1
  return count

lengthOfString('t')
print(length_of_string('t'))