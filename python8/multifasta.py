#!/usr/bin/env python3
import re
#Problem 1

multi_fasta = {}
with open('Python_08.fasta','r') as file_obj:
  for line in file_obj:
    line = line.rstrip()
    find_seq = re.search(r'(>)(\w+\s*?)',line)
    if find_seq:
      seqID = find_seq.group(2)
      print(seqID)




