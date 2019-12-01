import random

print("""
    A tictactoo Game that allow a person to play with computer. press q for left-top, w for top-center,
    e for right-top, a for left-center, s for center-center, d for right-center,
    z for left-bottom, x for center-bottom, c for right-bottom
""")

tictac_box = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']

tictac_already_select = []

abandom_tictac = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']

def DataEnteredPlayer():
    if x_player == "q":
        if tictac_box[0] != "O":
            tictac_box[0] = "X"
    if x_player == "w":
        if tictac_box[1] != "O":
            tictac_box[1] = "X"
    if x_player == "e":
        if tictac_box[2] != "O":
            tictac_box[2] = "X"
    if x_player == "a":
        if tictac_box[3] != "O":
            tictac_box[3] = "X"
    if x_player == "s":
        if tictac_box[4] != "O":
            tictac_box[4] = "X"
    if x_player == "d":
        if tictac_box[5] != "O":
            tictac_box[5] = "X"
    if x_player == "z":
        if tictac_box[6] != "O":
            tictac_box[6] = "X"
    if x_player == "x":
        if tictac_box[7] != "O":
            tictac_box[7] = "X"
    if x_player == "c":
        if tictac_box[8] != "O":
            tictac_box[8] = "X"
            
def DataEnteredEnemy():
    if computer_play == "q":
        if tictac_box[0] != "X":
            tictac_box[0] = "O"
    if computer_play == "w":
        if tictac_box[1] != "X":
            tictac_box[1] = "O"
    if computer_play == "e":
        if tictac_box[2] != "X":
            tictac_box[2] = "O"
    if computer_play == "a":
        if tictac_box[3] != "X":
            tictac_box[3] = "O"
    if computer_play == "s":
        if tictac_box[4] != "X":
            tictac_box[4] = "O"
    if computer_play == "d":
        if tictac_box[5] != "X":
            tictac_box[5] = "O"
    if computer_play == "z":
        if tictac_box[6] != "X":
            tictac_box[6] = "O"
    if computer_play == "x":
        if tictac_box[7] != "X":
            tictac_box[7] = "O"
    if computer_play == "c":
        if tictac_box[8] != "X":
            tictac_box[8] = "O"
            
counter = 0

player_winner = 0
enemy_winner = 0

def CalculateWinner():
    if tictac_box[0] == "X" and tictac_box[1] == "X" and tictac_box[2] == "X" or tictac_box[0] == "X" and tictac_box[3] == "X" and tictac_box[6] == "X" or tictac_box[0] == "X" and tictac_box[4] == "X" and tictac_box[8] == "X" or tictac_box[3] == "X" and tictac_box[4] == "X" and tictac_box[5] == "X" or tictac_box[1] == "X" and tictac_box[4] == "X" and tictac_box[7] == "X" or tictac_box[2] == "X" and tictac_box[5] == "X" and tictac_box[8] == "X" or tictac_box[6] == "X" and tictac_box[7] == "X" and tictac_box[8] == "X" or tictac_box[6] == "X" and tictac_box[4] == "X" and tictac_box[2] == "X":
        print("\nX wins the match\n")
        return True
    if tictac_box[0] == "O" and tictac_box[1] == "O" and tictac_box[2] == "O" or tictac_box[0] == "O" and tictac_box[3] == "O" and tictac_box[6] == "O" or tictac_box[0] == "O" and tictac_box[4] == "O" and tictac_box[8] == "O" or tictac_box[3] == "O" and tictac_box[4] == "O" and tictac_box[5] == "O" or tictac_box[1] == "O" and tictac_box[4] == "O" and tictac_box[7] == "O" or tictac_box[2] == "O" and tictac_box[5] == "O" and tictac_box[8] == "O" or tictac_box[6] == "O" and tictac_box[7] == "O" and tictac_box[8] == "O" or tictac_box[6] == "O" and tictac_box[4] == "O" and tictac_box[2] == "O":
        print("\nO wins the match\n")
        return True

def CalculateWinnerOrDraw():
    if tictac_box[0] == "X" and tictac_box[1] == "X" and tictac_box[2] == "X" or tictac_box[0] == "X" and tictac_box[3] == "X" and tictac_box[6] == "X" or tictac_box[0] == "X" and tictac_box[4] == "X" and tictac_box[8] == "X" or tictac_box[3] == "X" and tictac_box[4] == "X" and tictac_box[5] == "X" or tictac_box[1] == "X" and tictac_box[4] == "X" and tictac_box[7] == "X" or tictac_box[2] == "X" and tictac_box[5] == "X" and tictac_box[8] == "X" or tictac_box[6] == "X" and tictac_box[7] == "X" and tictac_box[8] == "X" or tictac_box[6] == "X" and tictac_box[4] == "X" and tictac_box[2] == "X":
        print("\nX wins the battle\n")
        return True
    elif tictac_box[0] == "O" and tictac_box[1] == "O" and tictac_box[2] == "O" or tictac_box[0] == "O" and tictac_box[3] == "O" and tictac_box[6] == "O" or tictac_box[0] == "O" and tictac_box[4] == "O" and tictac_box[8] == "O" or tictac_box[3] == "O" and tictac_box[4] == "O" and tictac_box[5] == "O" or tictac_box[1] == "O" and tictac_box[4] == "O" and tictac_box[7] == "O" or tictac_box[2] == "O" and tictac_box[5] == "O" and tictac_box[8] == "O" or tictac_box[6] == "O" and tictac_box[7] == "O" and tictac_box[8] == "O" or tictac_box[6] == "O" and tictac_box[4] == "O" and tictac_box[2] == "O":
        print("\nO wins the battle\n")
        return True
    else:
        print("\nDraw - Tie\n")

while True:
    print(tictac_box[0], "|", tictac_box[1], "|", tictac_box[2])
    print("--|---|----")
    print(tictac_box[3], "|", tictac_box[4], "|", tictac_box[5])
    print("--|---|----")
    print(tictac_box[6], "|", tictac_box[7], "|", tictac_box[8])
    counter += 1
    if counter == 1:
        if len(abandom_tictac) == 0:
            tictac_box = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
            tictac_already_select = []
            abandom_tictac = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
            CalculateWinnerOrDraw()
        else:
            x_player = input('\nEnter for X:')
            print("")
            if x_player not in tictac_already_select:
                if x_player in tictac_box:
                    if x_player in abandom_tictac:
                        abandom_tictac.remove(x_player)
                        tictac_already_select.append(x_player)
                        DataEnteredPlayer()
                        if CalculateWinner() == True:
                            tictac_box = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
                            tictac_already_select = []
                            abandom_tictac = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
                    else:
                        print("\nUsed Value\n")
                        counter = 0
                else:
                    print("\nYou can only type q, w, e, a, s, d, z, x, c\n")
                    counter = 0
            else:
                counter = 0
                print("\nTheir is already a value their\n")
    elif counter == 2:
        if len(abandom_tictac) == 0:
            tictac_box = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
            tictac_already_select = []
            abandom_tictac = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
            CalculateWinnerOrDraw()
            counter = 0
        else:
            computer_play = random.choice(abandom_tictac)
            print("\nComputer Played\n")
            tictac_already_select.append(computer_play)
            abandom_tictac.remove(computer_play)
            DataEnteredEnemy()
            if CalculateWinner() == True:
                tictac_box = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
                tictac_already_select = []
                abandom_tictac = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
            counter = 0
