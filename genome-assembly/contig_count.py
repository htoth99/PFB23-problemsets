#!/usr/bin/env python3

import sys

file_in = sys.argv[1]
Id_len = {}

seq_length = 0
header = None
with open (file_in,'r') as file_in_obj:
  for line in file_in_obj:
    line = line.rstrip()
    if line.startswith('>'):
      if header is not None:
        print(header,seq_length)
        seq_length = 0
      header = line[1:]
      Id_len[header] = ''
    else:
      seq_length = seq_length + len(line)
      Id_len[header] = seq_length
if seq_length:
  Id_len[header] = seq_length
  sorted_dict = sorted(Id_len.items(), key = lambda x:x[1], reverse=True)
  print(sorted_dict)
