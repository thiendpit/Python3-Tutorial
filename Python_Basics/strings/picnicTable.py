def printPicnic(itemsDict, leftWidth, righWidth):
  print('PICNIC ITEMS'. center(leftWidth + righWidth, '-'))
  for k, v in itemsDict.items():
    print(k.ljust(leftWidth, '.') + str(v).rjust(righWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)