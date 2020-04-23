import ast

def comma(list):
  output = ''
  for i in range(len(list)):
    if i != len(list) - 1:
      output += list[i] + ', '
    else:
      output += 'and ' + list[i]
  return output

if __name__ == "__main__":
    try:
      print('Enter a list:')
      list = ast.literal_eval(input())
      print(comma(list))
    except:
      print('Error: Invalid Value. You did not enter a list.')
