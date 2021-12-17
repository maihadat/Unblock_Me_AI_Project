import numpy as np
import Customized_Map_and_Block
import copy
import random 

AdjacentStates = dict()
depth = 1
def GetDepth():
    return depth

def Goal_state(node):
    start = node.AllBlocks[2].start_point_x
    if sum(node.GameMap.map[2, start: 6]) == X.indx * X.length:
        return True
    return False

def SuccGen(CurrState): 
    ChildLst = []
    for move in CurrState.GetNextMoves():
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

def Limit(depth, Queue):
    depth_limit = 100 #random.randint(20, 40)
    return depth == depth_limit or len(Queue) == 0

def DF_Traverse(root):
    pass
    if root.GameMap.__str__():
        pass
    

def BF_Traverse(root):
    global depth
    Queue = SuccGen(root)

    print(Queue)
    EndDepth = Queue[-1].GameMap.__str__()
    ChangeDepth = False
    
    while len(Queue) != 0:
        CurrNode = Queue.pop(0)
        if Limit(GetDepth(), Queue):
            return CurrNode
        if CurrNode.GameMap.__str__() == EndDepth:
            ChangeDepth = True
            depth += 1
            print(depth)
            
        

        else:
            for ChildNode in SuccGen(CurrNode):
                Queue.append(ChildNode)
                if len(Queue) == 500:
                    break
            # To get end of depth, we must append all childnodes of EndDepth first before starting new counting.   
            if ChangeDepth == True:
                EndDepth = Queue[-1].GameMap.__str__()
                ChangeDepth = False   
                
    return 'Failure'


if __name__  == '__main__':
    pass
    a = Customized_Map_and_Block.Block(5, 0, 'vertical', 2, 1)
    b = Customized_Map_and_Block.Block(4, 0, 'vertical', 2, 2)
    c = Customized_Map_and_Block.Block(4, 2, 'vertical', 2, 3)
    d = Customized_Map_and_Block.Block(3, 2, 'vertical', 2, 4)
    e = Customized_Map_and_Block.Block(2, 2, 'vertical', 2, 5)
    f = Customized_Map_and_Block.Block(3, 4, 'vertical', 2, 6)
    g = Customized_Map_and_Block.Block(0, 0, 'vertical', 2, 7)

    h = Customized_Map_and_Block.Block(1, 1, 'horizontal', 3, 8)

    i = Customized_Map_and_Block.Block(4, 4, 'horizontal', 2, 9)
    k = Customized_Map_and_Block.Block(0, 3, 'horizontal', 2, 10)

    X = Customized_Map_and_Block.Block(0, 2, 'horizontal', 2, 11)

    InitState = Customized_Map_and_Block.State([a, b, c, d, e, f, g, h, i, k, X])
    print(BF_Traverse(InitState).GameMap)