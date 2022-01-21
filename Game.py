from cmath import rect
from curses.textpad import rectangle
import pygame 


pygame.font.init()
# SETUP von der PiGame Enginee
screen = pygame.display.set_mode((640,240)) #Fenster erstellen
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
text = schrift.render("Start Game",False, (0,0,0))
if showStartScreen :
    #Startbildschirm.startScreenScene()
     while showStartScreen:
        screen.blit(text,(60,40))
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
            
            screen.fill(background) #neuen Hintergrund entsprechend der gedrückten Taste
            

else:
    pass
# Aktive Schleife des Pygames, die den Inhalt updatet
while running:
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

        screen.fill(background) #neuen Hintergrund entsprechend der gedrückten Taste
          
 # Beenden des Games (nach austreten aus der aaktiven Loop )  
pygame.quit()

#Grade geht iwas mit dem Text noch nicht, weiß nicht woran das liegt xD
