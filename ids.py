import Map_and_Block
import copy
import time


# start = time.time()
def goal_state(board, blk):
    """
    Check if we find the solution
    """
    start = blk.start_point_x
    if sum(board.map[blk.start_point_y][start:6]) == 2 * blk.indx:
        return True
    return False

def convert_str_steps(str_solution):
    converted_str_solution = []
    for i in str_solution[::-1]:
        a, b, c, d = i
        """
        Convert the moves into instructions
        - a: size step
        - b: up/down, right/left
        - c: block_index
        - d: direction
        """
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

def depth_limited_search(m, max_depth, current_depth):
    """
    make a deep-first-search function with limited depth
    because it's a recusive funtion => make global variable to add elements
    """
    if current_depth >= max_depth: return #if the current depth >= the depth we set then return(stop)
    global solution 
    global check
    global str_solution 
    global visited
    global count
    if check: return #if found the solution then return(stop)
    visited.add(m) #add this board so we don't encounter it again
    boards = [m]
    goal_block_index = m.blocks[-1].indx
    for board in boards:
        moves = Map_and_Block.Map.All_Moves(board)
        #make a list of possible moves
        for move in moves:
            d = Map_and_Block.Map() #create a new board
            d.map = copy.copy(board.map) #copy the board's map
            d.blocks = [block for block in board.blocks] #copy the board's blocks
            blk = copy.copy(move[0]) #copy the moved block so that the initial map is not changed
            new_move = (blk, move[1], move[2])
            d.move_block(new_move)
            d.blocks[blk.indx - 1] = blk #replace the moved block with the old block the map
            if d not in visited:
                """
                if we didn't encounter this map before then add board, move
                if we haven't found the solution, call the function with this map
                if found the solution, start tracking back to find the sequence of steps
                """
                visited.add(d) #add this board so we don't encounter it again
                steps[current_depth].append((board, d)) #save the board for tracking back
                str_steps[current_depth].append((move[1], move[2], blk.indx, blk.direction)) #save the move for tracking back
                if goal_state(d, d.blocks[-1]): #if solution found 
                    check = 1
                    count += 1
                    if count == 1:
                        print('found solution')
                        print(d, current_depth)
                        solution.append(d)
                        solution.append(board)
                        str_solution.append((move[1], move[2], blk.indx, blk.direction))
                        temp = board
                        k = len(steps)
                        while k > 0: # tracking back
                            for board_step in steps[k - 1]:
                                if temp == board_step[1]:
                                    solution.append(board_step[0])
                                    index = steps[k - 1].index(board_step)
                                    str_solution.append(str_steps[k - 1][index])
                                    temp = board_step[0]
                            k -= 1                                
                        return
                depth_limited_search(d, max_depth, current_depth + 1) # solution not found, call the function with this map
    
def iterative_deepening_search(m):
    """
    call the depth_limited_search function with depth = 0
    if not found the solution, increasing the max_depth
    """
    i = 0
    global steps
    global str_steps
    global visited
    global check
    global solution
    global str_solution
    global count
    solution = []
    str_solution = []
    check = 0
    count = 0
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
        
def print_result(m):
    """print the result after run iterative_deepening_search"""
    global solution
    global str_solution
    goal_block_index = m.blocks[-1].indx
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
