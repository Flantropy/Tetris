import sys
from typing import List

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
        self.stuck_tetrominoes: List[Tetromino] = []
    
    def run(self):
        while True:
            # HANDLING EVENTS
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
            
            # RENDER
            self.display.fill(BLACK)
            self.tetromino.draw(self.display)
            for tetromino in self.stuck_tetrominoes:
                tetromino.draw(self.display)
            pygame.display.update()
            
            # TICK CLOCK
            self.clock.tick(FPS)
    
    def update_state(self):
        if not self.tetromino.check_collisions(self.stuck_tetrominoes):
            self.tetromino.move(Vector2(0, 1))
        else:
            # self.tetromino.position -= Vector2(0, -1)
            self.stuck_tetrominoes.append(self.tetromino)
            self.tetromino = Tetromino()
        print([(v.x, v.y) for v in Tetromino.body_to_vectors(self.tetromino)])
        
    @staticmethod
    def shut_down():
        pygame.quit()
        sys.exit()
