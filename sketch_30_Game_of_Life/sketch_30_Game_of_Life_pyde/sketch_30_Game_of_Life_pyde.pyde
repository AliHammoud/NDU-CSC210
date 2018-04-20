import random
import copy

cell_w = 8
cell_h = 8

def init(empty = False):
    matrix = [
        [random.randint(0, 1)  if empty == False else 0 for n in range(cell_count_h)] 
        for m in range(cell_count_v)
    ]

    return matrix

def print_matrix(matrix):

    for column in range(len(matrix)):
        print(matrix[column])

        for row in range(len(matrix[column])):

            if matrix[row][column] == 1:
                fill(255)
            elif matrix[row][column] == 0:
                fill(0)

            rect(column * cell_w,
                 row * cell_h,
                 cell_w,
                 cell_h)

def count_neighbours(matrix, index):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            if matrix[index[0] + j][index[1] + i] == 1:
                count += 1

    if matrix[index[0]][index[1]] == 1:
        count -= 1

    return count

def generate(matrix):
    for column in range(1, len(matrix) - 1):
        for row in range(1, len(matrix[column]) - 1):
            if count_neighbours(matrix, (row, column)) == 3 and matrix[row][column] == 0:
                next[row][column] = 1
                
            elif count_neighbours(matrix, (row, column)) < 2 and matrix[row][column] == 1:
                next[row][column] = 0
            
            elif count_neighbours(matrix, (row, column)) > 2 and matrix[row][column] == 1:
                next[row][column] = 0
            else:
                next[row][column] = board[row][column]

def setup():
    size(257, 257)
    background(0)
    
    global cell_w, cell_h, cell_count_h, cell_count_v, board, next
    
    cell_count_h = width / cell_w
    cell_count_v = height / cell_h
    
    board = init()
    next = init(True)
    
    generate(board)
    print('')
    board = copy.deepcopy(next)
    print_matrix(next)
    
    generate(board)
    print('')
    board = copy.deepcopy(next)
    print_matrix(next)
    
    generate(board)
    print('')
    board = copy.deepcopy(next)
    print_matrix(next)
    
def draw():
    pass