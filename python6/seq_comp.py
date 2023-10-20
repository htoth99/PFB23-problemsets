#!/usr/bin/env python3

#Problem 7
seq_obj = open('Python_06.seq.txt','r')

#Each line looks like this: seqName	sequence\n so like two columns with a tab deliminated space


for line in seq_obj:
  line = line.rstrip() #removes \n
  split = line.split("\t") #splits file contents on tab
  seqName = split[0] #assigns the variable seqName to the first column (index 0)
  sequence = split[1].lower() #assigns the variable sequence to the second column (index 1)
  rev_seq = sequence[::-1] #this reverses dna
  rev_comp = rev_seq.replace('a','T')
  rev_comp = rev_comp.replace('t','A')
  rev_comp = rev_comp.replace('c','G')
  rev_comp = rev_comp.replace('g','C')
  print(f'>{seqName}\t{rev_comp}')

seq_obj.close()

