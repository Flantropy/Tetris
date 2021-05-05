from constants import *
from pygame.math import Vector2
import pygame
from random import choice
from numpy import rot90


class Tetromino:
    tetrominos = dict(
        straight=[
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],
        T=[
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]],
        L=[
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]],
        J=[
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]],
        S=[
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]],
        Z=[
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]],
        square=[
            [1, 1],
            [1, 1]]
    )
    
    def __init__(self):
        self.__position = Vector2(DISPLAY_WIDTH // CELL_SIZE // 2, -1)
        self.body = self.tetrominos["straight"]  # choice(list(self.tetrominos.values()))
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value: Vector2):
        print(f"setting value = {value}")
        if 0 <= value.x:
            self.__position = value
        else:
            self.__position = Vector2(0, value.y)
            
    def draw(self, display) -> None:
        for i, row in enumerate(self.body):
            for j, c in enumerate(row):
                if c == 1:
                    x_pos = (i + self.position.x) * CELL_SIZE
                    y_pos = (j + self.position.y) * CELL_SIZE
                    cell_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(surface=display, color=WHITE, rect=cell_rect)
    
    def move(self, direction: Vector2) -> None:
        self.position += direction
    
    def rotate(self) -> None:
        self.body = rot90(self.body)
