import random
import itertools as itt


cell=[" "," "," "," "," "," "," "," "," "," "]

def board():

    table= """
     1     2     3
  |-----|-----|-----|
A |  {}  |  {}  |  {}  |
  |-----|-----|-----|
B |  {}  |  {}  |  {}  |
  |-----|-----|-----|
C |  {}  |  {}  |  {}  |
  |-----|-----|-----|
"""
    print(table.format(cell[0], cell[1], cell[2], cell[3], cell[4], cell[5],cell[6], cell[7], cell[8]))

def Check_winner():
    combinations_row= [(0,1,2), (3,4,5), (6,7,8)]
    combinations_column= [(0,3,6), (1,4,7), (2,5,8)]
    combinations_diagonal = [(0,4,8), (3,4,6)]
    all_combinations= combinations_row + combinations_column + combinations_diagonal

    for j in all_combinations:
        checklist = []
        checklist2 = []
        for i in range(len(cell)):
            if cell[i] == "X":
                checklist.append(i)
            elif cell[i] == "O":
                checklist2.append(i)

    checklist_final = []
    for i in itt.combinations(checklist, 3):
        if i in all_combinations:
            print("Congrats you won !")
            exit()

    checklist_final = []
    for i in itt.combinations(checklist2, 3):
        if i in all_combinations:
            print("Sorry you lost !")
            exit()


def RunGame():

    board()
    Moves=["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    while len(Moves)>0:
        Translation={ "A1":0, "A2":1, "A3":2, "B1":3, "B2":4, "B3":5, "C1":6, "C2":7, "C3":8}
        my_move=input("Make your move ! Please enter the coordinates ! :  ").upper()
        try:
            if my_move in Moves:
                Moves.remove(my_move)
                coordinate=Translation[my_move]
                cell[coordinate]="X"
                board()
            else:
                print("It's out of the board ! Please retry !")
                raise IndexError
        except IndexError:
            RunGame()
        Check_winner()

        Dumb_computer=random.choice(Moves)
        Moves.remove(Dumb_computer)
        coordinate = Translation[Dumb_computer]
        cell[coordinate] = "O"
        board()



RunGame()




