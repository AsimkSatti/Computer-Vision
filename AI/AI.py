"""
Project 1
Tile Game
Graph-Search Algorithm using A* SEARCH
By- Asim Satti
"""

class tree:
    class node:
        def __init__(self,table):
            self.level = None
            self.incorrect = None
            self.children = []
            self.blank = None
            self.goal = 


        def             
        

    def __init__(self):
        self.root = None
        self.goal = None

    def newNode(self, parent):
        newNode = self.node()
        newNode.level = parent.level+=1
        
    def sides(self):
        #Create all children then add to the parennt
        #Max 4 children
        
    def calculateCheapestChild:
        for (

def Read(file):
    fp = open(file, 'r')
    with open(file):
        line = fp.readline()
        count = 0
        while (line):
            print(count,line)
            line = fp.readline()
            count+=1


if __name__ == "__main__":
    GSA = tree()

    #File_name  inital state
    file_name = input("Enter file path: ")
    # Goal state
    solved_file = file_name+"_solved"
    print(solved_file)
    Read(file_name)
