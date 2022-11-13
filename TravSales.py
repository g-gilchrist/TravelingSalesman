from sys import maxsize 
from itertools import permutations

# create a function that accepts the graph, start node and Number of Nodes in the graph
# I create two lists the vertex list and a path list, I utilize the path list to rename the nodes to the correct values
# After adding the nodes to the list I make the minPath infinite, or a really high number.
# I then utilize the permutations library to reorder the nodes in every possible combination.
def TravSales(graph, start, NumNodes): 
    vertex = []
    path = []
    for i in range(NumNodes): 
            if i != start: 
                    vertex.append(i)
    
    minPath = maxsize 
    permutationList = permutations(vertex)
    x=0
    y=0
    z = -1

    # we then utilize a for loop to iterate through the list of permutations giving them all an initial value of zero
    # I also utilize the Permutations for loop to create a 2 dimensional list/array as well as add the start node to each sub-list.
    # The magic of dynamic programming happens within the for loops, I utilize the for loops to carry out multiple iterations of the program  
    for Permutation in permutationList:
        currentWeight = 0
        currentNode = start
        path.append([start+1]) #this graph does not start at zero so I add one to the start variable because zero is the first number in programming 
        
        # I then utilize another for loop within the first for loop
        # I begin adding the weight of the edges from the graph
        # By updating the current node through each iteration of the for loop we move through the graph
        for permNode in Permutation: 
            currentWeight += graph[currentNode][permNode] 
            currentNode = permNode
    
            # This portion could be simplified by just appending the Permutation in the first for loop to the path list.
            # I did it this way again because the graph nodes do not start at zero. it's not my favorite solution but it works, 
            # from my research iterating through loops instead of recursion to create dynamic programming is much faster.
            path[y].append(currentNode+1)
            x+=1
            if x == 3:
                x = 0
                y+=1
      
        # we again add the graph node to the currentWeight
        # I then do an if statement to count every time the currentWeight is less than the minWeight
        # I utilize this to find which index has the smallest weighted path.
        # this does not solve all possible paths of the smallest weight, it only shows you the first path it finds of the smallest weight.
        # I then print out the findings
        currentWeight += graph[currentNode][start]
        if currentWeight < minPath:
            z += 1
        min_path = min(minPath, currentWeight)
    print("Smallest Path: \t |    Total weight: ")
    print(f"{path[z]} \t |    {min_path} ")

        
# in main I declare the number of nodes, the weights on each edge, the start variable and then initalize the function    
def main():
    
    NumNodes = 4

    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]] 

    start = 3

    TravSales(graph, start-1, NumNodes)
    

main()
