TILESIZE = 64
from random import randint
# map generator -> matrix h*w
class Map:
  def __init__(self):
    self.map = [[]]
    
  # basic map with walls, floor and ceiling
  def base(self, height, width):
    height += 1
    width += 2 
    for x in range(0, height):
      self.map.append([])
      for y in range(0, width):
        self.map[x].append(' ')
        if x == height-1:
          self.map[height].append(' ')    

    for x in range(0,width):
      self.map[0][x] = 'c'
      self.map[len(self.map)-1][x] = 'f'

    for x in range(1,len(self.map)-1):
      self.map[x][0] = 'w'
      self.map[x][len(self.map[x])-1] = 'w'  

    for x in self.map:
      print(x)
    # print(map)  

    self.rng()

  # random generator for platforms, mobs and items
  def rng(self):
    # ammount of platforms per level
    platAmmount = randint(1, len(self.map)//3)
    platLen = []
    availablePos = []
    posx = []
    posy = []
    
    x = 1
    # platforms' lengths
    while x < platAmmount+1:
      platLen.append(randint(len(self.map)//3, len(self.map)//2))
      
      x+=1
      print(platAmmount, platLen)
    
    # position of the platforms
    for x in range(3, len(self.map)-3):
      availablePos.append(self.map[x])
    
    platPos = availablePos
    for x in range(0, platAmmount):
      num = randint(0, len(availablePos))
      if num not in posx: posx.append(num)
    print(posx)
    for x in availablePos:  
      print(x)  
# im testing
map = Map()
map.base(10,10)


