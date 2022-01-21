from turtle import getscreen
import pygame
import Game
pygame.font.init()

schrift = pygame.font.SysFont("Arial", 30, False, False)
text = schrift.render("Start Game",True, (0,0,0))


'''def textZeigen():
    screen.blit(text,[100,100]) 
    print("done")'''

#textZeigen()
def startScreenScene(gamescreen):
    screen = gamescreen
    showStart = True
    # Aktive Schleife des Pygames, die den Inhalt updatet
    while showStart:
        pygame.display.update() # Jeden Zyklus das angezeigte Bild aktualisieren
        # Key press erkennen und ausführen Aktionen resultierender Aktionen 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #möglichkeit zum beenden des Games
                showStart = False # Schleife beendne
            if event.type == pygame.KEYDOWN: # Einzelzuweisung der Tasten

                # Key zuweisung über Dictonary (paare von Datensetzen ) für Hintergrundfarben
               #key_dict = {pygame.K_b:black, pygame.K_r:red, pygame.K_g:GREEN,pygame.K_t:turqies}
                # überprüfen ob die gedrückte Taste im Diconary zugewiesen wurden (nur Hintergrundfarbe)
            #if event.key in key_dict:
            #    background = key_dict[event.key]