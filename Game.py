import pygame 

# SETUP von der PiGame Enginee
screen = pygame.display.set_mode((640,240)) #Fenster erstellen
#Fenstertitel
caption = "Viel gewinnt"
pygame.display.set_caption(caption)
# Hintergrundfarben
red = (255,0,0)
turqies = (0, 255, 255)
screen.fill(turqies)
background = turqies
pygame.init()

#variablen 
running = True # laufen des Games solange True

# Aktive Schleife des Pygames, die den Inhalt updatet
while running:
    pygame.display.update() # Jeden Zyklus das angezeigte Bild aktualisieren
    # Key press erkennen und ausführen Aktionen resultierender Aktionen 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #möglichkeit zum beenden des Games
            running = False # Schleife beendne
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = red
                
            elif event.key == pygame.K_t:
                background = turqies
            screen.fill(background) #neuen Hintergrund entsprechend der gedrückten Taste
                
 # Beenden des Games (nach austreten aus der aaktiven Loop )  
pygame.quit()


