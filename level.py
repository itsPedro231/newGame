import pygame
from settings import *
from player import Player
from random import randint
from maps import Maps

class Level:
  def __init__(self):

    self.displaySurface = pygame.display.get_surface()
    self.gamePaused = False

    self.visibleSprites = YCamera()
    self.obstacleSprites = pygame.sprite.Group()

    self.currentAttack = None
    self.attackSprites = pygame.sprite.Group()
    self.attackableSprites = pygame.sprite.Group()
    self.buildMap()


  def buildMap(self):
    for idxy, row in enumerate(Maps[1]):
      for idxx, col in enumerate(row): 

        x = idxx * TILESIZE
        y = idxy * TILESIZE
        

        if col == 'g':  
          self.player = Player(
            (x,y),
            [self.visibleSprites], 
            self.obstacleSprites, 
            None, 
            None, )

  



  def run(self):
    self.visibleSprites.customDraw(self.player)

    self.visibleSprites.update()  

class YCamera(pygame.sprite.Group):
  def __init__(self):
    super().__init__()

    self.displaySurface = pygame.display.get_surface()
    self.halfWidth = self.displaySurface.get_size()[0] // 2
    self.halfHeight = self.displaySurface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()    

  def customDraw(self, player):
    self.offset.x = player.rect.centerx - self.halfWidth
    self.offset.y = player.rect.centery - self.halfHeight

    for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
        offsetPos = sprite.rect.topleft - self.offset
        self.displaySurface.blit(sprite.image, offsetPos)         

