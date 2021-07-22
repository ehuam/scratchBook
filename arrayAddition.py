#!/usr/bin/env python3

# Power sets are combinations.
def ArrayAdditionI(arr):
  from itertools import combinations

  maxNum = sorted(arr)[-1]
  array_without_max = sorted(arr)[:-1]

  for i in range(2, len(array_without_max)):
    for comb in combinations(array_without_max, i):
      if sum(comb) == maxNum:
        return True
  # code goes here
  return False
