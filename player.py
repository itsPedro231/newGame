import pygame
from entity import Entity 
from help import importFolder
from settings import *

class Player(Entity):
  def __init__(self, pos, groups, obstacleSprites, createAttack, destroyAttack):
    super().__init__(groups)
    
    self.image = pygame.image.load('images/player.png')
    self.lastSide = 'left'
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0, HITBOX_OFFSET['player'])

    self.playerAssets()
    self.status = 'left'

    self.attacking = False
    self.attackCd = 400
    self.attackTime = None

    self.obstacleSprites = obstacleSprites

    self.createAttack = createAttack
    self.destroyAttack = destroyAttack
    
    self.stats = {'health': 100, 'attack': 10, 'speed': 5}
    self.health = self.stats['health']
    
    self.vulnerable = True
    self.invulnerabilityDuration = 500

  def playerAssets(self):
    charPath = 'images/player/'
    self.animations = {
      'left': [],
      'right': [],
      'left_idle': [],
      'right_idle': [],
      'left_attack': [],
      'right_attack': [],
    }
    for animation in self.animations.keys():
      fullPath = charPath + animation
      self.animations[animation] = 'images/player.png'

  def input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
      self.direction.x = 1
      self.status = 'right'
      self.lastSide

    elif keys[pygame.K_a]:
      self.direction.x = -1
      self.status = 'left'
      self.lastSide = 'left'

    else:
      self.direction.x = 0    

    if keys[pygame.K_SPACE]:
      pass  

  def update(self):
    self.input()
    self.move(self.stats['speed'])