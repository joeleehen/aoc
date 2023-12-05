def main():
    gameTxt = "Game 100: 15 blue, 6 red; 1 green, 2 red; 12 blue, 8 green, 1 red; 1 red, 7 blue"
    maxes = {"red": 12, "green": 13, "blue": 14}

    ids = list()
    
    f = open("input.txt", "r")
    lines= f.readlines()
    
    for line in lines:
        ids.append(evalGame(line, maxes))

    print(ids)
    f.close()
    sumFound = 0
    for id in ids:
        sumFound += id
    print(sumFound)

    
def evalGame(inputStr, maxes):
    # get game id
    game_id = int(inputStr.split(":")[0][5:])

    # get max values of each cube
    cubes = getMaxes(inputStr.split(":")[1])

    # check if each game goes over maximum amount of cubes
    for i in range(len(list(cubes.values()))):
        if list(cubes.values())[i] > list(maxes.values())[i]:
            # return None if we draw more than the maximum amount of a color
            return 0
    return game_id


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
