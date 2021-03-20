import utils
import dice_stats as ds
import numpy as np
from statsmodels.stats.proportion import multinomial_proportions_confint as mci

rolls = {}
for a in range(2,13):
    rolls[a] = 0

while True:

  x = utils.inputNumber("Enter dice roll: ")
  print('')

  rolls[x] += 1

  total_rolls = ds.sum(rolls.values())

  mnci = mci(list(rolls.values()))
  bnci = ds.binom_ci(list(rolls.values()))

  utils.printResultsTable(rolls,
    sum=total_rolls,
    exp_rolls=ds.expected_rolls(total_rolls),
    freq=ds.freq(rolls.values()),
    exp_freq=ds.expected_frequency(),
    mnom_ci=mnci,
    bnom_ci=bnci)

  ds.test_dice(rolls)

  print('')
  print('')
  print('')
