import re

bagRegexp = re.compile("([0-9]+) (\w+ \w+) bag[s., ]*")

def parseInput(testData):
    lines = testData.splitlines()
    result = {}
    for line in lines:
        if line:
            holder, content = line.split("contain")
            bags = bagContent(content)
            cleanedHolder = " ".join(holder.split(' ')[0:2])
            if cleanedHolder not in result:
                result[cleanedHolder] = bags
            else:
                raise ValueError("bag already in result")
    return result

def bagContent(content):
    bags = bagRegexp.findall(content)
    result = {}
    for bag in bags:
        if bag[1] not in result:
            result[bag[1]] = int(bag[0])
        else:
            raise ValueError("content bag already present")
    return result

def findBags(toFind, allBags):
    found = []
    for aBag in toFind:
        for holder, searchBag in bags.items():
            if aBag in searchBag:
                found.append(holder)

    if len(found) > 0:
        result =  list(set(toFind + findBags(found, allBags)))
    else:
        result = toFind
    return result

def countBags(toFind, allBags):
    count = 0
    if toFind in allBags:
        for bag, content in allBags[toFind].items():
            count += content * (countBags(bag, allBags) + 1)

    return count

testData = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

expected = 4
bags = parseInput(testData)
result = findBags(['shiny gold'], bags)

if len(result) - 1 != expected:
    print(holders)
    print(holders, expected)
    raise ValueError("failed part 1 test data")

testData2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

expected = 126
bags = parseInput(testData2)
count = countBags('shiny gold', bags)
if count != expected:
    raise ValueError("test 2")

with open('day7input') as file:
    input = file.read()
    bags = parseInput(input)
    result = findBags(['shiny gold'], bags)
    print("Part 1", len(result) - 1)

    count = countBags('shiny gold', bags)
    print("Part 2", count)
