import timeit
start = timeit.default_timer()

import SpLib 
AdjacentStates = {}

def Goal(node):
    start = node.AllBlocks[-1].start_point_x
    if sum(node.GameMap.map[2, start: 6]) == InitState.AllBlocks[-1].indx * InitState.AllBlocks[-1].length:
        return True
    return False

def SuccGen(CurrState, PriQueue): 
    for move in CurrState.GetNextMoves():
        NextState = CurrState.NextState(move)
        if NextState.GameMap.__str__() not in AdjacentStates:
            AdjacentStates[NextState.GameMap.__str__()] = CurrState.GameMap.__str__()
            PriQueue.Enqueue(NextState)
    
def Heuristics1(State):
    count = 0
    for block in State.AllBlocks:
        if block.length == 3:
            if block.direction == 'v':
                if block.start_point_y != 3:
                    count += 1
            #elif block.direction == 'h':
                #if block.start_point_x != 0 or block.start_point_x != 5:
                    #count += 1 
        else:
            if block.direction == 'v':
                if block.start_point_y != 0 or block.start_point_y != 4:
                    count += 1
            #if block.direction == 'h':
                #if block.start_point_x != 0 or block.start_point_x != 5:
                    #count += 1
    return count           


def Heuristics2(State):
    global FinishAllBlocks
    count = 0
    for i in range(len(State.AllBlocks)):
        if not (State.AllBlocks[i] == FinishAllBlocks[i]):
            count += 1
   
    return count

def Heuristics3(State):
    global FinishAllBlocks
    sum = 0
    for i in range(len(State.AllBlocks)):
        if State.AllBlocks[i].start_point_x != FinishAllBlocks[i].start_point_x:
            sum += abs(State.AllBlocks[i].start_point_x - FinishAllBlocks[i].start_point_x)
        if State.AllBlocks[i].start_point_y != FinishAllBlocks[i].start_point_y:
            sum += abs(State.AllBlocks[i].start_point_x - FinishAllBlocks[i].start_point_x)
    return sum

def A_star_search(root):
    PriQueue = SpLib.PriorityQueue([])
    SuccGen(root, PriQueue)
    while PriQueue.GetSize() != 0:
        CurrNode = PriQueue.Dequeue()
        
        if Goal(CurrNode) == True:
            return CurrNode
        else:
            SuccGen(CurrNode, PriQueue)
    return -1

def Trace():
    CurrPos = FinishNode.GameMap.__str__()
    while CurrPos != InitState.GameMap.__str__():
        path.append(CurrPos)
        CurrPos = AdjacentStates[CurrPos]

def ConvertToText(AllBlocks, Input):
    with open(Input, 'w') as f:
        for block in AllBlocks:
            x, y, BlkType, leng = block.start_point_x, block.start_point_y, block.direction, block.length
            line = '%d %d %s %d\n' % (x, y, BlkType, leng)
            f.write(line)



Tag = 1000
_, All_Blocks = SpLib.read_input('A Star\Sample Test\inp%d.txt' % Tag)
_, FinishAllBlocks = SpLib.read_input('A Star\Sample Test\inp%d_2.txt' % Tag)

InitState = SpLib.State(All_Blocks, 0, Heuristics2)
print(InitState.GameMap)


#FinishState = SpLib.State(FinishAllBlocks)
FinishNode = A_star_search(InitState)

print(FinishNode.GameMap)



''' Get Finish State:
Tag = 
ConvertToText(FinishNode.AllBlocks, 'A Star\inp%d_2.txt' % Tag)


ConvertToText(FinishNode.AllBlocks, 'A Star\inp%d_2.txt' % Tag)

ConvertToText(InitState.AllBlocks, 'inp%d.txt % Tag)

'''
path = []
Trace()

print('Number of steps: %d' %(len(path)))

for i in range(len(path) -1, -1, -1):
    print('Step %d' % (len(path) - i))
    print(path[i])
    print()

stop = timeit.default_timer()
print('Time: ', stop - start) 
print(len(AdjacentStates))