import numpy as np
import Customized_Map_and_Block
import copy
import sys 
test = np.array([[0, 0, 0, 4, 5, 0],
                 [0, 0, 1, 4, 5, 0],
                 [8, 8, 1, 4, 5, 0],
                 [0, 0, 6, 6, 0, 0],
                 [0, 3, 2, 0, 0, 0],
                 [0, 3, 2, 7, 7, 0]])

a = Map_and_Block.Block(5, 0, 'vertical', 2, 1)
b = Map_and_Block.Block(4, 0, 'vertical', 2, 2)
c = Map_and_Block.Block(4, 2, 'vertical', 2, 3)
d = Map_and_Block.Block(3, 2, 'vertical', 2, 4)
e = Map_and_Block.Block(2, 2, 'vertical', 2, 5)
f = Map_and_Block.Block(3, 4, 'vertical', 2, 6)
g = Map_and_Block.Block(0, 0, 'vertical', 2, 7)

h = Map_and_Block.Block(1, 1, 'horizontal', 3, 8)

i = Map_and_Block.Block(4, 4, 'horizontal', 2, 9)
k = Map_and_Block.Block(0, 3, 'horizontal', 2, 10)

X = Map_and_Block.Block(0, 2, 'horizontal', 2, 11)

InitState = Map_and_Block.State([a, b, c, d, e, f, g, h, i, k, X])

def Goal_state(node):
    start = node.AllBlocks[2].start_point_x
    if sum(node.GameMap.map[2, start: 6]) == X.indx * X.length:
        return True
    return False

def SuccGen(CurrState): 
    global count
    ChildLst = []
    for move in CurrState.GetNextMoves():
        count += 1
        NextState = CurrState.NextStates(move)
        if NextState.GameMap.__str__() not in AdjacentStates:
            AdjacentStates[NextState.GameMap.__str__()] = CurrState.GameMap.__str__()
            ChildLst.append(NextState)    
    return ChildLst

def Trace():
    CurrPos = FinishNode
    while CurrPos != InitState.GameMap.__str__():
        path.append(CurrPos)
        CurrPos = AdjacentStates[CurrPos]
        
def BFS(root):
    Queue = SuccGen(root)
    while len(Queue) != 0:
        CurrNode = Queue.pop(0)
        if Goal_state(CurrNode):
            return CurrNode.GameMap.__str__()
        else:
            for ChildNode in SuccGen(CurrNode):
                Queue.append(ChildNode)
    return 'Failure'

AdjacentStates = dict()
count = 0
path = []
FinishNode = BFS(InitState)
Trace()
print('Number of steps: %d' %(len(path)))

for i in range(len(path) -1, -1, -1):
    print('Step %d' % (len(path) - i))
    print(path[i])
    print()