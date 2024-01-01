import random
import numpy as np
from pandas import *
from pyray import *



windowWidth = 800
windowHeight = 800

rows,cols = (10,10)
choices = ['Red','Green','Blue']
currarr = np.zeros(shape=(rows,cols))
newarr = np.zeros(shape=(rows,cols))

#Define the initial conditions
vacant = 0.2 # 10% of the grid id vacant
sim_threshold = 0.3 #(1-Tau) the number of neighbours equal and below warrants a move
pop_split = 1 # 1:1 Equal population split, must implement further

def init_grid(currarr,newarr,rows,cols):
    currarr = np.zeros(shape=(rows,cols))
    newarr = np.zeros(shape=(rows,cols))
    return currarr,newarr

def set_vacant(currarr,newarr,vacant,rows,cols):
    empty_val = int(vacant * (rows * cols))
    for i in range(empty_val):
        r = random.randint(0,rows - 1)
        c = random.randint(0,cols - 1)

        if(currarr[r][c] == 0):
            currarr[r][c] = 5
        else:
            r = random.randint(0,rows - 1)
            c = random.randint(0,cols - 1)
            currarr[r][c] = 5

    newarr = currarr
    return currarr,newarr

def populate_grid(currarr,newarr):
    for j in range(cols):
        for i in range(rows):
            if(currarr[i][j] != 5):
                r = random.random()
                if(r >= 0.5):
                    currarr[i][j] = 1
                else:
                    currarr[i][j] = 2
    newarr = currarr
    return currarr,newarr

currarr,newarr = init_grid(currarr,newarr,rows,cols)
currarr,newarr = set_vacant(currarr,newarr,vacant,rows,cols)
currarr,newarr = populate_grid(currarr,newarr)
print(currarr)