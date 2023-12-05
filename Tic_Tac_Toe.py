# PROGRAM TO CREATE A TIC-TAC-TOE GAME

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n\n\t\t\t\t\t||LET'S PLAY TIC-TAC-TOE||")
print("\t\t\t\t\t==========================\n")

print("Player 1 , Please enter your name")  # TAKING PLAYERS NAME
p1 = input()
print("Player 3 , Please enter your name")
p2 = input()
print("\n\n", p1, " will play with 'X'", sep='')  # ASSIGNING PLAYERS THEIR RESPECTIVE VALUES
print(p2, "will play with 'O'\n---------------------\n")


def show_matrix():                                  # TO DISPLAY THE 3*3 MATRIX
    i = 0
    while i < len(matrix):
        if i == 2 or i == 5 or i == 8:
            print(matrix[i])
        else:
            print(matrix[i], end="   ")
        i += 1


show_matrix()


def check_result():                                     # TO CHECK THE WINNER OF THE GAME
    while True:                                                         # RETURNS TRUE IF VALID COMBINATIONS ARE FOUND
        if matrix[0] == matrix[1] and matrix[1] == matrix[2]:
            return True
        elif matrix[3] == matrix[4] and matrix[4] == matrix[5]:
            return True
        elif matrix[6] == matrix[7] and matrix[7] == matrix[8]:
            return True
        elif matrix[0] == matrix[3] and matrix[3] == matrix[6]:
            return True
        elif matrix[1] == matrix[4] and matrix[4] == matrix[7]:
            return True
        elif matrix[2] == matrix[5] and matrix[5] == matrix[8]:
            return True
        elif matrix[0] == matrix[4] and matrix[4] == matrix[8]:
            return True
        elif matrix[2] == matrix[4] and matrix[4] == matrix[6]:
            return True
        else:
            return False                            # RETURN FALSE IF NO VALID COMBINATIONS ARE FOUND


chances = 1
while chances < 10:
    print("\n", p1, " Enter the box number", sep='')
    b1 = int(input())                       # TAKING INPUT FROM 1st THE USER

    if b1 != 'X' or b1 != 'O':
        matrix[b1 - 1] = 'X'                # PUTTING THE VALUE IN THE GIVEN BOX
        show_matrix()                       # DISPLAYS THE MATRIX AFTER A TURN
        chances += 1
        if check_result():                 # CALLS TO check_result() function to check if player has won the game or not
            print("\n||", p1, "is the winner ||")
            break
    if chances == 10:        # TOTAL NUMBER OF CHANCES
        print("\n\n||MATCH DRAWN||\n-------------")
        print("FINAL MATRIX\n-------------")
        show_matrix()  # DISPLAYS THE MATRIX IF THE MATCH IS DRAWN
        break

    print("\n", p2, " Enter the box number", sep='')             # TAKING INPUT FROM THE 2nd USER
    b2 = int(input())

    if b2 != 'X' or b2 != 'O':
        matrix[b2 - 1] = 'O'                                # PUTTING THE VALUE IN THE GIVEN BOX
        show_matrix()                                       # DISPLAYS THE MATRIX AFTER A TURN
        chances += 1
        if check_result():                 # CALLS TO check_result() function to check if player has won the game or not
            print("\n||", p2, "is the winner ||")
            break
