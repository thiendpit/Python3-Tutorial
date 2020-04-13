# num = [1, 2, 3]
# list = ['cat', 'bat', 'rat', 'elephant']
# list2 = ['hello', 3.1415, True, None, 42]

catNames = []
while True:
  print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.):')
  name = input()
  if name == '':
    break
  catNames = catNames + [name]
print('The cat names are: ')
for name in catNames:
  print('  ' + name)