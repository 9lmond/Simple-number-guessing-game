import random

num = random.randint(0, 15)

tries=0
max_tries=3
guess=None

print(f"Your goal is to guess a number from 0-15 in {max_tries} attempts.")

while guess != num:
    try:
        guess = int(input(f"Your Guess(0-15): "))
        tries += 1

        if guess == num:
            print("Correct!!")
            break
        elif guess > num:
            print("too high! Try a lower number.")
        else:
            print("too low! Try a higher number.")

        remaining_attempts = max_tries - tries
        if remaining_attempts > 0:
            print(f"{remaining_attempts} attempt(s) left.")
        else:
            print("Womp Womp Womp, you lose!. The correct answer was", num)
            break
    except ValueError:
        print("Please enter a valid integer.")
