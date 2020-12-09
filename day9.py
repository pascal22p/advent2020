from itertools import combinations

def do(numbers, preamble):
    part1 = -1
    part2 = (-1,  -1)
    for i in range(preamble, len(numbers)):
        sumList = []
        for combination in combinations(numbers[i-preamble:i], 2):
            sumList.append(sum(combination))
        if numbers[i] not in sumList:
            part1 = numbers[i]

            for j in range(0, len(numbers)):
                contiguous = 0
                k = -1
                savedList = []
                while(contiguous<part1):
                    k += 1
                    contiguous += numbers[j+k]
                    savedList.append(numbers[j+k])

                if contiguous == part1:
                    part2 = (min(savedList), max(savedList))
                    break

    return part1, part2

testInput = list(map(int, """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()))

expected = 127
part1, part2 = do(testInput, 5)

if part1 != expected:
    raise ValueError("Part 1 test failed")

if part2[0] != 15 or part2[1] != 47:
    raise ValueError("part 2")

with open('day9input') as file:
    input = list(map(int, file.readlines()))
    result = do(input, 25)
    print("Part 1", result[0])
    print("Part 2", sum(result[1]))
