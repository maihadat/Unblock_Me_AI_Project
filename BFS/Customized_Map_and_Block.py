import numpy as np
import copy

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
        if direction == "horizontal":
            for i in range(length):
                self.map[y][x + i] = index
        if direction == "vertical":
            for i in range(length):
                self.map[y + i][x] = index

    def delete_block(self, blk):
        x, y, direction, length = (
            blk.start_point_x,
            blk.start_point_y,
            blk.direction,
            blk.length,
        )
        if direction == "horizontal":
            for i in range(length):
                self.map[y][x + i] = 0
        if direction == "vertical":
            for i in range(length):
                self.map[y + i][x] = 0

    def move_block(self, blk, step, direct):
        #if (blk, step, direct) in Map.possible_move(self, blk):
        Map.delete_block(self, blk)
        blk.move(step, direct)
        Map.add_block(self, blk)
        
    def restore_move(self):
        move_block(self, blk, -step, direct)
        
        
    def possible_move(self, blk):
        x, y, direction, length, index = (
            blk.start_point_x,
            blk.start_point_y,
            blk.direction,
            blk.length,
            blk.indx
        )
        move_list = []
        if direction == "vertical":
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

        if direction == "horizontal":
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
    
    def All_Moves(self):
        All_Moves_list = []
        for blk in Block().AllBlocks:
            All_Moves_list += Map.possible_move(self,blk)
        return All_Moves_list

class Block:
    """
    x range from 0 to 5
    y range from 0 to 5
    """
   # All_Blocks = []

    def __init__(self, x, y, direction, length, index):
        self.start_point_x = x
        self.start_point_y = y
        self.direction = direction
        self.length = length
        self.indx = index
        #self.__class__.All_Blocks.append(self)
        
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
        if self.direction == "horizontal":
            self.start_point_x += step * direct
        if self.direction == "vertical":
            self.start_point_y += step * direct


class State():
    def __init__(self, AllBlocks):
        self.AllBlocks = AllBlocks
        self.GameMap = Map()
        for block in self.AllBlocks:
            self.GameMap.add_block(block)
            
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
    
    def NextStates(self, move):
        New = []
        for block in self.AllBlocks:
            TempBlock = copy.copy(block)
            if TempBlock.indx == move[2]:
                TempBlock.move(move[1], move[0])
            New.append(TempBlock)
        return State(New)