# Rock-Paper-Scissors: Use dict for choices, loop 5 rounds with random (import random),track wins with set.

import random

choices = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
options = list(choices.keys())
player_wins = set()

for round_num in range(1, 6):
    computer = random.choice(options)
    player = random.choice(options) # Simulating player input
    
    print(f"Round {round_num}: Player ({player}) vs Computer ({computer})")
    
    if player == computer:
        print("Result: Tie")
    elif choices[player] == computer:
        print("Result: Player Wins!")
        player_wins.add(round_num)
    else:
        print("Result: Computer Wins")

print(f"\nTotal Wins: {len(player_wins)}")
print(f"Rounds won: {player_wins if player_wins else 'None'}")