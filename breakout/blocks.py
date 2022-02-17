from turtle import Turtle
import random
from numpy import block

from scipy import rand

X_NEG = -380
X_POS = 380
BLOCK_START = -380
BLOCK_Y = 250

class Blocks():
    def __init__(self) -> None:

        self.blocks = []
        self.block_groups = []
        self.color = ["red", "orange", "yellow", "green", "blue", "purple"]


    def create_block(self, color):
        # function creates block objects
        length = 0.5
        width = 1
        new_block = Turtle()
        new_block.shape('square')
        new_block.shapesize(length, width)
        new_block.color(color)
        new_block.penup()
        self.blocks.append(new_block)


    def create_row_blocks(self):
        # Function creates the blocks needed for rows
        color = self.color.pop()
        for _ in range(26):
            self.create_block(color)


    def create_row(self):
        # Function lines up each block in a row

        block_list = []
        count = 0

        for _ in range(6):
            self.create_row_blocks()

        for i in range(len(self.blocks)):
            if count <= 25:
                block_list.append(self.blocks[i])
                count += 1
            else:
                self.block_groups.append(block_list)
                if i < len(self.blocks) - 1:
                    block_list = []
                    block_list.append(self.blocks[i])
                    count = 1
        else:
            self.block_groups.append(block_list)

        

        


        
