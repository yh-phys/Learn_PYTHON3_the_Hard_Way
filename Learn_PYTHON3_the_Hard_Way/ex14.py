#!/usr/bin/env python3

from sys import argv

script, user_name = argv
promot = '> '

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(promot)

print(f"Where do you live {user_name}?")
lives = input(promot)

print("What kind of computer do you have?")
computer = input(promot)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice.
""")
