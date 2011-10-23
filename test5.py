
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init (frequency=44100, size=16, channels=2)

if not pygame.display.get_init () :
	raise Exception ("pygame.display.get_init() returned False.")

display_surface = pygame.display.set_mode ((800,600), pygame.RESIZABLE)

firstpart = pygame.mixer.Sound ("brazilian-intro.ogg")
looppart = pygame.mixer.Sound ("brazilian-loop.ogg")
chann = pygame.mixer.find_channel ()
chann.queue (firstpart)

running = True
while running:

	eventlist = pygame.event.get ()

	for event in eventlist:
		if event.type == pygame.QUIT:
			running = False
	
	if chann.get_queue() == None:
		chann.queue (looppart)

	pygame.time.wait (10)

pygame.quit()
