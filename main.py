from izipygame import *

pygame.font.init()
fenetre = Window(1200, 800, "os")
p = Policestr(name=None, size=20, string="text", ftype='sys', color=(250,0,0), window=fenetre.get_canva(), x=0, y=0)

pygame.init()


fini = False
temps = pygame.time.Clock()

while not fini:
	mx,  my = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fini = True
		if event.type == KEYUP:
			if event.key == K_q:
				fini = True
			if event.key == K_a:
				p.set("test")



	temps.tick(60)
	
	fenetre.fill((0,255,20))
	p.write()


	pygame.display.flip()
pygame.quit()


