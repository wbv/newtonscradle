import pygame
from pygame.locals import *

screen = pygame.display.set_mode((1024,768), DOUBLEBUF)
bgcolor = pygame.color.Color(255, 255, 255, 255)
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y):
        self.set_pos(x, y)

    def set_pos(self, x, y):
        self.surface = pygame.image.load('ball.png').convert()
        self.x = x
        self.y = y

    def get_height(self):
        return self.surface.get_size()[1]

    def get_width(self):
        return self.surface.get_size()[0]


    def draw(self):
        screen.blit(self.surface, self.surface.get_rect().move(self.x, self.y))


def main():
    ball = Ball(0,0)

    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                exit()
        screen.fill(bgcolor)

        ball.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()