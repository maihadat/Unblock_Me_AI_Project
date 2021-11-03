
import numpy as np

class Map():
    def __init__(self):
        self.map = np.array([[0 for i in range(6)] for i in range(6)])

    def __str__(self):
        return str(self.map)

    def add_block(self, blk):
        x, y, direction, length, index = blk.start_point_x, blk.start_point_y, blk.direction, blk.length, blk.indx
        if direction == 'horizontal':
            for i in range(length):
                self.map[x][y+i] = index
        if direction == 'vertical':
            for i in range(length):
                self.map[x+i][y] = index



class Block():
   '''
   x range from 0 to 5
   y range from 0 to 5
   '''
   def __init__(self, x, y, direction, length, index):
        self.start_point_x = x
        self.start_point_y = y
        self.direction = direction
        self.length = length
        self.indx = index

   def move(self, step, direct):
        """
        :param step: int
        :param direct: -1/+1
        :return: new block
        """
        if self.direction == 'horizontal':
            self.start_point_x += step*direct
        if self.direction == 'vertical':
            self.start_point_y += step*direct


a = Block(1, 1, 'horizontal', 3, 1)
b = Map()
b.add_block(a)
print(b)
a.move(1, 1)