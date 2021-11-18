from random import randint

from blessed import Terminal

from time import sleep

generated_number = randint(0, 100)

choices = []

stop = False

term = Terminal()

while not stop:

    choice = int(input('Enter your choice: '))

    stop = False

    if 0 > choice > 100:

        print('Out of Bounds')
        continue

    elif choice == generated_number:

        stop = True

    elif len(choices)==0:

        if 0 <= abs(choice - generated_number) <= 10:

            print('Warm')

        else:

            print('Cold')

    elif choice in choices:

        print("Number already entered")
        continue

    else:
        if abs(choice - generated_number) > abs(choices[len(choices)-1] - generated_number):

            print('Colder')
            print(choices)

        elif abs(choice - generated_number) == abs(choices[len(choices)-1] - generated_number):

            print('Same')
            print(choices)

        else:

            print('Warmer')
            print(choices)

    choices.append(choice)

print(f'You won the game it took you {len(choices)} guesses.😃😄😎')

sleep(5)