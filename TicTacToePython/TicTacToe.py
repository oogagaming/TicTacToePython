from time import sleep
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

a = [" "," "," "]
b = [" "," "," "]
c = [" "," "," "]

board = [a,b,c]

def draw_board(rowall):
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

# def check_win(rows):
#     for i in rows:
#         print(rows[i])
        # if rows[i] == ["x","x","x"]:
        #     print("win")
        # elif rows[i] == ["o","o","o"]:
        #     print("win")

pinput = ""
playing = True

allgood = ""

turn = "p1"

while playing:
    if turn == "p1":
        
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
        # check_win(board)
    
    elif turn == "p2":
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