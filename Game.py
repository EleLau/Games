import pygame 


screen = pygame.display.set_mode((640,240))
caption = "Viel gewinnt"
pygame.display.set_caption(caption)
red = (255,0,0)
turqies = (0, 255, 255)
screen.fill(turqies)
background = turqies
pygame.init()


running = True

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = red
                
            elif event.key == pygame.K_t:
                background = turqies
            screen.fill(background)
                


    
pygame.quit()


