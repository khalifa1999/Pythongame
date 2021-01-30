import pygame

pygame.init()

# generer le titre de la fenetre

pygame.display.set_caption("big bang")
pygame.display.set_mode((1080, 700))

running = True
# tant que cette condition est vraie maintenir la fenetre  ouverte

while running:
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
