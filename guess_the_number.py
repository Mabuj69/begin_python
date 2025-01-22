import random

top_of_range = input("Type a number you want to play: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0.")
        quit()
    elif top_of_range <=10:
        chances = 5
    elif top_of_range <=100:
        chances = 7
    else:
        chances = 10
print(f"You have {chances} chances.")
random_number = random.randint(0, top_of_range)
guess = 0
while True:
    guess+=1
    if guess <= chances:
        user_guess = input(f"Guess a number between 0 and {top_of_range}: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess == random_number:
                print(f"You won in {guess} tries!")
                break  
            elif user_guess > random_number:
                print("You were above the number") 
            else:
                print("You were below the number")
        else:
            print("Please enter a number.")
            continue
    else:
        print(f"The number is {random_number}")
        print("You lost!")
        break
