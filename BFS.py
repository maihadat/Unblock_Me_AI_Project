import Map_and_Block
import time

start = time.time()

index = 1
MapTag = '44'
to_solve = Map_and_Block.read_input('testcases/inp%s.txt' % MapTag) 
print (to_solve[0])

All_Blocks = to_solve[1]
InitState = Map_and_Block.State(All_Blocks)

def Goal_state(node):
    start = node.AllBlocks[-1].start_point_x
    if sum(node.GameMap.map[2, start+2: 6]) == 0:
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

print ('Calculation time:', '{:.2f}'.format(time.time()-start),'secs')