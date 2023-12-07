def main():
    f = open("testput.txt", "r")
    lines = f.readlines()
    f.close()

    foundNums = findParts(lines)
    firstLastCheck(lines, foundNums)

    sum = 0
    for num in foundNums:
        sum += num

    print(sum)
    print("checking lines")
    for line in lines:
        print(line)

    print(type(lines))

def findParts(lines):
    numsFound = list()
    symbols = "*#+$=/@%&-"
    for i in range(1, len(lines) - 1):    # skip first and last lines to avoid index errors
        for j in range(len(lines[i])):
            if lines[i][j] in symbols:
                try:
                    # check adjacent areas for numbers
                    # VERY YUCKY
                    if lines[i - 1][j - 1].isdigit():
                        numsFound.append(pullNumber(lines, i - 1, j - 1))
                    if lines[i - 1][j].isdigit():
                        numsFound.append(pullNumber(lines, i - 1, j))
                    if lines[i - 1][j + 1].isdigit():
                        numsFound.append(pullNumber(lines, i - 1, j + 1))
                    if lines[i][j - 1].isdigit():
                        numsFound.append(pullNumber(lines, i, j - 1))
                    if lines[i][j + 1].isdigit():
                        numsFound.append(pullNumber(lines, i, j + 1))
                    if lines[i + 1][j - 1].isdigit():
                        numsFound.append(pullNumber(lines, i + 1, j -1))
                    if lines[i + 1][j].isdigit():
                        numsFound.append(pullNumber(lines, i + 1, j))
                    if lines[i + 1][j + 1].isdigit():
                        numsFound.append(pullNumber(lines, i + 1, j + 1))
                except IndexError:
                    pass
    return numsFound

def firstLastCheck(lines, numsFound):
    symbols = "*#+$=/@%&-"
    # check first row
    for i in range(len(lines[0])):
        if lines[0][i] in symbols:
            if lines[0][i - 1].isdigit():
                numsFound.append(pullNumber(lines, 0, i - 1))
            if lines[0][i + 1].isdigit():
                numsFound.append(pullNumber(lines, 0, i + 1))
    
    # check last row
    for i in range(len(lines[-1])):
        if lines[-1][i] in symbols:
            if lines[-1][i - 1].isdigit():
                numsFound.append(pullNumber(lines, len(lines) - 1, i - 1))
            if lines[-1][1 + 1].isdigit():
                numsFound.append(pullNumber(lines, len(lines) - 1, i + 1))

def pullNumber(lines, i, j):
    # lines[i][j] is a digit, get all digits of that number
    line = lines[i]
    number = ""
    # check to the left
    for idx in range(j, -1, -1):
        if line[idx].isdigit():
            number = line[idx] + number
        else:
            break
    # check to the right
    for idx in range(j + 1, len(line)):
        if line[idx].isdigit():
            number += line[idx]
            # this avoids double counting while allowing for duplicate numbers
            print("line before:", line)
            line = line.replace(number, "."*len(number))
            lines[i] = line.replace(number, "."*len(number))
            print("line after replacement:", lines[i])
        else:
            break

    return int(number)


main()
