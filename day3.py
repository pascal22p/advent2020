import numpy
import math

tree = '#'
moves = [[1,1],[3,1],[5,1],[7,1],[1,2]]

data = []
with open('day3input') as input:
    for line in input:
        data.append(line.strip())

xRepeat = len(data[0])

product = 1
for move in moves:
    treeCount = 0
    for y in range(0, math.ceil(len(data)/move[1])):
        x = (y * move[0])%xRepeat
        if data[y*move[1]][x] == tree:
            treeCount += 1
    product *= treeCount
    print("Move (%d, %d): %d"%(move[0], move[1], treeCount))
print("Product", product)
