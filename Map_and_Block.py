import numpy as np


class Map:
    def __init__(self):
        self.map = np.array([[0 for i in range(6)] for i in range(6)])
        self.blocks = Block.All_Blocks

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

    def move_block(self, tup):
        Map.delete_block(self, tup[0])
        tup[0].move(tup[1], tup[2])
        Map.add_block(self, tup[0])

    def possible_move(self, blk):
        x, y, direction, length = (
            blk.start_point_x,
            blk.start_point_y,
            blk.direction,
            blk.length,
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
                        move_list.append((blk, up, -1))    
            if y + length == 6:
                down = 0
            else:
                for down in range(1, 7 - y - length):
                    if self.map[y + length + down - 1][x] != 0:
                        down -= 1
                        break
                    else:
                        move_list.append((blk, down, +1))

        if direction == "horizontal":
            if x == 0:
                left = 0
            else:
                for left in range(1, x + 1):
                    if self.map[y][x - left] != 0:
                        left -= 1
                        break
                    else:
                        move_list.append((blk, left, -1))
            if x + length == 6:
                right = 0
            else:
                for right in range(1, 7 - x - length):
                    if self.map[y][x + length + right - 1] != 0:
                        right -= 1
                        break
                    else:
                        move_list.append((blk, right, +1))
        return move_list
    
    def All_Moves(self):
        All_Moves_list = []
        for blk in self.blocks:
            All_Moves_list += Map.possible_move(self,blk)
        return All_Moves_list

class Block:
    """
    x range from 0 to 5
    y range from 0 to 5
    """
    All_Blocks = []
    index = 1

    def __init__(self, x, y, direction, length):
        self.start_point_x = x
        self.start_point_y = y
        self.direction = direction
        self.length = length
        self.indx = Block.index
        Block.All_Blocks.append(self)
        Block.index += 1
        

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


'''
   Khi gõ các thông tin của map lên file txt thì cần theo một số quy chuần:
       + Các cột theo thứ tự từ trái qua phải lần lượt là start_x, start_y, kí tự đầu của direc, length
       + Khi điền block cuối(cũng là block đỏ) thì ko đc enter xuống dòng
    Tôi có để file test_map.txt làm mẫu để mọi người điền cho ko bị lỗi
'''
def read_input(file_name):
    m = Map()
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
            if block[4] == 'h':
                direc = 'horizontal'
            elif block[4] == 'v':
                direc = 'vertical'
            length = int(block[-1])
            blk = Block(x, y, direc, length)
            m.add_block(blk)
    return m

