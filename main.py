import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    # load player sprite
    self.image = pygame.image.load("sprites/player/dinosaur/run1.png")
    self.rect = self.image.get_rect()
    # initial position
    self.rect.x = x
    self.rect.y = y
    # initial speed
    self.speed = 5

  def update(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
      self.rect.y -= self.speed
    if key[pygame.K_DOWN]:
      self.rect.y += self.speed

# initialise
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dino Run")

# set the background color
background_color = (255, 255, 255)

# background objects initialisation
floor = pygame.image.load("sprites/others/floor.png")
cloud = pygame.image.load("sprites/others/cloud.png")

# player initialisation
player = Player(100, 100)
player_group = pygame.sprite.Group()
player_group.add(player)

# set the clock
clock = pygame.time.Clock()

# main loop
running = True
while running:
  # handle events
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
  
  # backgroundm objects
  screen.fill(background_color)    
  screen.blit(floor, (0, 500))
  
  # update player sprite
  player.update()
  player_group.draw(screen)

  # update
  pygame.display.update()
  
  # wait for the next frame
  clock.tick(60)

# quit 
pygame.quit()
