#!/usr/bin/env python3

#Problem 8
line_count = 0
char_count = 0
sum_of_lengths = 0
with open ("Python_06.fastq","r") as file_input:

  for line in file_input:
    if line != "\n":
      line_count += 1
    len_line = len(line) #the indentation here matters
    char_count = len_line + char_count #the indentation here matters 
    sum_of_lengths = sum_of_lengths + len_line

avg_len = sum_of_lengths/line_count
     
 
#  char_count = len(file_input)
print(f'The number of lines is {line_count}')
print(f'The number of characters is {char_count}')
print(f'The average length of the lines is {avg_len}')
