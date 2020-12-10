import numpy
import math
import re


testInput = numpy.fromstring("""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""", dtype = numpy.int32, sep = "\n")

testInput2 = numpy.fromstring("""16
10
15
5
1
11
7
19
6
12
4
""", dtype = numpy.int32, sep = "\n")

def do(input):
    sortedInput = numpy.sort(numpy.append(input, 0))
    shifted = sortedInput[:-1]

    diff = sortedInput[1:] - shifted
    unique, counts = numpy.unique(diff, return_counts=True)
    result = dict(zip(unique, counts))
    result[3] += 1

    return result

result = do(testInput)
expected = {1: 22, 3: 10}

if result != expected:
    raise ValueError("Test part 1 failed")

input = numpy.loadtxt('day10input', dtype=numpy.int32)
result = do(input)
print("Part 1", result[1]*result[3])
