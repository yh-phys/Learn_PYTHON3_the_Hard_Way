#!/usr/bin/env python3

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"These who know {binary} and these who {do_not}."

print(x)
print(y)
print(f"I sad: {x}")
print(f"I also sad: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)