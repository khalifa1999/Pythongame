import pygame

pygame.init()

# generer le titre de la fenetre

pygame.display.set_caption("big bang")
screen = pygame.display.set_mode((1080, 700))

# importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')


running = True
# tant que cette condition est vraie maintenir la fenetre  ouverte

while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
