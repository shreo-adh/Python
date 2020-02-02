choices = []
left = 9
for i in range(0, 9):
    choices.append(str(i+1))


def print_board():
    print(f"\n\n\t\t {choices[0]} | {choices[1]} | {choices[2]}")
    print("\t\t _________")
    print(f"\t\t {choices[3]} | {choices[4]} | {choices[5]}")
    print("\t\t _________")
    print(f"\t\t {choices[6]} | {choices[7]} | {choices[8]}")
    print("\n\n")


def check_left_diag():
    if choices[0] == choices[4] and choices[0] == choices[8]:
        return True
    return False


def check_right_diag():
    if choices[4] == choices[6] and choices[4] == choices[2]:
        return True
    return False


def check_row():
    for i in range(0, 3):
        y = i*3
        if choices[y] == choices[y+1] and choices[y] == choices[y+2]:
            return True
    return False


def check_column():
    for i in range(0, 3):
        if choices[i] == choices[i+3] and choices[i] == choices[i+6]:
            return True
    return False


def is_winner():
    if check_left_diag() or check_right_diag() or check_row() or check_column():
        return True
    else:
        return False


p1_turn = True
winner = False

while not winner:
    print_board()
    if p1_turn:
        print("Player 1 :")
    else:
        print("Player 2 :")

    try:
        ch = int(input("Enter your choice : "))
        if choices[ch-1] == 'X' or choices[ch-1] == 'O':
            print("\n\nPosition chosen is already filled !! \n\n")
            continue
        else:
            choices[ch-1] = "X" if p1_turn else "O"
            left -= 1
    except:
        print("Enter valid value of position!! \n\n")
        continue

    win = is_winner()
    if win:
        if p1_turn:
            print("\n\nGame Over !! \n\n Player 1 wins!! ")
        else:
            print("\n\nGame Over !! \n\n Player 2 wins!! ")
        winner = True

    if left == 0 and winner==False:
        print("Game Over !! \n\n It's a Draw!!")
        winner = True

    if winner:
        print_board()
    else:
        p1_turn = not (p1_turn)
