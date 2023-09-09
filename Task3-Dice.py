import random

def roll_dice(n):
    print(f"\nRolling {n}  dices .......")
    i=0
    while i<n:
        random_no=random.randint(1,6)
        print(random_no," ",end="")
        i+=1

num=1
while num==1:
    print("\t\t Dice Roller Game")
    print("\t\t.....................\n\n")
    n = int(input("Enter the number of dice you want to roll : "))
    roll_dice(n)

    num=int(input("\n\n--- Press 1 to replay and 0 to exit . ---"))
    if num==1:
        continue
    else:
        print("\n Game Exited .....")
        break
