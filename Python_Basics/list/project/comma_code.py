def commaCode(list):
  string = ''
  for i in range(len(list)):
    if i != len(list) - 1:
      string += str(list[i]) + ', '
    else:
      string += 'and ' + str(list[i])
  return string

if __name__ == "__main__":
    list = ['apples', 'bananas', 'tofu', 'cats']
    print(commaCode(list))
