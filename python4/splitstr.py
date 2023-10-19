#!/usr/bin/env python3

#Problem 2
taxa = ('sapiens,erectus,neanderthalensis')
print(taxa)
print(taxa[1]) #I get the letter a, since a in sapiens has the index of 1
print(type(taxa))

species = taxa.split(',')
print(species)
print(species[1]) #now I get erectus since this is now a list and has an index of 1
print(type(species))

print(sorted(species))

print(sorted(species, key=len))
