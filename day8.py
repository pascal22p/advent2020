import re

instructionList = ["nop", "acc", "jmp"]
instructionRegexp = re.compile(r"^([a-z]{3}) ([-+0-9]+)")

class Instructions:
    def acc(self, value):
        global instructionIndex
        registers[0] += value
        instructionIndex += 1
        return instructionIndex

    def nop(self, value):
        global instructionIndex
        instructionIndex += 1
        return instructionIndex

    def jmp(self, value):
        global instructionIndex
        instructionIndex += value
        return instructionIndex

def execute(function_name, value):
    m = globals()['Instructions']()
    func = getattr(m, function_name)
    return func(value)

def readInstruction(instruction):
    match = instructionRegexp.search(instruction)
    if match:
        action = match.group(1)
        value = int(match.group(2))
        if action not in instructionList:
            raise ValueError("Instruction `%s` do not exist"%action)
        else:
            return action, value
    else:
        raise ValueError("Invalid instruction")

def run(instruction):
    action, value = readInstruction(instruction)
    execute(action, value)

def part2(instructions):
    global instructionIndex
    global registers

    for i in range(len(instructions)):
        new = instructions.copy()
        action, value = readInstruction(instructions[i])
        if action == 'jmp':
            new[i] = "nop %d"%value
        elif action == 'nop':
            new[i] = "jmp %d"%value

        registers = [0]
        instructionIndex = 0
        instructionVisited = [0] * len(new)
        found = 0
        while True:
            if (instructionIndex > len(new) - 1):
                found = registers[0]
                break
            instructionVisited[instructionIndex] += 1
            if instructionVisited[instructionIndex] > 1:
                break
            run(new[instructionIndex])

        if found != 0:
            break
    return found

testInput = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

expected = [0,1,2,6,7,3,4,1]
expectedAccumulator = 5

registers = [0]
instructionIndex = 0
instructions = testInput.splitlines()
instructionVisited = [0] * len(instructions)
executed = []
while True:
    instructionVisited[instructionIndex] += 1
    executed.append(instructionIndex)
    if instructionVisited[instructionIndex] > 1:
        break
    run(instructions[instructionIndex])

if (any(x != y for x, y in zip(expected, executed))):
    raise ValueError('Test part 1 failed')

if (expectedAccumulator != registers[0]):
    raise ValueError("Accumulator value is wrong")

expected2 = 8
found = part2(instructions)

if (found != expected2):
    print(found, expected2)
    raise ValueError("test part 2 failed")


#######################################
# All tests done

registers = [0]
instructionIndex = 0
with open('day8input') as file:
    instructions = file.readlines()

    instructionVisited = [0] * len(instructions)
    while True:
        instructionVisited[instructionIndex] += 1
        if instructionVisited[instructionIndex] > 1:
            break
        run(instructions[instructionIndex])

    print("Part 1", registers[0])

    found = part2(instructions)
    print("Part 2", registers[0])
