import pygame
import requests
from io import BytesIO
import heros
import move

pygame.display.set_caption("Tittle")

url = "https://i.imgur.com/K4A9jQv.png"

response = requests.get(url)

image = BytesIO(response.content)

fond = pygame.image.load(image)

pygame.init()



largeur = 600
hauteur = 480
FPS = 1



ecran = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)


Heros = pygame.draw.rect
hX = 0
hY = 0
hVX = 1
hVY = 0


boucle = True

while boucle:
    ecran.blit(fond, (0, 0))
    Heros(ecran, (255,255,255), (hX, hY, 30, 0))
    hX += hVX
    hY += hVY
    hVX += 0.1
    hVY += 0.1
    for event in pygame.event.get():
        if event.type == pygame.K_RIGHT:
            boucle = False
        elif event.type == pygame.K_LEFT:
            boucle = False
        elif event.type == pygame.QUIT:
            boucle = False
    pygame.display.flip()


pygame.quit()