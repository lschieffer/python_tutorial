"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print "Welcome to madlibs, we will need a few things from you to get started.  Please provide us with:"

name = raw_input("name: ")
a1 = raw_input("adjective: ")
a2 = raw_input("adjective: ")
animal = raw_input("animal: ")
food = raw_input("food: ")
v1 = raw_input("verb: ")
n1 = raw_input("noun: ")
fruit = raw_input("fruit: ")
a3 = raw_input("adjective: ")
superhero = raw_input("superhero: ")
country = raw_input("country: ")
dessert = raw_input("dessert: ")
year = raw_input("year: ")
s2 = raw_input("noun: ")

print "ok, are you ready for your story?"

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print STORY % name, a1, a2, animal, food, v1, n1, fruit, a3, name, superhero, name, country, name, dessert, name, year, s2



