#!/usr/bin/env python3
import sys
import subprocess


file_input = sys.argv[1]
header = ''
nt = ''
myfastalist = []
contig_length = []
sort_length = []
#number of contigs in file
grep_cmd = f'grep -c ">" {file_input}'
contig_num = subprocess.check_output(f'grep -c ">" {file_input}', shell = True)
print(f'There are {contig_num} contigs in {file_input}')

with open(file_input,'r') as fasta_file_in:
  for line in fasta_file_in:
    if line.startswith('>'):
      header = line.rstrip().lstrip('>')
      if nt:
        continue
      else:
        myfastalist.append(nt)
    else:
      line = line.rstrip()
      nt = nt + line
#      contig_length = len(nt)
#      sort_length = sorted.contig_length()
  myfastalist.append(nt)
  sort_myfasta = sorted(myfastalist)
  zero_index_mylist = len(myfastalist[1])
  len_of_list = len(myfastalist)
  print(len_of_list)
  print(zero_index_mylist)



