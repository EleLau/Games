import pygame
import Game
schrift = pygame.font.SysFont("Arial", 30, False, False)
text = schrift.render("Start Game",True, (0,0,0))

screen = Game.screen
def textZeigen():
    screen.blit(text,[100,100]) 
    print("done")

textZeigen()
    