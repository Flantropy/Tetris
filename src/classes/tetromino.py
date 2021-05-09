from __future__ import annotations

from random import choice
from typing import List

import numpy
import pygame
from pygame.math import Vector2

from constants import (
    CELL_SIZE,
    DISPLAY_WIDTH,
    TETROMINO_COLORS
)


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
        self.body = choice(list(self.tetrominos.values()))
        self.color = choice(TETROMINO_COLORS)
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value: Vector2):
        self.__position = value
    
    def draw(self, display) -> None:
        for i, row in enumerate(self.body):
            for j, c in enumerate(row):
                if c == 1:
                    x_pos = (i + self.position.x) * CELL_SIZE
                    y_pos = (j + self.position.y) * CELL_SIZE
                    cell_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(surface=display, color=self.color, rect=cell_rect)
    
    def move(self, direction: Vector2) -> None:
        self.position += direction
    
    def rotate(self) -> None:
        self.body = numpy.rot90(self.body)
    
    def check_collisions(self, stuck_tetrominoes: List[Tetromino]) -> bool:
        my_vectors = self.body_to_vectors(self)
        # for vector in my_vectors:
        #     vector += Vector2(0, 1)
        for tetromino in stuck_tetrominoes:
            his_vectors = self.body_to_vectors(tetromino)
            for vector in my_vectors:
                if vector + Vector2(0, 1) in his_vectors:
                    return True
        for vector in my_vectors:
            if vector.y == 19:
                return True
        return False
    
    @staticmethod
    def body_to_vectors(tetr: Tetromino) -> List[Vector2]:
        vectors = []
        for i, row in enumerate(tetr.body):
            for j, col in enumerate(row):
                if col != 0:
                    vectors.append(Vector2(i, j) + tetr.position)
        return vectors
