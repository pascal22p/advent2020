import numpy

input = numpy.loadtxt('day1input', dtype=numpy.int32)

print("Part 1")
for val in input:
    sum = input + val
    index = numpy.argwhere(sum == 2020)
    if len(index) > 0:
        print(val, input[index[0][0]], val * input[index[0][0]])
        break

print("Part 2")
found = False
for i in range(len(input)):
    val1 = input[i]
    for val2 in input[i+1:]:
        sum = input + val1 + val2
        index = numpy.argwhere(sum == 2020)
        if len(index) > 0:
            print(val1, val2, input[index[0][0]], val1 * val2 * input[index[0][0]])
            found = True
            break
    if found:
        break
