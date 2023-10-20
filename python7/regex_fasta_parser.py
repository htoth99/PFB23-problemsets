#!/usr/bin/env python3
import re
#Problem 5
#the goal is to create a fasta dictionary, with the seqID beeing the key and the sequence being the value

fastaDict = {}
with open ('rev_comp.fasta','r') as fasta_obj:
  for line in fasta_obj:
    line = line.rstrip()  
    find_seq = re.search(r'(\s)(\w+)',line)
    found_seq = find_seq.group(2)
    find_ID = re.search(r'(>)(\w+)',line)
    found_ID = find_ID.group(2)

    fastaDict[found_ID] = found_seq
print(fastaDict)
 

#  for line in fasta_obj:
 #   line = line.rstrip()
 #   if line.startswith(">"):




  #   carrot,totalfasta = line.split(">")
   #  gene_ID,seq = totalfasta.split("\t") #this will return a list
    # fastaDict[gene_ID] = seq #defining empty dictionary with keys and values
#print(fastaDict)


