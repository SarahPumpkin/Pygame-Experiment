import pygame
from pygame.locals import *
import random
import sys

from Ground import Ground
from Player import Player
from Enemy import Enemy
ground = Ground(900, 120, 0, 300, "ground.jpg")
enemy = Enemy(100, 100, 300, 200, "bowser.png")
player = Player(200, 0)
pygame.init()

WIDTH = 800
HEIGHT = 400
FPS = 60
CLOCK = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Cadet")

background =pygame.image.load("skybg.jpg")

GroundGroup = pygame.sprite.Group()
GroundGroup.add(ground)
GroundGroup.add(enemy)

while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pass
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player.jump()
        player.update(GroundGroup)
        display.blit(background, (0, 0))
        ground.render(display)
        player.render(display)
        enemy.render(display)

        pygame.display.update()
        CLOCK.tick(FPS)
