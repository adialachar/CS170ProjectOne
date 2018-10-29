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
            #print("Solution Value is {}".format(solVal))

            for k in range (0,3):
                for l in range (0,3):

                    currVal = list[k][l]
                    #print("Current Value is {}".format(currVal))

                    if (currVal == solVal):
                        ManhattanDistance += (abs(i - k) + abs( j - l))
                        #print("Current Manhattan Distance is {}".format(ManhattanDistance))

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

    children = []

    if(left):
        LeftChange = deepcopy(dict)
        #swap we are using for now
        temp = LeftChange['puzzle'][a][b - 1]
        LeftChange['puzzle'][a][b - 1] = LeftChange['puzzle'][a][b]
        LeftChange['puzzle'][a][b] = temp
        #print("LEft Boi")
        #print(LeftChange['puzzle'])
        children.append(LeftChange)
        #LeftChange['g(n)'] += 1
        #LeftChange['h(n)'] = MannhattanDistanceCalculator(LeftChange['puzzle'])

    if(right):
        RightChange = deepcopy(dict)

        temp = RightChange['puzzle'][a][b + 1]
        RightChange['puzzle'][a][b+1] = RightChange['puzzle'][a][b]
        RightChange['puzzle'][a][b] = temp
        children.append(RightChange)
    
        #same as above
    if(up):
        UpChange = deepcopy(dict)
        temp = UpChange['puzzle'][a - 1][b]
        UpChange['puzzle'][a - 1][b] = UpChange['puzzle'][a][b]
        UpChange['puzzle'][a][b] = temp
        #print("Up Boi")
        #print(UpChange['puzzle'])
        children.append(UpChange)




    if(down):
        DownChange = deepcopy(dict)
        temp = DownChange['puzzle'][a + 1][b]
        DownChange['puzzle'][a + 1][b] = DownChange['puzzle'][a][b]
        DownChange['puzzle'][a][b] = temp
        #print("Down Boi")
        #print(DownChange['puzzle'])
        children.append(DownChange)


    for i in range (0, len(children)):

        children[i]['g(n)'] += 1
        children[i]['h(n)'] = ManhattanDistanceCalculator(children[i]['puzzle'])
        #print("The manhattan distance for this node is {}".format(children[i]['h(n)']))


    return children
    






def UniformCostSearch():

    #arguments for pseudocode are problem, queueing-function
    #nodese = make-queue(make-node(problem.InitialState))
    #loop do
    #   if EMPTY(nodes) then return failure
    #   node = Remove-Front(nodes)
    #   if problem.GOAL-StATE(node.STATE) succeeds then return node
    #nodes = QUEUEingfunction(nodes, expand(node, problem.operator)
    

    





    return 0




def Manhattan(list):

    solution = ([1,2,3] , [4,5,6] , [7,8,0])
        
    if (len(list) == 0):
        return False

    #node = list.pop([0])

    #find the min of the heuristics, and then only expand that one. ahhhh ok
    minimum = 9999
    minimumIndex = 0
    for i in range (0, len(list)):
            #find the min of the heuristics
            if ((list[i]['g(n)'] + list[i]['h(n)']) < minimum):
                minimumIndex = deepcopy(i)
                minimum = list[i]['g(n)'] + list[i]['h(n)']



   


    node = list.pop(minimumIndex) 
    print(node) 

    #if (node['puzzle'] == solution):
     #   return node

    counter = 0
    for i in range (0, 3):
        for j in range (0,3):
            if node['puzzle'][i][j] == solution[i][j]:
                counter += 1

    if(counter == 9):
        return node




    mergedlist = list + expandManhattan(node)
    #then just make a recrusive call with the new list appended to the old one, right?
    #oh its not that simple
    return Manhattan(mergedlist)
    






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
    #expandManhattan(e)
    Input = [e]
    print("Welcome to Aditya Acharya's 8-puzzle solver.")
    print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
    #userChoice = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
    userChoice = int(input())

    if(userChoice == 2):
        print("Enter your puzzle use a zero to represent the blank")
        #figure out how to take 3 numbers from the thing

    #print(type(Input))
    #Manhattan(Input)
    #provide room for user input here

    print("Enter your choice of algorithm")
    print(" 1. Uniform Cost Search")
    print(" 2. A* with the Misplaced Tile heruistic.")
    print(" 3. A* with the Manhattan distance heuristic")
    userChoice = int(input())










if __name__ == "__main__":
    main()
