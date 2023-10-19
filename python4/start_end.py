#!/usr/bin/env python3
import sys

#Problem 10
start_val = int(sys.argv[1])
end_val = int(sys.argv[2])

val_range = range(start_val,end_val)
for i in val_range:
  if i%2 != 0:
    print(i)


#printme = [print(num) for num in range(start_val,end_val)]

