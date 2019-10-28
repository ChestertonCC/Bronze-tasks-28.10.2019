import random

jumble = input("Write a random word: ")

j = list(jumble)
random.shuffle(j)

print("".join(j))
