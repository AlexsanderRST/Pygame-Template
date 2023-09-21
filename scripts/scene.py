import pygame


class Scene:
    def __init__(self, game):
        self.game = game
        self.bg_color = 'black'
        self.drawables = pygame.sprite.LayeredUpdates()
        self.updatables = pygame.sprite.Group()

    def check_events(self):
        for event in self.game.events:
            pass

    def draw(self, surface: pygame.Surface):
        self.drawables.draw(surface)

    def update(self):
        self.check_events()
        self.updatables.update()
