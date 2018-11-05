"""
Project 1
Tile Game
Graph-Search Algorithm using A* SEARCH
By- Asim Satti
"""

import sys

class tree:
    class node:
        def __init__(self,data = None):
            self.level = None
          
            self.left = None
            self.up = None
            self.right = None
            self.down = None
            self.table = data

        def getIncorrect(self):
            wrong = 0
            
          
            for i in range(len(self.table)):
                if(self.table[i] != self.goal[i]):
                         wrong+=1
 
            return wrong
                         
                


         
    def __init__(self, inital,final):
        self.root = None
        self.size = 0
        self.init = inital
        self.goal = final
        self.current = None
        self.directions = []


    def start(self):
     
        depth = 0
        self.root = self.newNode()
        self.current = self.root
        while(self.current.table != self.goal ):
            self.search()
            depth+=1
            print(depth,self.current.table,"  ", self.goal)
                     
    def search(self):
        #Searchs table finds the blank and creates children 
        zero_pos = -1
         
        for i in range(len(self.current.table)):
            if(int(self.current.table[i]) == 0):
                     zero_pos = i
 
        self.Left(zero_pos)
        self.Up(zero_pos)
        self.Right(zero_pos)
        self.Down(zero_pos)

        self.calculateCheapestChild()
        
                     

    def Left(self,space):
        #Left Column indexes out
        
        if(space != 0 or space != 3 or space != 6):
            self.current.left = self.newNode()
            
            self.current.left.table[space] = self.current.left.table[space-1]
          
            self.current.left.table[space - 1] = '0'
        
        else:
            self.current.left = None

    def Up(self,space):
        #Top row indexes out
        
        if(space != 0 or space != 1 or space != 2):
            self.current.up = self.newNode()
            self.current.up.table[space] = self.current.up.table[space -3]
            self.current.up.table[space -3] = '0'
         
        else:
            self.current.up = None

    def Right(self,space):
        #Right Column indexes out
        if(space != 2 or space != 5 or space != 8):
            self.current.right = self.newNode()
            self.current.right.table[space] = self.current.right.table[space+1]
            self.current.right.table[space +1 ] = '0'
         
                     
        else:
            self.current.right = None
                     
    def Down (self,space):
        if(space!=6 or space !=7 or space !=8):
            self.current.down = self.newNode()
            self.current.down.table[space] = self.current.down.table[space+3]
            self.current.down.table[space+3] = '0'
      
        else:
            self.current.down = None
        
 
        
    def newNode(self, inital = None,theGoal = None):
        #Creates children node
        #Increments level
        #Takes goal from root as they are the same
        
        newNode = self.node()
        if(self.size == 0):
            newNode.goal = theGoal
            newNode.level = 0
            newNode.table = self.init
        else:        
            newNode.level = self.current.level+1
            newNode.goal = self.goal
            newNode.table = self.current.table.copy()
        self.size+=1
        return newNode

    
 

    def getDirection(self,direction):
        #Adds Directions Traversed
        #Updates current 
       
        if(direction == 0):
            self.directions.append("L")
            self.current = self.current.left
            print('going left')
        elif(direction == 1):
            self.directions.append("U")
            self.current = self.current.up
            print('going up')
        elif(direction == 2):
            self.directions.append("R")
            self.current = self.current.right
            print('going right')
        elif(direction == 3):
            self.directions.append("D")
            self.current = self.current.down
            print('going down')

    
        
    def calculateCheapestChild(self):
        #Calculates Manhattan Distance by
        #*Adding all children to array
        #*Calculating the cost and position keeps track of LURD
        
        manhattanDistanceCosts = []
        if(self.current.left is not None):
 
            wrong = self.current.left.level + self.current.left.getIncorrect()
            manhattanDistanceCosts.append(wrong)

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        if(self.current.up is not None):
            wrong = self.current.up.level + self.current.up.getIncorrect()
            manhattanDistanceCosts.append(wrong)

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        if(self.current.right is not None):
            wrong = self.current.right.level + self.current.right.getIncorrect()
            manhattanDistanceCosts.append(wrong)

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        if(self.current.down is not None):
            wrong = self.current.down.level + self.current.down.getIncorrect()
            manhattanDistanceCosts.append(wrong)

        else:
            manhattanDistanceCosts.append(sys.maxsize)
        
       
        #Each keeps track of which child then cheapest
        
        cheapest = min(manhattanDistanceCosts)
        path = manhattanDistanceCosts.index(cheapest)
        self.getDirection(path)
        
         


def Read(file):
    #
    
    fp = open(file, 'r')
    init = []
    temp = []
    final = []
    with open(file):
        num=0
        while num<=9:
            char = fp.read(1)
            if not char:
                break
           
            temp.append(char)
        for each in range(len(temp)):
            if(ord(temp[each])==10):
                pass
            else:
                init.append(temp[each])
        
     
        final = init[9:]
        init = init[:9]


        return init,final
            


if __name__ == "__main__":
   # GSA = tree()

    #init are going to be arrays of size 9
   
    #File_name  inital state
    file_name = input("Enter file path: ")
    # Goal state
    solved_file = file_name+"_solved"
    print(solved_file)
    init,final = Read(file_name)

    print(init, final)

    GSA = tree(init,final)
    GSA.start()
