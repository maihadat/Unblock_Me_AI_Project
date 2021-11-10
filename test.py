import Map_and_Block

a = Map_and_Block.Block(1, 1, 'vertical', 3, 1)
b = Map_and_Block.Map()
b.add_block(a)
print(b, '\n')
b.move_block(a, 2, 1)
print(b)