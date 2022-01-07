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
    [5,3,-1,-1,7,-1,-1,-1,-1],
    [6,-1,-1,1,9,5,-1,-1,-1],
    [-1,9,8,-1,-1,-1,-1,6,-1],
    [8,-1,-1,-1,6,-1,-1,-1,3],
    [4,-1,-1,8,-1,3,-1,-1,1],
    [7,-1,-1,-1,2,-1,-1,-1,6],
    [-1,6,-1,-1,-1,-1,2,8,-1],
    [-1,-1,-1,4,1,9,-1,-1,5],
    [-1,-1,-1,-1,8,-1,-1,7,9]
]

if( solve( board,0,0)==False ):
    print("The Suduko board is not solvable")
else:
    printsudoku(board)
