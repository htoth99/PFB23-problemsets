#!/usr/bin/env python3
import sys

#Problem 1
favs = {}

favs['pet'] = 'Piper'
favs['color'] = 'green'
favs['plant'] = 'philo'

#you could also do it this way
favs2 = {}
listfavs = ['person','rhys','plant','monstera','treet','ginko','food','pasta']
for i in range(0,len(listfavs),2): #step of 2
  favs2[listfavs[i]]=listfavs[i+1]
print(favs2)

#Problem 2
print(favs['plant'])

#Problem 3
fav_thing = 'color'
print(favs[fav_thing])

#Problem 4
print(favs['pet'])

#Problem 5
favs['organism'] = 'Xanthomonas'
fav_thing = 'organism'
print(favs[fav_thing])

#Problem 6
print('The following lines are answers to number 6')
for category in favs:
  thing = favs[category]
  print(category,thing)

#Problem 7
print('The following line is the answer to number 7')
fav_thing = sys.argv[1]
print(favs[fav_thing])

#Problem 8
#user_in = input('Hello, welcome to my list of favorite things. To view the categories, press the letter k')
#if user_in == 'k':
#  print(list(favs.keys()))

#Problem 9
print('The following line is the answer to number 9')
favs['organism'] = 'dog'
print(favs)

#Problem 10
print('The following is the answer to number 10')
fav_input = input('Please input a new valule for favorite thing')
favs[fav_thing] = fav_input
print(favs)



