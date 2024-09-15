import numpy as np
grid = [
    [0,0,0,6,0,4,0,0,0],
    [0,3,0,0,0,0,2,0,0],
    [5,0,6,0,1,0,0,0,0],
    [0,2,0,7,0,0,5,4,0],
    [0,0,0,4,3,0,6,0,0],
    [0,0,0,0,0,0,0,0,0],
    [8,0,5,0,0,0,0,1,0],
    [0,4,3,0,0,5,0,0,0],
    [0,0,1,0,6,0,0,0,2]
]
def possible(x, y, n):
    for i in range (9):
        if grid[i][x] == n and i != y:
            return False
    for i in range (9):
        if grid[y][i] == n and i != x:
            return False
        
    x0 = (x//3)*3
    y0 = (y//3)*3
    for Y in range (y0, y0 + 3):
        for X in range (x0, x0 + 3):
            if grid[Y][X]== n:
                return False
    return True

def Print(matrix):
    for i in range (9):
        print(matrix[i])

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]== 0:
                for n in range(1,10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(np.matrix(grid))
    input("More?")

solve()
