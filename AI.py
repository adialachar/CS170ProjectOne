




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







def UniformCostSearch():

    #arguments for pseudocode are problem, queueing-function
    #nodese = make-queue(make-node(problem.InitialState))
    #loop do
    #   if EMPTY(nodes)
    #   node = Remove-Front(nodes)
    #   if problem.GOAL-StATE(node.STATE) succeeds then return node
    #nodes = QUEUEingfunction(nodes, expand(node, problem.operator)
    return 0





def main():

    puzzle = list(([0,0,0], [0,0,0], [0,0,0]))
    puzzleOne = list(([1,2,3], [4,6,0], [7,5,8]))
    puzzleTwo = list(([1,2,0], [4,6,3], [7,5,8]))
    a = ManhattanDistanceCalculator(puzzleOne)
    b = ManhattanDistanceCalculator(puzzleTwo)
    print(a)
    print(b)
    #provide room for user input here










if __name__ == "__main__":
    main()
