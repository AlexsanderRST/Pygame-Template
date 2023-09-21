"""
Alexsander Rosante's creation
"""

from config import *
from pygame.locals import *

import pygame
import scripts.scene as scene

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_w, screen_h))
        pygame.display.set_caption(f'{name} ({version})')
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.loop = True
        self.hovered = pygame.sprite.Group()
        self.scene = None

    def cursor_by_context(self):
        pygame.mouse.set_cursor(
            {0: SYSTEM_CURSOR_ARROW, 1: SYSTEM_CURSOR_HAND}
            [len(self.hovered.sprites())])

    def check_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == QUIT:
                self.loop = False

    def run(self):
        self.scene = scene.Scene(self)
        while self.loop:
            self.check_events()
            self.cursor_by_context()
            self.scene.update()
            self.scene.draw(self.screen)
            pygame.display.update()
            self.clock.tick(fps)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
