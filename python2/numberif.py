#!/usr/bin/env python3

number_testing = 50

if number_testing <0:
  print('The number is negative')
elif number_testing == 0:
  print('The number is equal to 0')
elif number_testing >0:
  print('The number is positive')
  if number_testing <50:
   print('the number is positive and less than 50')
   if number_testing%2 == 1:
    print('The number is positive, less than 50, and odd')
   else:
    print('The number is positive, less than 50, and even')
  elif number_testing == 50:
   print('The number is equal to 50, which means its even and not divisble by 3')
  else:
   print('the number is positive and greater than 50')
   if number_testing/3 - int(number_testing/3) == 0:
    print('The number is greater than 50 is divisble by 3')
   else:
    print('The number is greater than 50 and is not divisble by 3')
