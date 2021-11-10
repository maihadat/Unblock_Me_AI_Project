import Map_and_Block

a = Map_and_Block.Block(1, 1, 'vertical', 3, 1)
b = Map_and_Block.Block(0, 5, 'horizontal', 2, 2)
m = Map_and_Block.Map()

m.add_block(a)
m.add_block(b)

print(m,'\n')
print('a can move', m.possible_move(a),'\n')
print('b can move', m.possible_move(b),'\n')

m.move_block(b,2,1)

print(m,'\n')
print('a can move', m.possible_move(a),'\n')
print('b can move', m.possible_move(b),'\n')

m.move_block(a,2,1)

print(m,'\n')
print('a can move', m.possible_move(a),'\n')
print('b can move', m.possible_move(b),'\n')