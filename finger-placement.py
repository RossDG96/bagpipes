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

time_delay = int(input("What is the time delay that should be used in seconds? "))
iterations = int(input("How many iterations do you want to do? "))
iterator = 0

def display_random_item():
    random_item = random.choice(notes)
    print(random_item)

def timer(seconds):
    time.sleep(seconds)

while iterator < iterations:
    iterator += 1; 
    display_random_item()
    timer(time_delay)
