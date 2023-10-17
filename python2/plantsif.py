#!/usr/bin/env python3

plants = 35

if plants < 0:
  print('I do not have any plants')
elif plants < 10:
  print('I have some plants, but not enough')
elif plants == 15:
  print('I have a sufficient number of plants')
else:
  print('I probably have too many plants')
