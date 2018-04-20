_columns = 256
_rows = 128

#_columns = 10
#_rows = 10

box_width = 4

size(1025, 512)
background(0)
fill(0)

board = [[0] * _rows] * _columns
next  = [[0] * _rows] * _columns

def render(_board):
    for i in range(len(_board)):
        for j in range(len(_board[i])):
            if _board[i][j] == 1:
                fill (255)
            elif _board[i][j] == 0:
                fill (0)
                
            rect(
                i * box_width, 
                j * box_width, 
                box_width,
                box_width
                )

for row in range (1, len(board) - 1):
    for column in range(1, len(board[row]) - 1):
        board[row][column] = int(random(2))
        
        if board[row][column] == 1:
            fill (255)
        elif board[row][column] == 0:
            fill (0)
                
            rect(
                column * box_width, 
                row * box_width, 
                box_width,
                box_width
                )

for row in range (1, len(board) - 1):
    for column in range(1, len(board[row]) - 1):
        
        neighbours = 0
        
        for i in range (-1, 1):
                for j in range (-1, 1):
                    neighbours += board[row + j][column + i]
                    
        neighbours -= board[row][column]
        
        if   board[row][column] == 1 and neighbours <  2: next[row][column] = 0
        elif board[row][column] == 1 and neighbours >  3: next[row][column] = 0
        elif board[row][column] == 0 and neighbours == 3: next[row][column] = 1
        else: next[row][column] = board[row][column]


board = next