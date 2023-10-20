#!/usr/bin/env python3

#Problem 1
import re

list_pos = []
noone_obj = open("Python_07_nobody.txt","r")
hannah_w = open('hannah_nobody.txt','w')
noone = noone_obj.read()
for i in re.finditer(r"(Nobody)",noone):
  group_nobods = i.group(1)
  positions = i.start(1) + 1
  new_nobodies = re.sub(group_nobods,'Hannah',noone)
#  list_pos.append(positions)
#  list_pos.append(group_nobods)
  print(group_nobods,positions)  
  hannah_w.write(new_nobodies)
#  print(new_nobodies,positions)
print(list_pos)

noone_obj.close()

