import random

def play_game():
    name = str(input("Enter Your Name :"))
    print(" ------>  Rules for the Game  <-------\n\n")
    print(f"Welcome ! {name} to Number Guessing Game\n")
    print("\n1. Enter your guess numbers from 1 to 100 ")
    print("\n2. If your entered number is greater than random generated number , you will get a message 'Too High'  ")
    print("\n3. If your entered number is less than random generated number , you will get a message 'Too Low '    ")
    print("\n4. If matches you will get a message 'You Won' ")
    print("\n5. You will have 10 chances only\n")

    random_no=random.randint(1,100)

    i=0
    while i<10:

        num=int(input("Guess the number :"))
        if num==random_no:
            print("You Won the Game.... ")
            break
        elif num>random_no:
            print(" Too High ....")
        elif num<random_no:

            print(" Too Low ....")

    print("Guess Again ")
    i+=1

    print(random_no)

repeat=str('y')
while repeat=='y':
    play_game()
    repeat=str(input("Do You want to try again ...(Y/N)")).lower()

print("Exited ....")
exit()
