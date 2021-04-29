#task 1 solution
#fizz buzz problem
for num in range(1, 101):
    if num % 3 ==0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


#task 2
guesses_left = 3

import random
random_number= random.randint(0, 10)
while guesses_left >0:
    x = input("guess the number from 1-10: ")

    if guesses_left == x:
        print("you won")
        break
    else:
        print("that was wrong! try again")
        guesses_left = guesses_left-1
else:
    print("sorry you lose")