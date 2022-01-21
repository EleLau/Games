from cmath import rect
from curses.textpad import rectangle
from typing import Tuple
import pygame 


pygame.font.init()
# SETUP von der PiGame Enginee
screen = pygame.display.set_mode((800,600)) #Fenster erstellen
#Fenstertitel
caption = "Viel gewinnt"
pygame.display.set_caption(caption)
# Hintergrundfarben
red = (255,0,0)
turqies = (0, 255, 255)
GREEN = ( 0,255,0)
black = ( 0,0,0)
screen.fill(turqies)
background = turqies
#start des Games 
pygame.init()

#variablen 
running = True # laufen des Games solange True
showStartScreen = True 

schrift = pygame.font.SysFont("Arial", 30, False, False)#Schrift ausprobiert
text = schrift.render("Start Game",False, black)
txt2 = schrift.render("Back",False,black)
quad = pygame.Rect(300,300,200,35)
while running:
    if showStartScreen :
        #Startbildschirm.startScreenScene()
         while showStartScreen:
            screen.blit(text,(325,300))
            pygame.draw.rect(screen,black,quad,2)
            pygame.display.update() # Jeden Zyklus das angezeigte Bild aktualisieren
            # Key press erkennen und ausführen Aktionen resultierender Aktionen 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: #möglichkeit zum beenden des Games
                    showStartScreen = False # Schleife beendne
                if event.type == pygame.KEYDOWN: # Einzelzuweisung der Tasten

                    # Key zuweisung über Dictonary (paare von Datensetzen ) für Hintergrundfarben
                    key_dict = {pygame.K_b:black, pygame.K_r:red, pygame.K_g:GREEN,pygame.K_t:turqies}
                    # überprüfen ob die gedrückte Taste im Diconary zugewiesen wurden (nur Hintergrundfarbe)
                    if event.key in key_dict:
                        background = key_dict[event.key]
                #mausklick für den Startscreen:
                if event.type == pygame.MOUSEBUTTONDOWN: #wenn die Maus gedrückt wird 
                    x = pygame.mouse.get_pos()[0]   #x position des Mauscursors 
                    y = pygame.mouse.get_pos()[1]   #y ""
                    if x > 300 and x < 500 and y > 300 and y < 335: #check ob der cursor im Feld ist 
                        showStartScreen = False     #macht den Startbildschirm aus 
            screen.fill(background) #neuen Hintergrund entsprechend der gedrückten Taste
    else:   
        screen.blit(txt2,(325,300))
        pygame.draw.rect(screen,black,quad,2)
        # Aktive Schleife des Pygames, die den Inhalt updatet
        pygame.display.update() # Jeden Zyklus das angezeigte Bild aktualisieren
        # Key press erkennen und ausführen Aktionen resultierender Aktionen 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #möglichkeit zum beenden des Games
                running = False # Schleife beendne
            if event.type == pygame.KEYDOWN: # Einzelzuweisung der Tasten
                '''if event.key == pygame.K_r:
                background = red
            elif event.key == pygame.K_t:
                background = turqies'''
                # Key zuweisung über Dictonary (paare von Datensetzen ) für Hintergrundfarben
                key_dict = {pygame.K_b:black, pygame.K_r:red, pygame.K_g:GREEN,pygame.K_t:turqies}
                # überprüfen ob die gedrückte Taste im Diconary zugewiesen wurden (nur Hintergrundfarbe)
                if event.key in key_dict:
                    background = key_dict[event.key]
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 300 and x < 500 and y > 300 and y < 335:
                    showStartScreen = True 
        screen.fill(background) #neuen Hintergrund entsprechend der gedrückten Taste
          
 # Beenden des Games (nach austreten aus der aaktiven Loop )  
pygame.quit()


