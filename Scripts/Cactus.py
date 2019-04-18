import pygame as pg


class Cactus(pg.sprite.Sprite):
    def __init__(self,xPos,yPos,width,height,source, sourceIndex):
        pg.sprite.Sprite.__init__(self)
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.source = source
        self.sourceIndex = sourceIndex
        self.img = pg.image.load(self.source[sourceIndex])
        self.cactImg = pg.transform.scale(self.img,(self.width,self.height))
        self.collider = self.cactImg.get_rect()
        # TODO: List of cactus objects instead of just one.

    def moveCact(self, xSpeed):
        self.xPos -= xSpeed / 5

    def getCollider(self):
        self.collider = self.cactImg.get_rect(center=(self.xPos + (self.cactImg.get_width() / 2)
                                                      ,self.yPos + (self.cactImg.get_height() / 2)))
        self.collider.inflate_ip(-2,-2)
        return self.collider


