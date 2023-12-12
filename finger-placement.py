import random
import time

# Import the my_notes.py file. Customize my_notes_example.py to change which notes you want to practice. You have to rename my_notes_example.py to my_notes.py for the applcation to work. 
import my_notes

notes = my_notes.notes

time_delay = int(input("What is the time delay that should be used in seconds? "))
iterations = int(input("How many iterations do you want to do? "))
iterator = 0

def display_random_item():
    random_item = random.choice(notes)
    return random_item

def timer(seconds):
    time.sleep(seconds)
counter = 0

while 5 > counter:
    counter += 1;   
    print(f"Starting in {5 - counter} seconds...")
    time.sleep(1)

while iterator < iterations:
    iterator += 1; 
    item = display_random_item()
    print(f"{iterator} {item}")
    timer(time_delay)
