import re

passwordRegex = re.compile(r"([0-9]+)\-([0-9]+)[ ]+([a-zA-Z]{1}):[ ]+([^\s]+)")

with open('day2input') as input:
    validCount1 = 0
    validCount2 = 0
    for line in input:
            matches = passwordRegex.search(line)
            if matches is not None:
                start, end, letter, password = matches.groups()
                count = password.count(letter)

                if count >= int(start) and count <= int(end):
                    validCount1 += 1

                if password[int(start) - 1] == letter and password[int(end) - 1] != letter:
                    validCount2 += 1
                elif password[int(end) - 1] == letter and password[int(start) - 1] != letter:
                    validCount2 += 1
            else:
                continue

print("Part 1: valid passwords {}".format(validCount1))
print("Part 2: valid passwords {}".format(validCount2))
