from numpy import Inf
import Map_and_Block

a = Map_and_Block.Block(5, 1, 'vertical', 3)
b = Map_and_Block.Block(0, 5, 'horizontal', 2)
X = Map_and_Block.Block(0, 2, 'horizontal', 2)

m = Map_and_Block.Map()

def Goal_state():
    start = X.start_point_x
    if sum(m.map[2][start:6]) == (X.index-1)*2:
        return True
    return False

for blk in m.blocks:
    Map_and_Block.Map.add_block(m, blk)


print(m,'\n')
print ('Goal state', Goal_state(),'\n')

m.move_block (Map_and_Block.Map.All_Moves(m)[4])
print(m,'\n')
print ('Goal state', Goal_state(),'\n')

m.move_block (Map_and_Block.Map.All_Moves(m)[2])
print(m,'\n')
print ('Goal state', Goal_state(),'\n')
