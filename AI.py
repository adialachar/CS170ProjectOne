from copy import deepcopy



def MisplacedTileCalculator(list):
    solution = ([1,2,3], [4,5,6], [7,8,0])
    MisplacedTiles = 0
    for i in range (0,3):

        for j in range (0,3):
            if (solution[i][j] != list[i][j]):
                MisplacedTiles += 1

    return MisplacedTiles



def ManhattanDistanceCalculator(list):
    
    solution = ([1,2,3], [4,5,6], [7,8,0])
    ManhattanDistance = 0
    for i in range(0, 3):
        
        for j in range (0, 3):

            solVal = solution[i][j]
            print("Solution Value is {}".format(solVal))

            for k in range (0,3):
                for l in range (0,3):

                    currVal = list[k][l]
                    print("Current Value is {}".format(currVal))

                    if (currVal == solVal):
                        ManhattanDistance += (abs(i - k) + abs( j - l))
                        print("Current Manhattan Distance is {}".format(ManhattanDistance))

    return ManhattanDistance



def InputFormatting(puzzle, a, b):


    a = {'puzzle': puzzle, 'g(n)': int(a), 'h(n)': int(b)}


    return a



def expandManhattan(dict):

    #find the 0
    puzzle = dict['puzzle']

    for i in range (0,3):
        for j in range (0,3):
            print(puzzle[i][j])
            if (puzzle[i][j] == 0):
                a = deepcopy(i)
                b = deepcopy(j)


    print("This should be a zero --> {}".format(puzzle[a][b]))
    
    up = False
    down = False
    left = False
    right = False

    if (a == 0):
        down = True
    elif (a == 1):
        down = True
        up = True
    elif (a == 2):
        up = True


    if (b == 0):
        right = True
    elif (b == 1):
        left = True
        right = True
    elif (b == 2):
        left = True
    
    
    print( "left {0}, right {1}, up {2}, down {3}".format(left, right, up, down))



    if(left):
        LeftChange = deepcopy(dict)
        #swap we are using for now
        temp = LeftChange['puzzle'][a-1][b]
        LeftChange['puzzle'][a-1][b] = LeftChange['puzzle'][a][b]
        LeftChange['puzzle'][a][b] = temp

        LeftChange['g(n)'] += 1
        LeftChange['h(n)'] = MannhattanDistanceCalculator(LeftChange['puzzle'])

    if(right):
        RightChange = deepcopy(dict)

        #same as above
    if(up):
        UpChange = deepcopy(dict)

    if(down):
        DownChange = deepcopy(dict)









def UniformCostSearch():

    #arguments for pseudocode are problem, queueing-function
    #nodese = make-queue(make-node(problem.InitialState))
    #loop do
    #   if EMPTY(nodes) then return failure
    #   node = Remove-Front(nodes)
    #   if problem.GOAL-StATE(node.STATE) succeeds then return node
    #nodes = QUEUEingfunction(nodes, expand(node, problem.operator)
    return 0





def main():

    puzzle = list(([0,0,0], [0,0,0], [0,0,0]))
    puzzleOne = list(([1,2,3], [4,6,0], [7,5,8]))
    puzzleTwo = list(([1,2,0], [4,6,3], [7,5,8]))
    #a = ManhattanDistanceCalculator(puzzleOne)
    #b = ManhattanDistanceCalculator(puzzleTwo)
    #print("Manhattan")
    #print(a)
    #print(b)
    #c = MisplacedTileCalculator(puzzleOne)
    #d = MisplacedTileCalculator(puzzleTwo)
    #print("Misplaced Tiles")
    #print(c)
    #print(d)
    e = InputFormatting(puzzleOne,5,6)
    print(e['puzzle'])
    print(e['g(n)'])
    print(e['h(n)'])
    expandManhattan(e)
    #provide room for user input here










if __name__ == "__main__":
    main()
