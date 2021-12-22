import Map_and_Block as SpLib
import copy
import numpy as np

a = SpLib.Block(5, 0, 'v', 2)
b = SpLib.Block(4, 0, 'v', 2)
c = SpLib.Block(4, 2, 'v', 2)
d = SpLib.Block(3, 2, 'v', 2)
e = SpLib.Block(2, 2, 'v', 2)
f = SpLib.Block(3, 4, 'v', 2)
g = SpLib.Block(0, 0, 'v', 2)

h = SpLib.Block(1, 1, 'h', 3)

i = SpLib.Block(4, 4, 'h', 2)
k = SpLib.Block(0, 3, 'h', 2)

X = SpLib.Block(0, 2, 'h', 2)

InitState = SpLib.State([a, b, c, d, e, f, g, h, i, k, X])
print(InitState.GameMap)

def Goal_state(node):
    start = node.AllBlocks[-1].start_point_x
    if sum(node.GameMap.map[2, start: 6]) == InitState.AllBlocks[-1].indx * InitState.AllBlocks[-1].length:
        return True
    return False

def SuccGen(CurrState, Queue): 
    for move in CurrState.GetNextMoves():
        NextState = CurrState.NextStates(move)
        if NextState.GameMap.__str__() not in AdjacentStates:
            AdjacentStates[NextState.GameMap.__str__()] = CurrState.GameMap.__str__()
            Queue.append(NextState)    

def Trace():
    CurrPos = FinishNode.GameMap.__str__()
    while CurrPos != InitState.GameMap.__str__():
        path.append(CurrPos)
        CurrPos = AdjacentStates[CurrPos]


def BFS(root):
    Queue = []
    SuccGen(root, Queue)
    while len(Queue) != 0:
        CurrNode = Queue.pop(0)
        if Goal_state(CurrNode):
            return CurrNode
        else:
            SuccGen(CurrNode, Queue) 
    return "Failure"



AdjacentStates = dict()
path = []
FinishNode = BFS(InitState)

if FinishNode != 'Failure':
    Trace()

    print('Number of steps: %d' %(len(path)))

    for i in range(len(path) -1, -1, -1):
        print('Step %d' % (len(path) - i))
        print(path[i])
        print()
else:
    print('We have been stucked! No ways to go straight!')

