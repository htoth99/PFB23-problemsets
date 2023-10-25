#!/usr/bin/env python3
import re
import sys

dna_input ='GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGGATAGGGGGGGGGGAAAAAAAAAAAAAAAAAAAAAAAA'

dna2_input = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''


#Problem 3
def nt_60(dna):
  dna_60 = re.sub(r'(\w{1,60})',r'\1\n',dna)
  return(dna_60)

def wrap_nt60(dna):
  lines = dna.split() #splits on white space, aka line breaks
  seq = ''.join(lines) #makes a string, join elements of a sequence
  wrapped_final = nt_60(seq)
  return(wrapped_final)

def wrap_nt2(dna,width_s):
  width = int(width_s)
  lines = dna.split()
  complete_S = ''
  for left_side in range(0,len(lines),width):
    if left_side + width < len(lines):
      complete_S = lines[left_side:(left_side + width)] + complete_S
    else: 
      complete_S = lines[left_side:len(lines)]
    
    
#print(nt_60(dna_input))
#print(wrap_nt60(dna2_input))
print(wrap_nt2(dna2_input,20))
