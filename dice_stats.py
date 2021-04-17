import numpy as np
from statsmodels.stats.proportion import proportion_confint as bci
import mmct

def sum(arr):
  tot = 0
  for x in arr:
    tot += x
  return tot

def freq(arr):
  res = []
  tot = sum(arr)
  for x in arr:
    res.append(x/tot)
  return res

def expected_frequency():
  res = []
  for x in range(2,13):
    y = 6 - abs(7-x) # Expected number of rolls after 36 total rolls
    res.append(y/36)
  return res

def expected_rolls(total):
  arr = []
  for x in range(2,13):
    y = 6 - abs(7-x) # Expected number of rolls after 36 total rolls
    arr.append(total*y/36)
  return arr


def binom_ci(arr):
  total = sum(arr)
  res = np.zeros([11,2])
  for i in range(11):
    i_ci = bci(arr[i],total,method='wilson')
    res[i,0] = i_ci[0]
    res[i,1] = i_ci[1]
  return res


def test_dice(rolls):

  act_rolls = np.array(list(rolls.values()))
  exp_freq = np.array([1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36])

  t = mmct.tester()
  t.n_trials = 100000
  p = t.do_test(act_rolls,exp_freq)

  print("H0: Counts = Expected counts")
  print("Test: Exact two-sided multinomial test: p = %s" % p)
