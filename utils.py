from prettytable import PrettyTable
import numpy as np

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



def printResultsTable(rolls, sum, exp_rolls, freq, exp_freq, mnom_ci, bnom_ci):

  header_row = ["Eyes"]
  count_row = ["Count"]
  for a in rolls:
    header_row.append(a)
    count_row.append(rolls[a])

  header_row.append("Total")
  count_row.append(sum)

  exp_rolls_arr = ["Expected count"]
  exp_rolls_arr.extend(exp_rolls)
  exp_rolls_arr.append("")

  freq_rolls = ["Frequency"]
  freq_rolls.extend(freq)
  freq_rolls.append("")

  exp_freq_rolls = ["Expected freq."]
  exp_freq_rolls.extend(exp_freq)
  exp_freq_rolls.append("")

  lower_ci = ["95% sim. m.nom. CI"]
  lower_ci.extend(list(mnom_ci[:,0]))
  lower_ci.append("")

  upper_ci = [""]
  upper_ci.extend(list(mnom_ci[:,1]))
  upper_ci.append("")

  lower_bin_ci = ["95% binom. CI"]
  lower_bin_ci.extend(list(bnom_ci[:,0]))
  lower_bin_ci.append("")

  upper_bin_ci = [""]
  upper_bin_ci.extend(list(bnom_ci[:,1]))
  upper_bin_ci.append("")


  table = PrettyTable()
  table.field_names = header_row.copy()
  table.add_rows([count_row,exp_rolls_arr,freq_rolls,exp_freq_rolls,
    lower_ci,upper_ci,lower_bin_ci,upper_bin_ci])
  table.align = "r"
  table.float_format = ".2"
  print(table)
