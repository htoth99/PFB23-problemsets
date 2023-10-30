#!/usr/bin/env python3

#Problem 9
#the goal is to create a fasta dictionary, with the seqID beeing the key and the sequence being the value

fastaDict = {}
with open ('rev_comp.fasta','r') as fasta_obj:
  for line in fasta_obj:
    line = line.rstrip()
    if line.startswith(">"):
     carrot,totalfasta = line.split(">") #if line starts with >, it will have ID and the carrot
     gene_ID,seq = totalfasta.split("\t") #this will return a list
     fastaDict[gene_ID] = seq #defining empty dictionary with keys and values
print(fastaDict)


