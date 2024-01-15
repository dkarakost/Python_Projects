#we declare a 2D list
tictactoe = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]
#Desing the output of the board
print("_______")
print("|" + tictactoe[0][0] + "|" + tictactoe[0][1] + "|" + tictactoe[0][2] + "|")
print("+-+-+-+")
print("|" + tictactoe[1][0] + "|" + tictactoe[1][1] + "|" + tictactoe[1][2] + "|")
print("+-+-+-+")
print("|" + tictactoe[2][0] + "|" + tictactoe[2][1] + "|" + tictactoe[2][2] + "|")
print("-------")

times = 0
while times < 9:
    player1 = int(input("Player 1 plays please choose a box: "))
    times += 1 
    
    if player1 == 1:
        row = 0
        column = 0
    elif player1 == 2 :
        row = 0 
        column = 1
    elif player1 == 3 :
        row = 0 
        column = 2
    elif player1 == 4 :
        row = 1
        column = 0
    elif player1 == 5 :
        row = 1
        column = 1
    elif player1 == 6 :
        row = 1 
        column = 2
    elif player1 == 7 :
        row = 2 
        column = 0
    elif player1 == 8 :
        row = 2 
        column = 1
    elif player1 == 9 :
        row = 2 
        column = 2
    if tictactoe[row][column] == " ":
        tictactoe[row][column] = "O"
        print("_______")
        print("|" + tictactoe[0][0] + "|" + tictactoe[0][1] + "|" + tictactoe[0][2] + "|")
        print("+-+-+-+")
        print("|" + tictactoe[1][0] + "|" + tictactoe[1][1] + "|" + tictactoe[1][2] + "|")
        print("+-+-+-+")
        print("|" + tictactoe[2][0] + "|" + tictactoe[2][1] + "|" + tictactoe[2][2] + "|")
        print("-------")
        
        if tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O":
            print("Player 1 has won!")
            quit()
        elif tictactoe[1][0] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O":
            print("Player 1 has won!")
            quit()
        elif tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O":
            print("Player 1 has won!")
            quit()
        elif tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O":
            print("Player 1 has won!")
            quit()
        elif tictactoe[0][1] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O":
            print("Player 1 has won!")
            quit()
        elif tictactoe[0][2] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O":
            print("Player 1 has won!")
            quit()
        elif tictactoe[0][0] == "O" and tictactoe[1][1] == "O" and tictactoe[2][2] == "O":
            print("Player 1 has won!")
            quit()
        elif tictactoe[0][2] == "O" and tictactoe[1][1] == "O" and tictactoe[2][0] == "O":
            print("Player 1 has won!")
            quit()
    elif tictactoe[row][column] != " ":
        print("Try a different one!")
        times -= 1
        continue
    if times == 9:
        break
    while times<9:
        player2 = int(input("Player 2 plays, please choose a box."))
        times += 1
        if player2 == 1:
            row = 0
            column = 0
        elif player2 == 2:
            row = 0
            column = 1
        elif player2 == 3:
            row = 0
            column = 2
        elif player2 == 4:
            row = 1
            column = 0
        elif player2 == 5:
            row = 1
            column = 1
        elif player2 == 6:
            row = 1
            column = 2
        elif player2 == 7:
            row = 2
            column = 0
        elif player2 == 8:
            row = 2
            column = 1
        elif player2 == 9:
            row = 2
            column = 2
            
        if tictactoe[row][column] ==" ":
            tictactoe[row][column] ="X"
            
            print("_______")
            print("|" + tictactoe[0][0] + "|" + tictactoe[0][1] + "|" + tictactoe[0][2] + "|")
            print("+-+-+-+")
            print("|" + tictactoe[1][0] + "|" + tictactoe[1][1] + "|" + tictactoe[1][2] + "|")
            print("+-+-+-+")
            print("|" + tictactoe[2][0] + "|" + tictactoe[2][1] + "|" + tictactoe[2][2] + "|")
            print("-------")
            
            if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
                print("Player 2 has won!")
                quit()
            elif tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
                print("Player 2 has won!")
                quit()
            elif tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X":
                print("Player 2 has won!")
                quit()
            elif tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X":
                print("Player 2 has won!")
                quit()
            elif tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
                print("Player 2 has won!")
                quit()
            elif tictactoe[0][2] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X":
                print("Player 2 has won!")
                quit()
            elif tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X":
                print("Player 2 has won!")
                quit()
            elif tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X":
                print("Player 2 has won!")
                quit()
            break
        elif tictactoe[row][column] != " ":
            print("Try a different one!")
            times -= 1
            continue
        
print("It's a draw")
