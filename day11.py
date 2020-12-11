import numpy

_floor_ = -1
_free_ = 0
_occupied_ = 1

def parseInput(text):
    lines = text.splitlines()
    layout = []
    for line in lines:
        layout.append(list(map(charToInt, [char for char in line.strip()])))

    return numpy.array(layout)

def charToInt(char):
    if char == ".":
        return _floor_
    elif char == "L":
        return _free_
    else:
        return _occupied_

def intToChar(num):
    if num == _floor_:
        return "."
    elif num == _free_:
        return "L"
    else:
        return "#"

def fillSeats(layout):
    newLayout = layout.copy()
    for row in range(numpy.shape(layout)[0]):
        for col in range(numpy.shape(layout)[1]):
            rmin = max(row-1, 0)
            rmax = min(row+2, numpy.shape(layout)[0])
            cmin = max(col-1, 0)
            cmax = min(col+2, numpy.shape(layout)[1])

            if layout[row, col] == _free_:
                if(not numpy.any(layout[rmin:rmax, cmin:cmax] == _occupied_)):
                    newLayout[row, col] = _occupied_
            elif layout[row, col] == _occupied_:
                if(numpy.count_nonzero(layout[rmin:rmax, cmin:cmax] == _occupied_)>4):
                    newLayout[row, col] = _free_
    return newLayout

def fillSeats2(layout):
    newLayout = layout.copy()
    for row in range(numpy.shape(layout)[0]):
        for col in range(numpy.shape(layout)[1]):
            neighbours = getNeighbours(layout, row, col)
            if layout[row, col] == _free_:
                if(not numpy.any(neighbours == _occupied_)):
                    newLayout[row, col] = _occupied_
            elif layout[row, col] == _occupied_:
                if(numpy.count_nonzero(neighbours == _occupied_)>4):
                    newLayout[row, col] = _free_
    return newLayout

def searchLeft(layout, i, j):
    found = _floor_
    for k in range(j-1, -1, -1):
        if layout[i, k] != _floor_:
            found = layout[i, k]
            break
    return found

def searchRight(layout, i, j):
    found = _floor_
    for k in range(j+1, numpy.shape(layout)[1]):
        if layout[i, k] != _floor_:
            found = layout[i, k]
            break
    return found

def searchTop(layout, i, j):
    found = _floor_
    for k in range(i-1, -1, -1):
        if layout[k, j] != _floor_:
            found = layout[k, j]
            break
    return found

def searchBottom(layout, i, j):
    found = _floor_
    for k in range(i+1, numpy.shape(layout)[0]):
        if layout[k, j] != _floor_:
            found = layout[k, j]
            break
    return found

def searchTopLeft(layout, i, j):
    found = _floor_
    for k, l in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
        if layout[k, l] != _floor_:
            found = layout[k, l]
            return found
    return found

def searchTopRight(layout, i, j):
    found = _floor_
    for k, l in zip(range(i-1, -1, -1), range(j+1, numpy.shape(layout)[1])):
        if layout[k, l] != _floor_:
            found = layout[k, l]
            return found
    return found

def searchBottomLeft(layout, i, j):
    found = _floor_
    for k, l in zip(range(i+1, numpy.shape(layout)[0]), range(j-1, -1, -1)):
        if layout[k, l] != _floor_:
            found = layout[k, l]
            return found
    return found

def searchBottomRight(layout, i, j):
    found = _floor_
    for k, l in zip(range(i+1, numpy.shape(layout)[0]), range(j+1, numpy.shape(layout)[1])):
        if layout[k, l] != _floor_:
            found = layout[k, l]
            return found
    return found

def getNeighbours(layout, i, j):
    return numpy.array([
        searchTopLeft(layout, i, j),
        searchTop(layout, i, j),
        searchTopRight(layout, i, j),
        searchRight(layout, i, j),
        searchBottomRight(layout, i, j),
        searchBottom(layout, i, j),
        searchBottomLeft(layout, i, j),
        searchLeft(layout, i, j)
    ])

def printLayout(layout):
    charLayout = []
    for line in layout:
        charLayout.append(''.join(list(map(intToChar, [num for num in line]))))
    return "\n".join(charLayout)

##########################
# Tests

testInput = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

expected1 = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

expected2 = """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""

layout = parseInput(testInput)
newLayout = fillSeats(layout)
if (printLayout(newLayout) != expected1):
    raise ValueError("failed test part 1.1")

newLayout2 = fillSeats(newLayout)
if (printLayout(newLayout2) != expected2):
    print(printLayout(newLayout))
    for a, b in zip(expected2.splitlines(), printLayout(newLayout2).splitlines()):
        print("%s || %s"%(a.strip(),b.strip()))
    raise ValueError("failed test part 1.2")

layout = parseInput(testInput)
newLayout = fillSeats(layout)
while not numpy.all(layout == newLayout):
    layout = newLayout.copy()
    newLayout = fillSeats(layout)

if numpy.count_nonzero(newLayout == _occupied_) != 37:
    raise ValueError("test part 1. Wrong number of seats")

###### Part 2

testInput2 = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
layout = parseInput(testInput2)

if not numpy.all(getNeighbours(layout, 4, 3) == _occupied_):
    raise ValueError("test part 2.1 failed")

testInput3 = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""
layout = parseInput(testInput3)

expected3 = """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""

if numpy.all(getNeighbours(layout, 3, 4) != _occupied_):
    raise ValueError("test part 2.2 failed")

layout = parseInput(testInput)
newLayout = fillSeats2(layout)
while not numpy.all(layout == newLayout):
    layout = newLayout.copy()
    newLayout = fillSeats2(layout)

if (printLayout(newLayout) != expected3):
    print(printLayout(newLayout))
    for a, b in zip(expected3.splitlines(), printLayout(newLayout).splitlines()):
        print("%s || %s"%(a.strip(),b.strip()))
    raise ValueError("failed test part 2.3")

##########################
# Main

with open('day11input') as file:
    layout = parseInput(file.read())
    layout2 = layout.copy()

    newLayout = fillSeats(layout)
    while not numpy.all(layout == newLayout):
        layout = newLayout.copy()
        newLayout = fillSeats(layout)
    print("Part 1", numpy.count_nonzero(newLayout == _occupied_))

    newLayout2 = fillSeats2(layout2)
    while not numpy.all(layout2 == newLayout2):
        layout2 = newLayout2.copy()
        newLayout2 = fillSeats2(layout2)
    print("Part 2", numpy.count_nonzero(newLayout2 == _occupied_))
