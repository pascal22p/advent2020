
def parseInput(text):
    answersInput = text.split("\n\n")
    answers = []
    for group in answersInput:
        answers.append(group.split())
    return answers

def part1(answers):
    result = []
    for group in answers:
        result.append(len(set("".join(group))))
    return result

def part2(answers):
    result = []
    for group in answers:
        sets = []
        for person in group:
            sets.append(set(person))
        result.append(len(set.intersection(*sets)))
    return result

testData = """abc

a
b
c

ab
ac

a
a
a
a

b"""

expected1 = [3,3,3,1,1]
expected2 = [3,0,1,1,1]

answers = parseInput(testData)
result = part1(answers)

if result != expected1:
    print(result)
    print(expected1)
    raise ValueError("Failed test1")

answers = parseInput(testData)
result = part2(answers)

if result != expected2:
    print(result)
    print(expected2)
    raise ValueError("Failed test2")

with open('day6input') as file:
    input = file.read()
    answers = parseInput(input)
    result = part1(answers)

    print("Part 1")
    print(sum(result))

    answers = parseInput(input)
    result = part2(answers)
    print("Part 2")
    print(sum(result))
