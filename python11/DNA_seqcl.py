#!/usr/bin/env python3

#This problem asks me to create a DNA sequence class that will contain a sequence, its name, and organism 
#via the __init__ function

class DNA_recs(object):
#defining class attributes
  def __init__(self,sequence,seqID,organism):
    self.sequence = sequence
    self.seqID = seqID
    self.organism = organism
#Determine sequence length
  def seqLen(self):
    length_sequence = len(self.sequence)
    return length_sequence
#Determine nt composition
  def ntComp(self)
    count_dict = {}
    count_dict[self.seqID] = {'A':0,'T':0,'G':0,'C':0}
    



    a_count = self.sequence('A')
    t_count = self.sequence('T')
    g_count = self.sequence('G')
    c_count = self.sequence('C')
#creating new record objects
dnaR1 = DNA_recs('GATTACGACTAGA','silly_gene','piper')
dnaR2 = DNA_recs('GATACGACGACTA','cute_gene','abby')

#Printed out the sequence, gene ID, and organism
print(f'The sequence is {dnaR1.sequence}')
print(f'The gene ID is {dnaR1.seqID}')
print(f'The organism is {dnaR1.organism}')

#What's the length of my seqence?
print(f'The length of Pipers sequence is {dnaR1.seqLen()}')
