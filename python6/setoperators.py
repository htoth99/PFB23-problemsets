#!/usr/bin/env python3

#Problem 2
a = {3,14,15,9,26,5,35,9}
b = {60,22,14,0,9}

#Intersection
intersect = a & b
print(f'The intersection is {intersect}')
#Differences
diff = a - b
diff2 = b - a
print(f'The diff between a and b is {diff} and the diff between b and a is {diff2}')
#Union
union = a | b
print(f'The union is {union}')
#Symetrical difference
sym_diff = a ^ b
print(f'The symmetrical difference {sym_diff}')
