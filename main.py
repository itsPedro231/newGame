import pygame
import sys
from settings import Map

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
  def run(self):
    Map().base(20,10)
    # while True:
    #   for event in pygame.event.get():

    #     if event.type == pygame.QUIT:
    #       pygame.quit()
    #       sys.exit()

    #   self.screen.fill('black')
    #   pygame.display.update()  
    

if __name__ == '__main__':
  Game().run()
