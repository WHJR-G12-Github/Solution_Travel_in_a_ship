import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=500
height=400
screen = pygame.display.set_mode((width,height))

# Loading images
# Creating an empty dictionary 'images'
images={}
# Loading the background image 'sea.png' into the 'images' dictionary under the name 'bg'. Now, 'images["bg"]' refers to the background image
images["bg"] = pygame.image.load("sea.png").convert_alpha()
# Loading the ship image 'ship.png' into the 'images' dictionary under the name 'ship'. Now, 'images["ship"]' refers to the ship image
images["ship"] = pygame.image.load("ship.png").convert_alpha()

# Creating a variable 'bgx' to hold x-axis value of background image and initialize it to zero (Eg. a=0 . Here, variable 'a' is created & initialized to zero)
bgx=0

while True:    
    screen.fill((50,150,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Decrementing the value of 'bgx' by 5 to move the background 
    bgx=bgx-5
    
    # Code to reset bgx to 0 after bgx becomes less then -1000
    # Checking if 'bgx' is less than -1000 
    if   bgx < -1000  :
        # Resetting the value of 'bgx' to zero
        bgx=0
    
    # Displaying the ship image at the coordinates '[100,150]'
    screen.blit(images["ship"],[100,150]) 
    # Displaying the background image at the coordinates '[bgx,0]'
    screen.blit(images["bg"],[bgx,0])
     
    
   
    pygame.display.update()
    clock.tick(30)
