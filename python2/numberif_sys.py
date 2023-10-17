#!/usr/bin/env python3
import sys

num = sys.argv[1]
num = int(num)

if num <0:
  print('The number is negative')
elif num == 0:
  print('The number is equal to 0')
elif num >0:
  print('The number is positive')
  if num <50:
    print('The number is + and less than 50')
    if num%2 == 1:
      print('The number is positive, less than 50, and odd')
    else:
      print('The number is positive, less than 50, and even')
  elif num == 50:
    print('The number is equal to 50')
  else:
    print('The number is positive and great than 50')
    if num/3 - int(num/3) == 0:
      print('The number is greater than 50 and is divisble by 3')
    else:
      print('The number is greater than 50 and is not divisble by 3')
