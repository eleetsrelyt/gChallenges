## Heads vs Tails

import random

print("Let's flip a coin.")
count = 0
while count <= 0:
    count = round(float(input("How many times do you want to flip?")),0)

i = 0
h = 0
t = 0
while i < count:
    flip = random.choice('ab')
    if flip == 'a':
        print("heads")
        h = h + 1
    else:
        print("tails")
        t = t + 1
    i = i + 1

p = round((h / count) * 100,2)

print("You flipped heads",p,"percent of the time")
