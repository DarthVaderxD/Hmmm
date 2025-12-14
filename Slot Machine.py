import random
elements=["🍉","🍒","🔔","⭐"]


def machine(sui, xd):
        slot1=random.choice(elements)
        slot2=random.choice(elements)
        slot3=random.choice(elements)
        if slot1==slot2==slot3:
            print(f"{slot1} | {slot2} | {slot3}")
            return xd+2*sui
        else:
            print(f"{slot1} | {slot2} | {slot3}")
            return xd-sui
                


def game():
    balance=100
    print("--------------------------")
    print("Welcome to Python Slots")
    print("Symbols: 🍉 🍒 🔔 ⭐")
    print("--------------------------")
    print(f"Current balance: ₹{balance}")
    def machines(balance):
        lol=int(input("Enter your bet amount: "))
        print("Spinning")
        a=machine(lol, balance)
        if a-balance>lol:
            print("You win")
            print(f"Balance : ₹{a}")
            sui=input("Wanna try again (Y/N): ")
            sui=sui.upper() 
            if sui=="Y":
                machines(a)
            else:
                print("Thanks for playing")
                exit()
        elif balance == 0:
            print("You lost")
            print(f"Balance : ₹{a}")
            print("You dont have money left. Please play again when you have some money")
            exit()
        elif balance<0:
            print(f"Balance : ₹{a}")
            print(f"You are under debt. You have to pay ₹{-a} or else cops are incoming.")
        else:
            print("You lost")
            print(f"Balance : ₹{a}")
            sui=input("Wanna try again (Y/N): ")
            sui=sui.upper() 
            if sui=="Y":
                machines(a)
            else:
                print("Thanks for playing")
                exit()
    machines(balance)
    
    
game()


