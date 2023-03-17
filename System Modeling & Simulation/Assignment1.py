import random

player1_wins = 0
player2_wins = 0

for i in range(5):
    print(f"\nStep {i+1}:")
    while True:
        player1_roll = random.randint(1, 6)
        player2_roll = random.randint(1, 6)
        print(f"Player 1 rolls: {player1_roll}")
        print(f"Player 2 rolls: {player2_roll}")
        if player1_roll != player2_roll:
            if player1_roll > player2_roll:
                print("Player 1 wins!")
                player1_wins += 1
            else:
                print("Player 2 wins!")
                player2_wins += 1
            break
        else:
            print("Tie! Rolling again...")

if player1_wins > player2_wins:
    print("\nPlayer 1 is the winner!")
else:
    print("\nPlayer 2 is the winner!")
