# find max of each cube per game, multiply each

def main():
    gameTxt = "Game 100: 15 blue, 6 red; 1 green, 2 red; 12 blue, 8 green, 1 red; 1 red, 7 blue"
    maxes = {"red": 12, "green": 13, "blue": 14}

    powers = list()
    
    f = open("input.txt", "r")
    lines= f.readlines()
    
    for line in lines:
        powers.append(evalGame(line, maxes))

    print(powers)
    f.close()
    sumFound = 0
    for power in powers:
        sumFound += power 
    print(sumFound)

    
def evalGame(inputStr, maxes):
    # get game id
    game_id = int(inputStr.split(":")[0][5:])

    # get max values of each cube
    cubes = getMaxes(inputStr.split(":")[1])

    # get power of the set from cubes values
    product = 1
    for value in list(cubes.values()):
        product *= value
        print("product for game", game_id, "updated to", product, "(multiplied by", value, ")")

    return product


def getMaxes(valuesStr):
    cubeDict = {"red": 0, "green": 0, "blue": 0}

    rounds = valuesStr.split(";")
    # update max number of cubes by round
    for trial in rounds:
        cubes = trial.split(",")
        for draw in cubes:
            numDrawn = [int(i) for i in draw.split() if i.isdigit()][0]
            color = [c for c in draw.split() if c.isdigit() is False][0]
            cubeDict[color] = max(numDrawn, cubeDict[color])

    return cubeDict


main()
