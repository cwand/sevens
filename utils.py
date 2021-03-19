
def inputNumber(message):
  while True:
    try:
      userInput = int(input(message))
    except ValueError:
      print("Not an integer! Try again.")
      continue
    else:
      if (userInput < 2) or (userInput > 12):
        print("Number must be between 2 and 12! Try again.")
        continue
      return userInput 
    break
