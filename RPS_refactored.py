import random

R, P, S = 1, 2, 3
wording = {"R" : "Rock", "P" : "Paper", "S" : "Scissors"}
options = list("RPS")

print("Welcome to the game of Rock, Paper, Scissors...")

player1 = input("Hi Player! Please input your name: ").title().strip()

print("You are playing against the CPU!")
print("."*50)
print("To play the game, input 'r' for rock, 'p' for paper and 's' for scissors.")
print("="*50)
input("Press enter to continue: ")

while True:
    play1 = input(f"{player1}, input your choice ('r' for 'rock', 'p' for 'paper', 's' for scissors): ").strip().upper()
    
    if play1 in options:
        print(f"You picked {wording[play1]}!")
        pass
    else:
        print("Wrong selection made, replay!")
        print("."*50)
        continue
    
    computer = random.choice(options)
    print(f"CPU picked {wording[computer]}!")
    print("."*50)
    print(f"Player ({wording[play1]}) : CPU ({wording[computer]})")
    print("."*50)
    
    play1 = eval(play1)
    play2 = eval(computer)
    result = play1 - play2

    if result == 0:
        print("It's a tie! Replay!")
        continue
    elif abs(result) == 2:
        if result == 2:
            print("CPU wins!")
        else:
            print(f"You win!")
        break
    elif result >= 0:
        print(f"You win!")
        break
    else:
        print("CPU wins!")
        break
print("."*50)


