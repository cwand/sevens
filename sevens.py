import utils

rolls = {}
for a in range(2,13):
    rolls[a] = 0

while True:

  x = utils.inputNumber("Enter dice roll: ")
  print('')

  rolls[x] += 1

  print(rolls)

  print('')
  print('')
  print('')
