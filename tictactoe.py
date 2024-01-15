#we declare a 2D list
triliza = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]
#Desing the output of the board
print("_______")
print("|" + triliza[0][0] + "|" + triliza[0][1] + "|" + triliza[0][2] + "|")
print("+-+-+-+")
print("|" + triliza[1][0] + "|" + triliza[1][1] + "|" + triliza[1][2] + "|")
print("+-+-+-+")
print("|" + triliza[2][0] + "|" + triliza[2][1] + "|" + triliza[2][2] + "|")
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
    if triliza[row][column] == " ":
        triliza[row][column] = "O"
        print("_______")
        print("|" + triliza[0][0] + "|" + triliza[0][1] + "|" + triliza[0][2] + "|")
        print("+-+-+-+")
        print("|" + triliza[1][0] + "|" + triliza[1][1] + "|" + triliza[1][2] + "|")
        print("+-+-+-+")
        print("|" + triliza[2][0] + "|" + triliza[2][1] + "|" + triliza[2][2] + "|")
        print("-------")
        
        if triliza[0][0] == "O" and triliza[0][1] == "O" and triliza[0][2] == "O":
            print("Player 1 has won!")
            quit()
        elif triliza[1][0] == "O" and triliza[1][1] == "O" and triliza[1][2] == "O":
            print("Player 1 has won!")
            quit()
        elif triliza[2][0] == "O" and triliza[2][1] == "O" and triliza[2][2] == "O":
            print("Player 1 has won!")
            quit()
        elif triliza[0][0] == "O" and triliza[1][0] == "O" and triliza[2][0] == "O":
            print("Player 1 has won!")
            quit()
        elif triliza[0][1] == "O" and triliza[1][1] == "O" and triliza[1][2] == "O":
            print("Player 1 has won!")
            quit()
        elif triliza[0][2] == "O" and triliza[2][1] == "O" and triliza[2][2] == "O":
            print("Player 1 has won!")
            quit()
        elif triliza[0][0] == "O" and triliza[1][1] == "O" and triliza[2][2] == "O":
            print("Player 1 has won!")
            quit()
        elif triliza[0][2] == "O" and triliza[1][1] == "O" and triliza[2][0] == "O":
            print("Player 1 has won!")
            quit()
    elif triliza[row][column] != " ":
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
            
        if triliza[row][column] ==" ":
            triliza[row][column] ="X"
            
            print("_______")
            print("|" + triliza[0][0] + "|" + triliza[0][1] + "|" + triliza[0][2] + "|")
            print("+-+-+-+")
            print("|" + triliza[1][0] + "|" + triliza[1][1] + "|" + triliza[1][2] + "|")
            print("+-+-+-+")
            print("|" + triliza[2][0] + "|" + triliza[2][1] + "|" + triliza[2][2] + "|")
            print("-------")
            
            if triliza[0][0] == "X" and triliza[0][1] == "X" and triliza[0][2] == "X":
                print("Player 2 has won!")
                quit()
            elif triliza[1][0] == "X" and triliza[1][1] == "X" and triliza[1][2] == "X":
                print("Player 2 has won!")
                quit()
            elif triliza[2][0] == "X" and triliza[2][1] == "X" and triliza[2][2] == "X":
                print("Player 2 has won!")
                quit()
            elif triliza[0][0] == "X" and triliza[1][0] == "X" and triliza[2][0] == "X":
                print("Player 2 has won!")
                quit()
            elif triliza[0][1] == "X" and triliza[1][1] == "X" and triliza[1][2] == "X":
                print("Player 2 has won!")
                quit()
            elif triliza[0][2] == "X" and triliza[2][1] == "X" and triliza[2][2] == "X":
                print("Player 2 has won!")
                quit()
            elif triliza[0][0] == "X" and triliza[1][1] == "X" and triliza[2][2] == "X":
                print("Player 2 has won!")
                quit()
            elif triliza[0][2] == "X" and triliza[1][1] == "X" and triliza[2][0] == "X":
                print("Player 2 has won!")
                quit()
            break
        elif triliza[row][column] != " ":
            print("Try a different one!")
            times -= 1
            continue
        
print("It's a draw")
