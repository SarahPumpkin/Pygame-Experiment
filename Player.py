import pygame
from pygame.locals import *

vec = pygame.math.Vector2

animation_left_run = [pygame.image.load("Images/tile009.png"), pygame.image.load("Images/tile010.png"),
                   pygame.image.load("Images/tile011.png"), pygame.image.load("Images/tile012.png"),
                   pygame.image.load("Images/tile013.png"), pygame.image.load("Images/tile014.png"),
                   pygame.image.load("Images/tile015.png"), pygame.image.load("Images/tile016.png"),
                   pygame.image.load("Images/tile017.png")]
animation_right_run = [pygame.image.load("Images/tile018.png"), pygame.image.load("Images/tile019.png"),
                   pygame.image.load("Images/tile020.png"), pygame.image.load("Images/tile021.png"),
                   pygame.image.load("Images/tile022.png"), pygame.image.load("Images/tile023.png"),
                   pygame.image.load("Images/tile024.png"), pygame.image.load("Images/tile025.png"),
                   pygame.image.load("Images/tile026.png")]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("Images/tile018.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        #Player information
        self.pos = vec(x, y)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)
        #Player constants
        self.ACC = 0.7
        self.FRIC = -.1
        #Player movements
        self.jumping = False
        self.running = False
        self.direction = "RIGHT"
        self.move_frame = 0


    def move(self):
        self.acc = vec(0, 0.5)

        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        keys = pygame.key.get_pressed()


        if keys[K_LEFT]:
            self.acc.x = -self.ACC
            self.image = animation_left_run[self.move_frame]
            self.direction = "LEFT"
        if keys[K_RIGHT]:
            self.acc.x = self.ACC
            self.image = animation_right_run[self.move_frame]
            self.direction = "RIGHT"
            ## self.image = pygame.transform.scale(self.image, (100, 100))
        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.topleft = self.pos
    def walking(self):
        if self.move_frame > 6:
            self.move_frame = 0
            return
        if self.jumping == False and self.running == True:
            if self.vel.x >= 0:
                self.image = animation_right_run[self.move_frame]
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = animation_left_run[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1
        if self.running == False and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "LEFT":
                self.move_frame = 0
                self.image = animation_left_run[self.move_frame]
            elif self.direction == "RIGHT":
                self.move_frame = 0
                self.image = animation_right_run[self.move_frame]
    def update(self, group):
        self.collision(group)
        self.walking()
        self.move()
        #self.horizontalcollision(group)

    def collision(self, group):
        hits = pygame.sprite.spritecollide(self, group, False)
        if self.vel.y > 0:
            if hits:
                for i in hits:
                    x = 0
                    lowest = hits[x]
                    print("Hits[x] is ", hits[x], "!")
                    if self.rect.bottom >= lowest.rect.top:
                        self.pos.y = lowest.rect.top - self.rect.height + 1
                        self.rect.y = lowest.rect.top - self.rect.height + 1
                        self.vel.y = 0
                        self.jumping = False
                    if self.rect.right > lowest.rect.left and self.direction == "RIGHT":
                        if len(hits) > 1:
                            x += 1
                            lowest = hits[x]
                            self.pos.x = lowest.rect.left - self.rect.width + 1
                            self.rect.x = lowest.rect.left - self.rect.width + 1
                            self.vel.x = 0
                    if self.rect.left < lowest.rect.right and self.direction == "LEFT":
                        if len(hits) > 1:
                            x += 1
                            lowest = hits[x]
                            self.pos.x = lowest.rect.right # + self.rect.width - 1
                            self.rect.x = lowest.rect.right # + self.rect.width - 1
                            self.vel.x = 0


    def jump(self):
        if self.jumping == False:
            self.jumping = True
            self.vel.y = -10



    def render(self, display):
        display.blit(self.image,self.pos)