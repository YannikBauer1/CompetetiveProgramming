# The matrix to be tested
# M = [[3,5,5],[2,5,2],[1,3,4]]
# M = [[5,1,1],['-','-',1],['-','-',1]]
# M = [[5,2,3],[6,4,1],[2,1,3]]
# M = [[5,5,5],[5,5,5],[5,5,5]]
# M = [[5,1,1],[2,4,1],[1,2,3]]
# M = [[6,1,1],[3,5,5],[10,7,3]]
# M = [[1,2,3,4,5],[6,7,8,9,10],[7,2,3,5,9]]
# M = [[2,4,6,1,7],[5,3,4,5,1]]
# M = [[1,10,6],[5,8,4],[1,6,9],[9,9,4]]

import numpy as np
import time

np.random.seed(0)
M = np.random.randint(900, size=(30, 30)).tolist()

h = len(M)
w = len(M[0])

import time

t = time.time()


def neighbors(x, y):
    '''Obtain the neighbors of a point in a matrix'''

    neighbor = [(i, j) for j in range(y - 1, y + 2) for i in
                range(x - 1, x + 2)]
    neighbor.remove((x, y))

    return [point for point in neighbor if
            0 <= point[0] <= h - 1 and 0 <= point[1] <= w - 1 and abs(
                point[0] - x) + abs(point[1] - y) <= 1]


neighbor = dict()

for i in range(h):
    for j in range(w):
        neighbor[(i, j)] = neighbors(i, j)


def maximum_value_matrix(M):
    ''' get the max value of the list M'''

    m = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != '-':
                if M[i][j] > m:
                    m = M[i][j]
    return m


def get_coordinates_attack(M, value):
    ''' get the coordinates from matrix M whose value is equal to p'''

    return [(i, j) for j in range(len(M[0])) for i in range(len(M)) if
            M[i][j] == value]


def minimum_value_matrix_from_point(defender):
    ''' get the min value of the list M'''

    m = 1001
    for coord in defender:
        if M[coord[0]][coord[1]] != '-':
            if M[coord[0]][coord[1]] < m:
                m = M[coord[0]][coord[1]]

    return m


def get_coordinates(M, value):
    ''' get the coordinates of the weaker defenders'''

    return [point for point in defender if M[point[0]][point[1]] == value]


def soma(M):
    s = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != '-':
                s += M[i][j]
    return s


# register the original positions
kingdom_positions = dict()

for i in range(h):
    for j in range(w):
        kingdom_positions[(i, j)] = [(i, j)]

new_M = [value for value in M]

while soma(new_M) != 1:
    coord = get_coordinates_attack(M, maximum_value_matrix(M))
    attacker = sorted(coord)[0]

    defender = neighbor[attacker]
    coord = sorted(
        get_coordinates(M, minimum_value_matrix_from_point(defender)))

    if minimum_value_matrix_from_point(defender) == maximum_value_matrix(M):
        defender = sorted(coord)[0]
        new_M[attacker[0]][attacker[1]] = '-'
        new_M[defender[0]][defender[1]] = '-'
        kingdom_positions.pop(defender)
        kingdom_positions.pop(attacker)

    elif coord == []:
        new_M[attacker[0]][attacker[1]] = new_M[attacker[0]][attacker[1]] - 1
        if new_M[attacker[0]][attacker[1]] == 0:
            new_M[attacker[0]][attacker[1]] = '-'
            kingdom_positions.pop(attacker)

    else:
        defender = sorted(coord)[0]
        kingdom_positions[defender] = kingdom_positions[defender] + \
                                      kingdom_positions[attacker]
        kingdom_positions.pop(attacker)

        new_M = [value for value in M]

        new_M[defender[0]][defender[1]] = M[attacker[0]][attacker[1]] - \
                                          M[defender[0]][defender[1]]
        new_M[attacker[0]][attacker[1]] = '-'

        coord = get_coordinates_attack(M, maximum_value_matrix(M))
        attacker = sorted(coord)[0]

print(time.time() - t)