import Map_and_Block
import Customized_Map_and_Block
import BFS_Tools
from importlib import reload 


def CreateBlk(Input):
    with open(Input) as f:
        _, AllBlocks = Map_and_Block.read_input(Input)

        print(AllBlocks)
    return AllBlocks
        
def ConvertToText(AllBlocks, Input):
    with open(Input, 'w') as f:
        for block in AllBlocks:
            x, y, BlkType, leng = block.start_point_x, block.start_point_y, block.direction, block.length
            line = '%d %d %s %d\n' % (x, y, BlkType, leng)
            f.write(line)

def BFS_Reverse(lowbound, upbound):
    global BFS_Tools, Map_and_Block
    for i in range(lowbound, upbound + 1): # upbound + 1
        Input = 'inp%s.txt' % i
        with open(Input, 'w') as f:
            BFS_Tools = reload(BFS_Tools)
            Map_and_Block = reload(Map_and_Block)
            AllBlks = CreateBlk('inp%s_2.txt'%i)
            InitState = Map_and_Block.State(AllBlks)
            print(InitState.GameMap)
            NewState = BFS_Tools.BF_Traverse(InitState)
            ConvertToText(NewState.AllBlocks, Input)

    #return NewState.AllBlocks
            
BFS_Reverse(101, 110) 
#ConvertToText(a, 'inp71_2.txt')


