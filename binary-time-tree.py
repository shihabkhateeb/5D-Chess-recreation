#File that defines binary tree nodes for storing time states, allowing for branching off of timelines. 

class Node: #A node represents a single move, after which time 'moves' forward. 
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data): #insert into tree based on whose move it is/branch timelines based on whose move it is.
        #pass in move's FEN string, extract part that indicates w/b turn, this indicates which side to branch towards
