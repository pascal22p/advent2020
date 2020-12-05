
def part(start, end, part):
    middle = (end - start) // 2 + start
    if part == 'F' or part == 'L':
        return start, middle
    else:
        return middle + 1, end

def getRow(sequence, end):
    start = 0
    for letter in sequence:
        result = part(start, end, letter)
        start, end = result

    if start != end:
        print(sequence, start, end)
        raise ValueError('Ooops')
    else:
        return start

testData = {"BFFFBBFRRR": [70, 7, 567],
"FFFBBBFRRR": [14, 7, 119],
"BBFFBBFRLL": [102, 4, 820]}

for input, expected in testData.items():
    row = int(getRow(input.strip()[0:7], 127))
    seat = int(getRow(input.strip()[-3:], 7))
    id = row * 8 + seat
    if row != expected[0]:
        print(input, row)
        raise ValueError("Failed row")
    if seat != expected[1]:
        print(input, seat)
        raise ValueError("Failed seat")
    if id != expected[2]:
        print(input, id)
        raise ValueError("Failed id")

ids = []
with open('day5input') as file:
    for line in file:
        if len(line.strip())>0:
            row = int(getRow(line.strip()[0:7], 127))
            seat = int(getRow(line.strip()[-3:], 7))
            id = row * 8 + seat
            ids.append(id)

print("Part 1")
print(max(ids))

print("Part 2")
for i in range(min(ids), max(ids)):
    if i not in  ids:
        print(i, "is free")
