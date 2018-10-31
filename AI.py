from copy import deepcopy 


solution = ([1,2,3], [4,5,6], [7,8,0]) #The solution to the 8-tile problem. 
#If you want to change the goal state, change this array
 



def MisplacedTileCalculator(list): #Calculates and returns the number of misplaced tiles in a 2-D array
    
    MisplacedTiles = 0
    for i in range (0,len(list)):

        for j in range (0,len(list)): 
            if (solution[i][j] != list[i][j]):
                MisplacedTiles += 1

    return MisplacedTiles



def ManhattanDistanceCalculator(list): #Calculates and returns the Manhattan distance for a 2-D array

    ManhattanDistance = 0
    for i in range(0, len(list)):
        
        for j in range (0, len(list)):

            solVal = solution[i][j]

            for k in range (0,len(list)):
                for l in range (0,len(list)):

                    currVal = list[k][l]

                    if (currVal == solVal):
                        ManhattanDistance += (abs(i - k) + abs( j - l))
                        

    return ManhattanDistance







def InputFormatting(puzzle, a, b): #turns the user input into a dictionary


    a = {'puzzle': puzzle, 'g(n)': int(a), 'h(n)': int(b)}


    return a



def expand(dict, heuristicCalculator): #responsible for expanding the node passed in and returning a list of nodes resulting from expansion

    
    puzzle = dict['puzzle']

    for i in range (0,len(puzzle)): #loop to find where the zero or 'free' tile is
        for j in range (0,len(puzzle)):
            #print(puzzle[i][j])
            if (puzzle[i][j] == 0):
                a = deepcopy(i)
                b = deepcopy(j)


    
    up = False
    down = False
    left = False
    right = False

    if (a == 0): #if the tile is in the top row, it can only move down in the vertical direction
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
    
    
   # print( "left {0}, right {1}, up {2}, down {3}".format(left, right, up, down))

    children = [] #list to be returned

    if(left):
        LeftChange = deepcopy(dict)
        #swaps the free tile and the tile directly to the left of it, if possible
        temp = LeftChange['puzzle'][a][b - 1]
        LeftChange['puzzle'][a][b - 1] = LeftChange['puzzle'][a][b]
        LeftChange['puzzle'][a][b] = temp
        children.append(LeftChange) 


    if(right):
        RightChange = deepcopy(dict)
        #swaps the free tile and the tile directly to the right, if possible
        temp = RightChange['puzzle'][a][b + 1]
        RightChange['puzzle'][a][b+1] = RightChange['puzzle'][a][b]
        RightChange['puzzle'][a][b] = temp
        children.append(RightChange)
    
        
    if(up):
        UpChange = deepcopy(dict)
        #swaps the free tile and the tile directly aboce it, if possible
        temp = UpChange['puzzle'][a - 1][b]
        UpChange['puzzle'][a - 1][b] = UpChange['puzzle'][a][b]
        UpChange['puzzle'][a][b] = temp
        children.append(UpChange)




    if(down):
        DownChange = deepcopy(dict)
        #swaps the free tile and the tile directly below it, if possible
        temp = DownChange['puzzle'][a + 1][b]
        DownChange['puzzle'][a + 1][b] = DownChange['puzzle'][a][b]
        DownChange['puzzle'][a][b] = temp
        children.append(DownChange)


    for i in range (0, len(children)): #now we give each of the new nodes their proper heuristic

        children[i]['g(n)'] += 1 #Increments the depth of the nodes
        children[i]['h(n)'] = heuristicCalculator(children[i]['puzzle']) #calculates the proper h(n) value depending on what heuristic the user wanted
        


    return children
    







def UniformCostCalculator(list):

    #arguments for pseudocode are problem, queueing-function
    #nodese = make-queue(make-node(problem.InitialState))
    #loop do
    #   if EMPTY(nodes) then return failure
    #   node = Remove-Front(nodes)
    #   if problem.GOAL-StATE(node.STATE) succeeds then return node
    #nodes = QUEUEingfunction(nodes, expand(node, problem.operator)
        

    return 0





    
maxQlength = [] #keeps track of the max queue length of the input queue



def ASTAR(list, heuristicCalculator, nodesExpanded):

    
        
    if (len(list) == 0): #if EMPTY(nodes) then return failure
        return False

    maxQlength.append(len(list))

    
    minimum = 9999
    minimumIndex = 0
    for i in range (0, len(list)): #This set of loops finds the puzzle in the list with the lowest f(n), which wil become the node that is evaluated
            if ((list[i]['g(n)'] + list[i]['h(n)']) < minimum):
                minimumIndex = deepcopy(i)
                minimum = list[i]['g(n)'] + list[i]['h(n)']



   


    node = list.pop(minimumIndex) #node = RemoveFront(nodes) 
    
    print("Currently, the best node to expand is")
    for i in range (0, len(node['puzzle'])):
        print()
        for j in range (0, len(node['puzzle'])):
            print(node['puzzle'][i][j] , end = ' ')
    print()
    print("With a g(n) of {} and a h(n) of {}".format(node['g(n)'], node['h(n)']))
    print()
    
    #print(node)


    # these loops just check if the current state is the goal state
    counter = 0
    for i in range (0, 3):
        for j in range (0,3):
            if node['puzzle'][i][j] == solution[i][j]:
                counter += 1

    if(counter == 9): #this verifires that each element in the list is the same as each element in the solution
        print("Success!")
        print("To solve this problem, the search algorithm expanded a total of {} nodes".format(nodesExpanded))
        print("The maximum number of nodes in the queue at any one time was {}".format(max(maxQlength)))
        print("The depth of the goal node was {}".format(node['g(n)']))
        return node




    mergedlist = list + expand(node,heuristicCalculator) #nodes = queueing-function(node, expand(node, problem.operator)
    nodesExpanded += 1
    
    return ASTAR(mergedlist,heuristicCalculator, nodesExpanded) #recursive call to repeat process 
    






def main():

    puzzle = list(([0,0,0], [0,0,0], [0,0,0]))
    puzzleOne = list(([1,2,3], [4,6,0], [7,5,8]))
    puzzleTwo = list(([1,2,0], [4,6,3], [7,5,8]))
    e = InputFormatting(puzzleOne,0,0)
    
    print("Welcome to Aditya Acharya's 8-puzzle solver.")
    print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
    userChoice = int(input())

    if(userChoice == 2):
        print("Enter your puzzle use a zero to represent the blank")
        print("Use commas to seperate the numbers")
        print("Input should look like 1,2,3 (press enter) 4,5,6 (press enter) 7,8,0 (press enter)")
        a = input()
        b = input()
        c = input()
        
        counter = 0
        for i in range (0, len(a)):
            if (a[i] != ' ' and a[i] != ','):
                e['puzzle'][0][counter] = int(a[i])
                print("These numbers should be equal {} <-----> {}".format(int(a[i]), e['puzzle'][0][counter]))
                print("Counter is {}".format(counter))
                counter += 1


        counter = 0

        for i in range (0, len(b)):
            if (b[i] != ' ' and b[i] != ','):
                e['puzzle'][1][counter] = int(b[i])
                counter += 1
        counter = 0

        for i in range (0, len(c)):
            if (c[i] != ' ' and c[i] != ','):
                e['puzzle'][2][counter] = int(c[i])
                counter += 1

        #print(e['puzzle'])

    Input = [e]


    print("Enter your choice of algorithm")
    print(" 1. Uniform Cost Search")
    print(" 2. A* with the Misplaced Tile heruistic.")
    print(" 3. A* with the Manhattan distance heuristic")
    userChoice = int(input())
    if userChoice == 1:
        ASTAR(Input,UniformCostCalculator, 0) 
    elif userChoice == 2:
        ASTAR(Input, MisplacedTileCalculator, 0)
    elif userChoice == 3:
        ASTAR(Input, ManhattanDistanceCalculator, 0)
    
    







if __name__ == "__main__":
    main()
