import pygame

# initialise
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")

# set the background color
background_color = (255, 255, 255)

# set the clock
clock = pygame.time.Clock()

# main loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # clear
    screen.fill(background_color)    
    
    # update
    pygame.display.update()
    
    # wait for the next frame
    clock.tick(60)

# quit 
pygame.quit()
