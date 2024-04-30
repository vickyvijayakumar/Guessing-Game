import random
def main():
    print("Welcome to the Number Guessing Game")
    print("...................................")

    target_number= random.randint(1,100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100:"))
        attempts +- 1

        if guess < target_number:
            print("Too Low ! Try Again.")
        elif guess > target_number:
            print("Too High ! Try Again.")
        else:
            print(f"Congratulations ! You Guessed the number {target_number} correctly in {attempts} attempt.s")
            break
if __name__ =="__main__":
    main()
