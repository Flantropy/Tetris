from constants import *
from pygame.math import Vector2
import pygame
from random import choice


class Tetromino:
	tetrominos = [
		[Vector2(0, 0), Vector2(0, 1), Vector2(0, 2), Vector2(0, 3)],  # straight
		[Vector2(0, 0), Vector2(1, 1), Vector2(0, 1), Vector2(1, 0)],  # square
		[Vector2(0, 0), Vector2(0, 1), Vector2(0, 2), Vector2(1, 1)],  # T
		[Vector2(0, 0), Vector2(1, 0), Vector2(2, 0), Vector2(2, 1)],  # L
		[Vector2(0, 1), Vector2(1, 0), Vector2(1, 1), Vector2(2, 0)]  # skew
	]
	
	def __init__(self):
		self.start = Vector2(DISPLAY_WIDTH // CELL_SIZE // 2, -1)
		self.body = self.tetrominos[4]
	
	def draw(self, display) -> None:
		for cell in self.body:
			x_pos = (cell.x + self.start.x) * CELL_SIZE
			y_pos = (cell.y + self.start.y) * CELL_SIZE
			cell_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
			pygame.draw.rect(surface=display, color=WHITE, rect=cell_rect)
	
	def move_down(self) -> None:
		self.start += Vector2(0, 1)
	
	def move_horizontally(self, side: Vector2) -> None:
		for cell in self.body:
			cell += side
	
	def rotate(self) -> None:
		print("rotating...")
		pivot = self.body[1]
		print(f"my pivot is at {pivot.x} // {pivot.y}")
		for cell in self.body:
			detla_x = cell.x - pivot.x
			delta_y = cell.y - pivot.y
			print(detla_x, delta_y)
