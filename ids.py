import Map_and_Block
import copy
import time

a = Map_and_Block.Block(2, 1, 'vertical', 2)
b = Map_and_Block.Block(2, 3, 'vertical', 2)
c = Map_and_Block.Block(1, 4, 'vertical', 2)
d = Map_and_Block.Block(3, 1, 'vertical', 3)
e = Map_and_Block.Block(4, 1, 'vertical', 3)
f = Map_and_Block.Block(0, 3, 'horizontal', 2)
g = Map_and_Block.Block(2, 5, 'horizontal', 2)
X = Map_and_Block.Block(0, 2, 'horizontal', 2)

m = Map_and_Block.Map()

for blk in m.blocks:
    Map_and_Block.Map.add_block(m, blk)

print(m,'\n')

# start = time.time()
def goal_state(board, blk):
    start = blk.start_point_x
    if sum(board.map[2][start:6]) == 2 * blk.indx:
        return True
    return False

def convert_str_steps(str_solution):
    converted_str_solution = []
    for i in str_solution[::-1]:
        a, b, c, d = i
        if d == 'vertical':
            if b == 1:
                converted_str_solution.append('Move block ' + str(c) + ' down with size step = ' + str(a))
            else:
                converted_str_solution.append('Move block ' + str(c) + ' up with size step = ' + str(a))
        else:
            if b == 1:
                converted_str_solution.append('Move block ' + str(c) + ' to the right with size step = ' + str(a))
            else:
                converted_str_solution.append('Move block ' + str(c) + ' to the left with size step = ' + str(a))
    return converted_str_solution

# visited = set()
# steps = []
# str_steps = []
# check = 0
goal_block_index = m.blocks[-1].indx
def depth_limited_search(m, max_depth, current_depth):
    if current_depth >= max_depth: return
    global solution 
    global check
    global str_solution 
    global visited
    if check: return
    # visited = set()
    visited.add(m)
    boards = [m]
    # global steps
    # steps = []
    # global str_steps 
    # str_steps = []
    goal_block_index = m.blocks[-1].indx
    for board in boards:
        board_moves = {}
        str_board_moves = {}
        moves = Map_and_Block.Map.All_Moves(board)
        for move in moves:
            d = Map_and_Block.Map()
            d.map = copy.copy(board.map)
            d.blocks = [block for block in board.blocks]
            # a, b, c = move
            blk = copy.copy(move[0])
            new_move = (blk, move[1], move[2])
            d.move_block(new_move)
            d.blocks[blk.indx - 1] = blk
            if d not in visited:
                visited.add(d)
                # board_moves[board] = board_moves.get(board, []) + [d]
                # str_board_moves[board] = str_board_moves.get(board, []) + [(move[1], move[2], blk.indx, blk.direction)]
                # print(d)
                # print()
                steps[current_depth].append((board, d))
                str_steps[current_depth].append((move[1], move[2], blk.indx, blk.direction))
                if goal_state(d, d.blocks[-1]):
                    print('found solution')
                    print(d, current_depth)
                    solution.append(d)
                    solution.append(board)
                    str_solution.append((move[1], move[2], blk.indx, blk.direction))
                    check = 1
                    temp = board
                    k = len(steps)
                    while k > 0:
                        for board_step in steps[k - 1]:
                            if temp == board_step[1]:
                                solution.append(board_step[0])
                                index = steps[k - 1].index(board_step)
                                str_solution.append(str_steps[k - 1][index])
                                temp = board_step[0]
                        k -= 1                                
                    return
                depth_limited_search(d, max_depth, current_depth + 1)
            # check += 1
                # if goal_state(d, d.blocks[-1]):
                #     print('board solved')
    # steps.append(step)
    
def iterative_deepening_search(m):
    i = 0
    global steps
    global str_steps
    global visited
    global check
    global solution
    global str_solution
    solution = []
    str_solution = []
    check = 0
    while not check:
        print('max_depth', i)
        visited = set()
        check = 0
        steps = [[] for j in range(i)]
        str_steps = [[] for j in range(i)]
        depth_limited_search(m, i, 0)
        print(len(visited))
        if check:
            print('solution found at max_depth = ' + str(i) + '.')
        i += 1
        
start = time.time()
iterative_deepening_search(m)
initial_board = solution.pop()
solution = solution[::-1]
str_solution = convert_str_steps(str_solution)
run_time = time.time() - start

print('The runtime of the program is ' + str(run_time) + 's.')
print('To solve the problem the program has stored', len(visited), 'boards.')
print('It takes', len(solution), 'steps to solve the problem.')
print('The initial board is:')
print(initial_board)
print('The block need to escape is block ' + str(goal_block_index) + '.')
print()
for i in range(len(solution)):
    print('- Step', i + 1)
    print(str_solution[i])
    print(solution[i])
    input('Press enter to next step:')
    print()
print('Board solved!')  
