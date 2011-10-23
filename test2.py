
import pygame
from pygame.locals import *

pygame.init()

stillbunchie = pygame.image.load ("red-bunchie.png")

if not pygame.display.get_init () :
	raise Exception ("pygame.display.get_init() returned False.")

display_surface = pygame.display.set_mode ((800,600), pygame.RESIZABLE)

display_surface.blit (stillbunchie, (0,0))

pygame.display.flip ()

while True:

	event = pygame.event.wait ()
	
	if event.type == QUIT:
		break

pygame.quit()
