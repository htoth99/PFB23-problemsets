#!/usr/bin/env python3
import re
#Problem 1

seq_ID = ''
nt = ''
multi_fasta = {}
count_dict = {}


with open('Python_08.fasta','r') as file_obj:
  for line in file_obj:
    line = line.rstrip()
    find_ID = re.search(r'(>)(\w+\s*?)',line)
    if find_ID:
      seqID = find_ID.group(2)
      multi_fasta[seqID] = ''    

    else:
      nt = line
      multi_fasta[seqID] += nt
#  print(multi_fasta) 
  for seqID in multi_fasta:
    seqS = multi_fasta[seqID]
    if seqID not in count_dict:
      count_dict[seqID] = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}
    count_dict[seqID]['A'] = seqS.count('A')
    count_dict[seqID]['T'] = seqS.count('T')
    count_dict[seqID]['G'] = seqS.count('G')
    count_dict[seqID]['C'] = seqS.count('C')
  print(count_dict)
  #  Acount = nt.count('A')
  #  Tcount = nt.count('T')
  #  Gcount = nt.count('G')
  #  Ccount = nt.count('C')

      
#      multi_fasta[seq_ID] = {nt,nt_count}



#multifasta[seqID][nt]=count

