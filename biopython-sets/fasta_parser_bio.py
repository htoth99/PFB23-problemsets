#!/usr/bin/env python3

import Bio

from Bio import SeqIO


long = 0
short = 10000000000000000

for seq_obj in SeqIO.parse("Python_08.fasta","fasta"):
  if len(seq_obj.seq) > long:
    long = len(seq_obj.seq)
  if len(seq_obj.seq) < short:
    short = len(seq_obj.seq)
