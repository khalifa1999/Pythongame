import pygame
from game import Game
from player import Player

pygame.init()







# generer le titre de la fenetre

pygame.display.set_caption("big bang")
screen = pygame.display.set_mode((1080, 700))

# importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# charger player
player = Player()

# charger notre jeu

game = Game()

running = True
# tant que cette condition est vraie maintenir la fenetre  ouverte

while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de notre joueur
    screen.blit(game.player.image, game.player.rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #Evenment si le joueur appuie sur une touche
        elif event.type == event.KEYDOWN:
            #detecter la touche qui a ete appuyee
            if event.type == pygame.K_RIGHT:
                #deplacement vers la droite

            elif event.type == pygame.K_LEFT:
                #deplacement vers la gauche

