
import pygame
from pygame.locals import *

pygame.init()

if not pygame.display.get_init () :
	raise Exception ("pygame.display.get_init() returned False.")

display_surface = pygame.display.set_mode ((800,600), pygame.RESIZABLE)

while True:

	event = pygame.event.wait ()
	
	if event.type == QUIT:
		break

pygame.quit()
