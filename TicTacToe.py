import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

a = [" "," "," "]
b = [" "," "," "]
c = [" "," "," "]

board = [a,b,c]

def draw_board(rowall):
    print("   1 2 3 ")
    x = 0
    for i in rowall:
        line = "|"
        for j in i:
            if j == "x":
                line = line + "\u0332x"
            elif j == "o":
                line = line + "\u0332o"
            else:
                line = line + "\u0332 "
            line = line + "|"
        if x == 0: line = "a " + line
        if x == 1: line = "b " + line
        if x == 2: line = "c " + line

        x += 1
        print(line)

def get_input(p,t):
    
    while p not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3","exit"]:
        if t == "p1":
            p = input("player1: ")
        if t == "p2":
            p = input("player2: ")
    return p

def check_cell(cell):
    return eval(cell[0])[int(cell[1])-1] == " "

def check_win(rows):
    #Check horizontal rows
    i = 0
    for row in rows:
        # print(row)
        checkrow = ""
        for x in row: checkrow += x
        if checkrow == "xxx" or checkrow == "ooo":
            return "win"
        # print(check)
        i += 1
    #Check vertical columns
    for j in range(0,3):
        col = ""
        for y in range(0,3):
            col += rows[y][j]
        if col == "xxx" or col == "ooo":
            return "win"
    #Check diagonal
    diag = ""
    
    diag += rows[0][0]
    diag += rows[1][1]
    diag += rows[2][2]
    if diag == "xxx" or diag == "ooo":
        return "win"
    
    diag = ""
    diag += rows[0][2]
    diag += rows[1][1]
    diag += rows[2][0]
    if diag == "xxx" or diag == "ooo":
        return "win"
    
    # for row in rows:
       
    if not " " in rows[0] and not " " in rows[1] and not " " in rows[2]:
            return "stale"
        

pinput = ""
playing = True

allgood = ""

turn = "p1"

draw_board(board)

while True:
    if turn == "p1" and playing:
        
        pinput = get_input(pinput,turn)
            
        if pinput == "exit": playing = False; break
        
        if check_cell(pinput): 
            eval(pinput[0])[int(pinput[1])-1] = "x"
            allgood = True
        else:
            print("Already filled")
            allgood = False
    
        pinput = ""
        if allgood: 
            turn = "p2" 
            allgood = True
            cls()
        draw_board(board)
        if check_win(board) == "win": 
            playing = False
            print("Player 1 Wins!!")
            break
        elif check_win(board) == "stale":
            playing = False
            print("Stalemate");
            break
    
    elif turn == "p2" and playing:
        pinput = get_input(pinput,turn)
            
        if pinput == "exit": playing = False; break
        
        try:

            if check_cell(pinput): 
                eval(pinput[0])[int(pinput[1])-1] = "o"
                allgood = True
            else:
                # while eval(pinput[0])[int(pinput[1])-1] == "x" or eval(pinput[0])[int(pinput[1])-1] == "o":
                print("Already filled")
                allgood = False
        
        
        except Exception as e: print(e)
        
        pinput = ""
        if allgood: 
            turn = "p1" 
            allgood = True
            cls()
        draw_board(board)
        if check_win(board) == "win": 
            playing = False
            print("Player 2 Wins!!");
            break
        elif check_win(board) == "stale":
            playing = False
            print("Stalemate");
            break