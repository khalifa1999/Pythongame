import pygame
from game import Game


pygame.init()

# generer le titre de la fenetre

pygame.display.set_caption("big bang")
screen = pygame.display.set_mode((1080, 700))

# importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')



# charger notre jeu

game = Game()

running = True
# tant que cette condition est vraie maintenir la fenetre  ouverte

while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    # appliquer l'image de notre joueur
    screen.blit(game.player.image, game.player.rect)
    print(game.player.rect.x)
    # mouvement de nos personnages
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()



    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # Evenment si le joueur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False


