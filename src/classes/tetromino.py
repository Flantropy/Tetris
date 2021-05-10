from typing import List
from random import choice
from numpy import rot90
from pygame.math import Vector2
from constants import (
    TETROMINO_COLORS,
    CELLS_IN_HORIZONTAL,
    CELLS_IN_VERTICAL
)


class Tetromino:
    shapes = dict(
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
        self.position = Vector2(CELLS_IN_HORIZONTAL//2, -1)
        self.body = choice(list(self.shapes.values()))
        self.color = choice(TETROMINO_COLORS)
        self.occupied_cells_on_gird = []  # List to track collisions

    def move(self, direction: Vector2) -> bool:
        if self.is_move_possible(direction):
            self.position += direction
            return True
        return False
        
    def is_move_possible(self, direction) -> bool:
        for vector in self.get_vectors():
            vector += direction
            if not 0 <= vector.x < CELLS_IN_HORIZONTAL or vector.y >= CELLS_IN_VERTICAL:
                return False
            if vector in self.occupied_cells_on_gird:
                return False
        return True
    
    def rotate(self) -> None:
        self.body = rot90(self.body)

    def get_vectors(self) -> List[Vector2]:
        vectors = []
        for i, row in enumerate(self.body):
            for j, pixel in enumerate(row):
                if pixel != 0:
                    vectors.append(Vector2(i, j) + self.position)
        return vectors

