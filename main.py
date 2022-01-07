import PySimpleGUI as sg
   
def resetboard(board):
    for i in range(9):
        for j in range(9):
            board[i][j]=-1;

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

def printsudoku(board):
    print("  - - - - - - - - - - - - - -")
    for i in range(0,9):
        print(" | ",end="")
        for j in range(0,9):
            print(board[i][j],end=" ")
            if( (j+1)%3==0 ):
                print(" | ",end="")
        print()
        if( (i+1)%3==0):
            print("  - - - - - - - - - - - - - -")


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

sg.theme('BluePurple')
   
# input_rows = [[sg.Input(size=(5,1), pad=(1,1)) for col in range(9)] for row in range(9)]   

layout = [[sg.Text('Enter value of Sudoku cell here:'),
           sg.Text(size=(15,1), key='-OUTPUT-')],
          [[sg.Input(size=(5,1), pad= ( (1,1) if ( (col+1)%3!=0 & (row+1)%3!=0) else (8,8) ), key="{row}-{col}") for col in range(9)] for row in range(9)],
          [sg.Button('Solve'), sg.Button('Reset'),sg.Button('Exit')]]
  
window = sg.Window('Sudoku Solver', layout)
  
while True:
    event, values = window.read()
    # print(event, values)
      
    if event in  (None, 'Exit'):
        break
    elif event == 'Solve':
        for row in range(9):
            for col in range(9):
                # if( values["{row}-{col}"]!=""):
                    # board=int(values["{row}-{col}"])
                print( values["{row}-{col}"])
        if( solve( board,0,0)==False ):
            print("The Suduko board is not solvable")
        else:
            printsudoku(board)
    elif event=='Reset':
        resetboard(board);

window.close()




