"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt

def CalculateNextNode(length, CurrentNode, NextNode):
    NextNode.append([CurrentNode[j][0]+length*sin(CurrentNode[j][2]-0.1), CurrentNode[j][1]+length*cos(CurrentNode[j][2]-0.1), CurrentNode[j][2]-0.1])
    NextNode.append([CurrentNode[j][0]+length*sin(CurrentNode[j][2]+0.1), CurrentNode[j][1]+length*cos(CurrentNode[j][2]+0.1), CurrentNode[j][2]+0.1])

def DrawNodes(CurrentNode, NextNode):
    plt.plot([CurrentNode[j][0], NextNode[-2][0]],[CurrentNode[j][1], NextNode[-2][1]])
    plt.plot([CurrentNode[j][0], NextNode[-1][0]],[CurrentNode[j][1], NextNode[-1][1]])
    
length = 1

CurrentNode = [[0,1,0]]

# Draw the root of the tree
plt.plot([0,0],[0,1])

BranchNumber = 5

for i in range(BranchNumber):
    
    NextNode = []
    
    for j in range(len(CurrentNode)): #loop over d 
        CalculateNextNode(length, CurrentNode, NextNode)
        DrawNodes(CurrentNode, NextNode)
        
    CurrentNode = NextNode
    length*=0.6
    
plt.savefig('tree.png')
