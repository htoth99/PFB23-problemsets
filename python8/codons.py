#!/usr/bin/env python3
import sys
import re

#Problem 2
file_input = sys.argv[1]

my_dict = {}
seqID = ''
nt = []


with open (file_input,'r') as fasta_read, open ('Python_08.codons-frame-1.nt','w') as writing_file:
  for line in fasta_read:
    if line.startswith('>'):
      seqID = line.rstrip().lstrip('>')
      my_dict[seqID] = []
      prec_line = '' #resetting string for each seqID
    else:
      prec_line += line
      codon_list = re.findall(r'(.{3})',prec_line)
      my_dict[seqID] = codon_list
  
  writing_file.write(str(my_dict))
