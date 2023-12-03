def main():
    #print(findDigit("ab1bc2"))
    #print(findDigit("ab1c2grthreewow"))
    
    sum = 0

    # read lines of input file and get each digit pair
    f = open("src/input.txt", "r")
    lines = f.readlines()
    for line in lines:
        digits = findDigit(line)
        sum += int(digits)

    print(sum)

def findDigit(line):
    first = -1
    last = -1
    for i in range(0, len(line)):
        # if it's a number, record it
        if line[i].isnumeric():
            if first == -1:
                first = line[i] 
            last = line[i]
        # if it's a letter, check if it spells an number
        else:
            if findSpelled(line, i) != -1:
                # if we found a spelled number
                if first == -1:
                    first = findSpelled(line, i)
                last = findSpelled(line, i)

    digits = str(first) + str(last)
    return digits


def findSpelled(line, i):
    found = -1
    lookup = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "zero": 0
            }
    
    for word in lookup:
        # check each word on current index
        if line[i:i+len(word)] == word:
            found = lookup[word]

    # return last found word
    return found


main()

