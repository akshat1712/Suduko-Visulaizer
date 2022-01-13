from PySimpleGUI import PySimpleGUI

# Importing PySimpleGUI as sg for UI & UX
import PySimpleGUI as sg

# Functions to perform specific tasks like solving,reseting etc.
 
def resetboard(board,window):
    for i in range(9):
        for j in range(9):
            board[i][j]=-1;
            window["-{}-{}-".format(i,j)].update("")

def check_column( board, y,val):
    for i in range(9):
        if( board[i][y]==val):
            return False
    return True

def check_row( board,x,val):
    for i in range(9):
        if( board[x][i]==val):
            return False
    return True

def check_subgrid(board,val,x,y):
    x-=x%3
    y-=y%3
    for i in range(3):
        for j in range(3):
            if( board[x+i][y+j]==val):
                return False
    return True

def printsudoku(board,window):
    print("  - - - - - - - - - - - - - -")
    for i in range(0,9):
        print(" | ",end="")
        for j in range(0,9):
            window["-{}-{}-".format(i,j)].update(str( board[i][j]))
            print(board[i][j],end=" ")
            if( (j+1)%3==0 ):
                print(" | ",end="")
        print()
        if( (i+1)%3==0):
            print("  - - - - - - - - - - - - - -")

def get_color(row,col):
    if(  (row<=3 or row>6 ) and ( col<=3 or col>6 ) ):
        return "#760000"
    elif ( ( row>3 and row<=6 ) and ( col>3 and col<=6)):
        return "#760000"
    else :
        return "#001670"
    
# Using Backtracking algorithm to solve the Sudoku problem

def solve( board,x,y):
    if( x==9):
        x=0
        y+=1
    if(y==9):
        return True
    if( board[x][y]!=-1):
        return solve(board,x+1,y)
    for i in range(1,10):
        if( check_column(board,y,i) & check_row(board,x,i) & check_subgrid(board,i,x,y)):
            board[x][y]=i;
            if( solve(board,x+1,y)==True):
                return True
            board[x][y]=-1
    return False

# -1 in the board means that place is empty and we can make a sudoku puzzle by replacing sudoku puzzle by replacing -1 with 1-9 
board =[
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1]
]

sg.theme("DarkTeal8")
layout = [[sg.Text('Enter value of Sudoku cell here:'),
           sg.Text(size=(15,1), key='-OUTPUT-')],
          [[sg.Input(size=(5,45), pad= ( 4,4 ), key="-{}-{}-".format(row,col), background_color=get_color(row+1,col+1)) for col in range(9)] for row in range(9)],
          [sg.Button('Solve'), sg.Button('Reset'),sg.Button('Exit')]]
  
window = sg.Window('Sudoku Solver', layout)
  
while True:
    event, values = window.read()
    if event =="Exit" or event==sg.WIN_CLOSED:
        break
    elif event == 'Solve':
        for row in range(9):
            for col in range(9):
                if( values["-{}-{}-".format(row,col)]!=""):
                    board[row][col]=int(values["-{}-{}-".format(row,col)])
        if( solve( board,0,0)==False ):
            print("The Suduko board is not solvable")
        else:
            printsudoku(board,window)
    elif event=='Reset':
        resetboard(board,window);

window.close()