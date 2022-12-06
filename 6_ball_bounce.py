# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
# it bounces back up to 3/5 the height it fell. 
# Write a program bounce.py that prints a table showing the height of the first 10 bounces.

import math

height = 100
num_bounce = 0

def only_number_bounce(height,num_bounce):
    while num_bounce < 11:
        height = round(height *3/5,4)                    # ball bounce back up to 3/5 the height it fell
        print(height)
        num_bounce += 1

def time_and_bounce(height,num_bounce):
    
    try:
        g = float(input('Input gravitational acceleration on Earth in meter pro seconds aquared(m/s2):\n'))
    except NameError as ne:
        print('Something went wrong')
        print(ne)
    except TypeError as tp:                               #value error if '' entered
        print('Please enter a proper value')
        print(tp)

    # h = 1/2 *g*t**(2)
    # t = math.sqrt(2*h/g)
    t1 = round(math.sqrt(2*height/g),4)
    print(f"The time the ball touch the ground for the first time is: {t1}")

    num_bounce_new = 2
    while num_bounce_new < 11:
        height = round(3/5 * height,4)
        t2 = round(math.sqrt(2*height/g),4)
        t1 = round(t1 + 2*t2,4)

        print(f"Time the ball touch the ground in the {num_bounce_new}th: {t1}")
        num_bounce_new += 1

prompt_1 = input("Do you want to only show the height of the next 11 bounces? Enter to skip\n")

if prompt_1:
    only_number_bounce(height,num_bounce)

prompt_2 = input("Count the time the ball touch the ground?: Enter to skip\n")

if prompt_2:
    time_and_bounce(height,num_bounce)