#!/usr/bin/env python3

#Problem 6
nums = [101,2,15,22,95,33,2,27,72,15,52]
nums_it = iter(nums)
for i in nums_it:
  if i%2 == 0:
    print(i)

#Problem 7
odds = 0
evens = 0

nums2 = [101,2,15,22,95,33,2,27,72,15,52]
nums2_it = iter(nums2)

for n in nums2_it:
  if n%2 == 0:
   evens = n + evens
  else:
   odds = n + odds

print(odds)
print(evens)
