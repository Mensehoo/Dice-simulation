import random

def dice_simulation():
    print("Welcome to the dice throwing simulation!")
    
    while True:
        roll = input("Type 'y' to roll the dice or 'n' to exit: ").lower()
        
        if roll == 'y':
            dice_result = random.randint(1, 6)
            print(f"You got a number: {dice_result}")
        elif roll == 'n':
            print("Thank you for using the dice simulation. See you later.!")
            break
        else:
            print("Invalid input. Please type 'y' to roll the dice or 'n' to exit.")

dice_simulation()
