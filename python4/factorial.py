#!/usr/bin/env python3

#Problem 5 - calculating factorial
#1000! = 1000*999*998*997*996.....

countdown = 1000
total = 1000

while countdown > 0:
  subtract = countdown - 1
  if subtract == 0:
    break
  else:
    total = subtract * total
    countdown = countdown - 1
total = total + 1
print(total)

#  operation = 1000*subtract
#  total = total + operation
#  countdown = countdown - 1
#print(total)

  
