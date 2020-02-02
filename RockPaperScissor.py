import random
choices = ['r', 'p', 's']

winner = None
pl_pnt = 0
cmp_pnt = 0


def show_pnts():
    print(f"\n\nYour points:    {pl_pnt}")
    print(f"System points:  {cmp_pnt}\n\n")


def is_winner():
    global winner
    if pl_pnt == 5:
        winner = True
        return True
    elif cmp_pnt == 5:
        winner = False
        return True
    else:
        return False


def pnts_upd():
    if your_ch != comp_ch:
        global cmp_pnt
        global pl_pnt
        if your_ch == 'r' and comp_ch == 'p':
            cmp_pnt += 1
        elif your_ch == 'r' and comp_ch == 's':
            pl_pnt += 1
        elif your_ch == 's' and comp_ch == 'r':
            cmp_pnt += 1
        elif your_ch == 's' and comp_ch == 'p':
            pl_pnt += 1
        elif your_ch == 'p' and comp_ch == 's':
            cmp_pnt += 1
        else:
            pl_pnt += 1
    show_pnts()


while True:
    your_ch = input("Rock Paper Scissor? (r/p/s) : ")
    if your_ch not in choices:
        print("Invalid Choice!!\n\n")
        continue
    your_ch.lower()
    comp_ch = random.choice(choices)
    print(f"\n\nYour choice:   {your_ch}")
    print(f"\n\nSystem choice: {comp_ch}")

    pnts_upd()
    if is_winner():
        print("\n\nGAME OVER !!\n")
        if winner:
            print("You Win!!\n\n")
        else:
            print("You Lose!!\n\n")
        break
