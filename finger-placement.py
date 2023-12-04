import random
import time

notes = [
    "Low - G",
    "Low - A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "High - G",
    "High - A"
]

def display_random_item():
    random_item = random.choice(notes)
    print(random_item)

def timer(seconds):
    time.sleep(seconds)

while True:
    display_random_item()
    timer(1)
