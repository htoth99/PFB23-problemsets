#!/usr/bin/env python3

#Problem 11
mylist = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
my2list = []

#print(mylist[0],mylist[1],mylist[2],mylist[3],sep="\t")
pos = 0

for seq in mylist:
  length_calc = len(seq)
  pos = pos + 1
  print(seq,length_calc,pos,sep="\t")
