import numpy
import math

testInput = """F10
N3
F7
R90
F11"""

def parseInput(text):
    input = []
    for line in text.splitlines():
        if line:
            input.append({"action":line[0], "distance":int(line[1:])})

    return input

def doInstruction(instruction, current, rotation):
    if instruction["action"] == "N":
        current[1] += instruction["distance"]
    elif instruction["action"] == "S":
        current[1] -= instruction["distance"]
    elif instruction["action"] == "E":
        current[0] += instruction["distance"]
    elif instruction["action"] == "W":
        current[0] -= instruction["distance"]
    elif instruction["action"] == "L":
        if instruction["distance"] not in [0, 90, 180, 270]:
            raise ValueError("Not Implement: non square rotations")
        rotation = rotation - instruction["distance"]
        if rotation < 0:
            rotation += 360
        rotation = rotation%360
    elif instruction["action"] == "R":
        if instruction["distance"] not in [0, 90, 180, 270]:
            raise ValueError("Not Implement: non square rotations")
        rotation = rotation + instruction["distance"]
        if rotation < 0:
            rotation += 360
        rotation = rotation%360
    elif instruction["action"] == "F":
        if rotation == 0:
            current[1] += instruction["distance"]
        elif rotation == 90:
            current[0] += instruction["distance"]
        elif rotation == 180:
            current[1] -= instruction["distance"]
        elif rotation == 270:
            current[0] -= instruction["distance"]

    return current, rotation

def doInstruction2(instruction, current, rotation, waypoint):
    if instruction["action"] == "N":
        waypoint[1] += instruction["distance"]
    elif instruction["action"] == "S":
        waypoint[1] -= instruction["distance"]
    elif instruction["action"] == "E":
        waypoint[0] += instruction["distance"]
    elif instruction["action"] == "W":
        waypoint[0] -= instruction["distance"]
    elif instruction["action"] in ["R", "L"]:
        rotationRad = math.radians(instruction["distance"])
        if instruction["action"] == "L":
            direction = 1.0
        else:
            direction = -1.0
        rotationMatrix = numpy.array([[math.cos(rotationRad), -direction * math.sin(rotationRad)],
        [direction * math.sin(rotationRad), math.cos(rotationRad)]])
        waypoint = numpy.dot(rotationMatrix, waypoint)
    elif instruction["action"] == "F":
        current += instruction["distance"]*waypoint

    return current, rotation, waypoint

instructionList = parseInput(testInput)

current = numpy.array([0.0, 0.0])
rotation = 90
for instruction in instructionList:
    current, rotation = doInstruction(instruction, current, rotation)

expected = 25
if abs(current[0]) + abs(current[1]) != expected:
    raise ValueError("error test part 1")

current = numpy.array([0.0, 0.0])
waypoint = numpy.array([10.0, 1.0])
rotation = 90.0
for instruction in instructionList:
    current, rotation, waypoint = doInstruction2(instruction, current, rotation, waypoint)

expected = 286
if abs(current[0]) + abs(current[1]) != expected:
    raise ValueError("error test part 2")

with open('day12input') as file:
    instructionList = parseInput(file.read())
    current = [0, 0]
    rotation = 90
    for instruction in instructionList:
        current, rotation = doInstruction(instruction, current, rotation)

    print("Part 1", abs(current[0]) + abs(current[1]))

    current = numpy.array([0.0, 0.0])
    waypoint = numpy.array([10.0, 1.0])
    rotation = 90.0
    for instruction in instructionList:
        current, rotation, waypoint = doInstruction2(instruction, current, rotation, waypoint)

    print("Part 2", round(abs(current[0]) + abs(current[1])))
