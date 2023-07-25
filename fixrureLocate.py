import csv

testShelf = []

with open("../shelf bin location.csv", 'r') as file:
  reader = csv.DictReader(file)
  for line in reader:
    testShelf.append({"shelf": line["shelf"], "row": line["row"], "bin": line["bin"], "assembly": line["assembly"]})

def findAssembly(item):
  for i in testShelf:
    if item in i['assembly']:
      # print(i['shelf'], i['row'], i['bin'])
      num1 = i['shelf']
      num2 = i['row']
      num3 = i['bin'] 
      return num1, num2, num3

while True:
  print('what board are you looking for? ')
  print('To leave, press ctrl+c')
  item = input('--> ').upper()

  try:
    print(findAssembly(item))
  except TypeError:
    print('invalid assembly, please try again')

    