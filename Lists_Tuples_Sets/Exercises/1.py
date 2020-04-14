list = [1,2,3,-2]
# Write a Python program to sum all the items in a list.
def sum_all_items(list):
  result = 0
  for item in list:
    result += item
  return result

print(sum_all_items(list))

# Write a Python program to multiplies all the items in a list.
def mul_all_items(list):
  result = 1
  for item in list:
    result *= item
  return result

print(mul_all_items(list))

# Write a Python program to get the largest number from a list.
def max_of_list(list):
  max = list[0]
  for num in list:
    if num > max:
      max = num
  return max

print(max_of_list(list))