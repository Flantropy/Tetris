import sys
import pygame
from pygame.locals import *
from pygame.math import Vector2
from classes.tetromino import Tetromino
from constants import *


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.update = pygame.USEREVENT
        pygame.time.set_timer(self.update, UPDATE_RATE)
        self.tetromino = Tetromino()
        self.grid = [Vector2(x, y)
                     for x in range(CELLS_IN_HORIZONTAL)
                     for y in range(CELLS_IN_VERTICAL)]
        self.occupied_cells = []
    
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.shut_down()
                if event.type == self.update:
                    self.update_state()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.tetromino.rotate()
                    if event.key == K_a:
                        self.tetromino.move(Vector2(-1, 0))
                    if event.key == K_i:
                        self.tetromino.move(Vector2(1, 0))
                        
            self.render_gfx()
            self.clock.tick(FPS)
    
    def render_gfx(self) -> None:
        self.display.fill(BLACK)
        self.draw_grid()
        self.draw_occupied_cells()
        self.draw_tetromino()
        pygame.display.update()
    
    def update_state(self) -> None:
        self.tetromino.occupied_cells_on_gird = self.occupied_cells
        if self.tetromino.move(Vector2(0, 1)):
            return
        self.occupied_cells.extend(self.tetromino.get_vectors())
        self.tetromino = Tetromino()
        self.clear_filed_lines()
    
    def clear_filed_lines(self) -> None:
        lines = {}
        for line in range(CELLS_IN_VERTICAL):
            lines[line] = len([v for v in self.occupied_cells if v.y == line])
        for key, value in lines.items():
            if value == CELLS_IN_HORIZONTAL:
                for vector in self.occupied_cells.copy():  # removing filled line
                    if vector.y == key:
                        self.occupied_cells.remove(vector)
                for vector in self.occupied_cells:  # shift lines down
                    if vector.y < key:
                        vector += Vector2(0, 1)
    
    @staticmethod
    def shut_down():
        pygame.quit()
        sys.exit()
        
    def draw_grid(self) -> None:
        for vector in self.grid:
            self.draw_cell(vector=vector, color=GREY)
    
    def draw_tetromino(self) -> None:
        for vector in self.tetromino.get_vectors():
            self.draw_cell(vector=vector, color=self.tetromino.color, width=CELL_SIZE)
        
    def draw_occupied_cells(self) -> None:
        for vector in self.occupied_cells:
            self.draw_cell(vector=vector, color=WHITE, width=CELL_SIZE)
            
    def draw_cell(self, vector: Vector2, color: tuple, width=1, border_radius=1) -> None:
        pygame.draw.rect(
            surface=self.display,
            color=color,
            rect=pygame.Rect(vector.x * CELL_SIZE,
                             vector.y * CELL_SIZE,
                             CELL_SIZE, CELL_SIZE),
            width=width,
            border_radius=border_radius)
