#!/usr/bin/env python3

#Problem 5
py6_obj = open("python_06.txt","r")

for line in py6_obj:
  upped = line.upper()
  upped = upped.rstrip()
  print(upped)

py6_obj.close()
#Problem 6
with open("python_06.txt","r") as song_read, open("Python_06_uc.txt","w") as song_write:
 for line in song_read:
  upper_song = line.upper()
  upper_song = upper_song.rstrip()
  song_write.write(upper_song)

