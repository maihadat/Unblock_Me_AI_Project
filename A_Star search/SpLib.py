import numpy as np
import copy
import os

class Block:
    index = 0
    """
    x range from 0 to 5
    y range from 0 to 5
    """ 
    def __init__(self, x, y, direction, length):
        global index
        self.start_point_x = x
        self.start_point_y = y
        self.direction = direction
        self.length = length
        Block.index += 1  #when you initialize next item, its index will raise
        self.indx = Block.index
                 
        
    def __str__(self):
        a = 'start_point_x = %d\
        start_point_y = %d\
        direction = %s\
        length = %d\
        index  = %d'\
            % (int(self.start_point_x),\
            int(self.start_point_y),\
            self.direction,\
            int(self.length),\
            int(self.indx))
        return a

    def move(self, step, direct):
        """
        :param step: int
        :param direct: -1/+1
        :return: new block
        """
        if self.direction == "h":
            self.start_point_x += step * direct
        if self.direction == "v":
            self.start_point_y += step * direct
            
    def restartTag():
        Block.index = 0
    def __eq__(self, other):
        return self.start_point_x == other.start_point_x and self.start_point_y == other.start_point_y
class Map:
    def __init__(self):
        self.map = np.array([[0 for i in range(6)] for i in range(6)])

    def __str__(self):
        return str(self.map)

    def add_block(self, blk):
        x, y, direction, length, index = (
            blk.start_point_x,
            blk.start_point_y,
            blk.direction,
            blk.length,
            blk.indx,
        )
        
        if direction == "h":
            for i in range(length):
                self.map[y][x + i] = index
        if direction == "v":
            for i in range(length):
                self.map[y + i][x] = index

    def possible_move(self, blk):
        x, y, direction, length, index = (
            blk.start_point_x,
            blk.start_point_y,
            blk.direction,
            blk.length,
            blk.indx
        )
        move_list = []
        if direction == "v":
            if y == 0:
                up = 0
            else:
                for up in range(1, y + 1):
                    if self.map[y - up][x] != 0:
                        up -= 1
                        break
                    else:
                        move_list.append((up, -1, index))    
                        
            if y + length == 6:
                down = 0
            else:
                for down in range(1, 7 - y - length):
                    if self.map[y + length + down - 1][x] != 0:
                        down -= 1
                        break
                    else:
                        move_list.append((down, +1, index))

        if direction == "h":
            if x == 0:
                left = 0
            else:
                for left in range(1, x + 1):
                    if self.map[y][x - left] != 0:
                        left -= 1
                        break
                    else:
                        move_list.append((left, -1, index))
            if x + length == 6:
                right = 0
            else:
                for right in range(1, 7 - x - length):
                    if self.map[y][x + length + right - 1] != 0:
                        right -= 1
                        break
                    else:
                        move_list.append((right, +1, index))
        return move_list

class State():
    def __init__(self, AllBlocks, InitCost = 0, Func = None):
        self.AllBlocks = AllBlocks
        self.GameMap = Map()
        for block in self.AllBlocks:
            self.GameMap.add_block(block)
        self.InitCost = InitCost
        self.Eval = None
        self.Func = Func
        self.GetEvaluation()

        Block.restartTag()
        
    def __lt__(self, other):
        return self.Eval < other.Eval
    def __gt__(self, other):
        return self.Eval > other.Eval
    def __eq__(self, other):    
        return self.Eval == other.Eval
    
    def GetEvaluation(self):
        if self.Func != None:
            self.Eval = self.InitCost + self.Func(self)
        else: 
            self.Eval = self.InitCost 
        
    def GetMap(self):
        return self.GameMap
    
    def GetNextMoves(self):
        All_Moves_list = []
        a = self.GetMap()
        for blk in self.AllBlocks:
            All_Moves_list += a.possible_move(blk)
        return All_Moves_list

    def Display(self):
        return self.GameMap.__str__()
    
    def NextState(self, move):
        New = []
        for block in self.AllBlocks:
            TempBlock = copy.copy(block)
            if TempBlock.indx == move[2]:
                TempBlock.move(move[1], move[0])
            New.append(TempBlock)
        return State(New, self.InitCost + 1, self.Func)

class PriorityQueue():
    def __init__(self, Lst):
        self.Lst = Lst
        if self.GetSize() > 1:
            self.BuildHeap()
    
    def __str__(self):
        return str(self.Lst)

    def GetSize(self):
        return len(self.Lst)
    
    def BuildHeap(self):
        for i in range((self.GetSize() // 2) - 1, -1):
            self.Heapify(i)
            
    def Swap(self, i, j):
        self.Lst[i], self.Lst[j] = self.Lst[j], self.Lst[i]
        
    def Heapify(self, i):
        l = i * 2 + 1
        r = i * 2 + 2
        MinId = i
        if r <= self.GetSize() - 1:
            if self.Lst[MinId] > self.Lst[r]:
                MinId = r
            
        if l <= self.GetSize() - 1:
            if self.Lst[MinId] > self.Lst[l]:
                MinId = l
                
        if MinId != i:
            self.Swap(i, MinId)
            self.Heapify(MinId)

    def RevHeapify(self, i):
        parent = i // 2
        if parent != i and self.Lst[parent] > self.Lst[i]:
            self.Swap(parent, i)
            self.RevHeapify(parent)
            
    def Minimum(self):
        if self.GetSize != 0:
            return self.Lst[0]
        else:
            return float('inf')
            
    def Enqueue(self, a):
        self.Lst.append(a)
        self.RevHeapify(self.GetSize() - 1)
        
    def Dequeue(self):
        self.Swap(0, self.GetSize() - 1)
        Max = self.Lst.pop()
        self.Heapify(0)
        return Max

def read_input(file_name): # read a text file and return an instance of Map class
    m = Map()
    AllBlocks = []
    with open(file_name) as f:
        list_of_blocks = f.readlines()[:]
        number_of_blocks = len(list_of_blocks)
        for i in range(number_of_blocks):
            if i == number_of_blocks-1:
                block = list_of_blocks[i].strip()
            else:
                block = list_of_blocks[i][:-1].strip()
            x = int(block[0])
            y = int(block[2])
            direc = block[4]
            length = int(block[-1])
            blk = Block(x, y, direc, length)
            AllBlocks.append(blk)
            m.add_block(blk)
    return m, AllBlocks


if __name__ == '__main__':
    print(os.getcwd())
    _, Test = read_input('A Star\inp1000_2.txt')
    InitState = State(Test)
    print(InitState.GameMap)
    