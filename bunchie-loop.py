
import pygame
from pygame.locals import *

def resize_viewport (w,h):
	"""
	ON RESIZE set new display mode, recalculate bunchie frame size, recreate scaled frames
	"""
	global display_surface, blit_h, blit_w, bunchie_ratio, disp_w, disp_h, bunchie_frames
	global scaled_frames
	
	display_surface = pygame.display.set_mode ((w,h), RESIZABLE|DOUBLEBUF)
	pygame.display.set_caption ("Infinite Bunchie loop with Jean Jacques Perrey's Brazilian Flower"+
		" (also infinitely looped)")

	disp_ratio = float(w)/h

	if disp_ratio > bunchie_ratio:
		blit_h = int(h)
		blit_w = int(bunchie_ratio*h)
	else:
		blit_w = int(w)
		blit_h = int(w/bunchie_ratio)

	disp_w = w
	disp_h = h
	
	scaled_frames = []
	for frame in bunchie_frames:
		scaled_frames.append (pygame.transform.scale (frame, (blit_w,blit_h)))

def init ():
	"""
	initialization: init pygame, pygame.mixer, load bunchie frames, calculate bunchie-ration,
	load music, enque music-intro
	"""
	global bunchie_frames, bunchie_ratio, channel, musicintro, musicloop

	pygame.init()
	
	if not pygame.display.get_init () :
		raise Exception ("pygame.display.get_init() returned False.")

	pygame.mixer.init (frequency=44100, size=16, channels=2)

	bunchie_frames = []
	for i in range(1,12):
		bunchie_frames.append (pygame.image.load ("frames/bunchie-color"+str(i)+".png"))
	bunchie_ratio = float(bunchie_frames[0].get_size()[0])/bunchie_frames[0].get_size()[1]
	
	musicintro = pygame.mixer.Sound ("brazilian-intro.ogg")
	musicloop = pygame.mixer.Sound ("brazilian-loop.ogg")

	channel = pygame.mixer.find_channel ()
	channel.queue (musicintro)
	
	resize_viewport(800,600)

def mainloop():
	"""
	the mainloop: draws bunchie animation, enqueues the musicloop from time to time,
	breaks on QUIT event  
	"""
	global musicloop, display_surface, scaled_frames, disp_w, disp_h, blit_w, blit_h
	curframe = 0
	running = True
	lasttick = 0
	while running:
	
		eventlist = pygame.event.get ()
	
		for event in eventlist:
			if event.type == QUIT:
				running = False
			elif event.type == VIDEORESIZE:
				resize_viewport (event.w, event.h)
		
		if channel.get_queue() == None:
			channel.queue (musicloop)
		
		display_surface.fill ((255,255,255))
		display_surface.blit (scaled_frames[curframe], (disp_w/2 - blit_w/2, disp_h/2 - blit_h/2))
		pygame.display.flip ()
		
		now = pygame.time.get_ticks () 
		if now - lasttick > 60:
			curframe += 1
			if curframe > 10:
				curframe = 0
			lasttick = now

if __name__=="__main__":

	init ()
	mainloop ()
	pygame.quit()

