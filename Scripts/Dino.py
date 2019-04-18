import pygame as pg
from pygame import *
import Scripts.Vector2 as VC2


class Player(pg.sprite.Sprite):
    def __init__(self,playerWidth,playerHeight,destination, cl):
        pg.sprite.Sprite.__init__(self)
        pg.init()
        self.playerSize = self.playerWidth, self.playerHeight = playerWidth,playerHeight
        self.img = image.load(destination)
        self.player = transform.scale(self.img,self.playerSize)

        self.xSpeed = 1
        self.playerPos = VC2.Vector2(0, 0)
        self.collider = self.player.get_rect(center=(self.playerPos.x, self.playerPos.y))
        self.velocity = 0
        self.isGrounded = False
        self.clock = cl

    def jump(self, yPower, gravity):
        self.velocity -= gravity
        if self.isGrounded is True:
            if self.velocity <= 0:
                self.velocity = yPower
                self.isGrounded = False

        else:
            self.velocity -= gravity

        self.playerPos.y -= self.velocity / self.clock.get_time()
        self.getCollider()

    def getCollider(self):

        self.collider = self.player.get_rect(center=(self.playerPos.x + (self.player.get_width() / 2),
                                                     self.playerPos.y + self.player.get_height() / 2))
        self.collider.inflate_ip(-2,2)
        self.collider.right -= 3
        return self.collider
