import sys
import pygame
from classes.tetromino import Tetromino
from pygame.locals import *
from constants import *
from pygame.math import Vector2


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.update = pygame.USEREVENT
        pygame.time.set_timer(self.update, UPDATE_RATE)
        self.tetromino = Tetromino()
    
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
            pygame.display.update()
            
            # TICK CLOCK
            self.clock.tick(FPS)
    
    def update_state(self):
        self.tetromino.move(Vector2(0, 1))
        print(self.tetromino.position.x)
    
    @staticmethod
    def shut_down():
        pygame.quit()
        sys.exit()
