import pygame, pygame.mixer
from pygame.locals import*
import sys

class Block:

	nb_block = 0
	list_block = []
	def __init__(self, x=0, y=0, larg=100, haut=100, speed=5):
		self.xbegin = x
		self.ybegin = y
		self.larg = larg
		self.haut = haut
		self.xend = x+larg
		self.yend = y+haut
		self.speed = speed
		self.id = Block.nb_block
		self.time = pygame.time.get_ticks()/1000
		Block.nb_block += 1
		Block.list_block.append(self)

	def set_position(self, x, y):
		self.xbegin = x
		self.ybegin = y
		self.xend = x+self.larg
		self.yend = y+self.haut

	def set_mouse_position(self, pos="center"):
		mx,  my = pygame.mouse.get_pos()
		if pos is "origin":
			self.set_position(mx, my)
		elif pos is "center":
			self.set_position(mx-self.larg//2, my-self.haut//2)


	def move(self, direction):
		if direction == "right":
			self.xbegin += self.speed
		elif direction == "left":
			self.xbegin -= self.speed
		elif direction == "up":
			self.ybegin -= self.speed
		elif direction == "down":
			self.ybegin += self.speed

	def gravity(self, g=10):
		self.speed = g*self.time
		self.ybegin += self.speed
		self.time = pygame.time.get_ticks()/1000

	def delete_from_class_list(self):
		del Block.list_block[self.id]
		Block.nb_block -= 1

	def cursor_collide(self, cursor):
		if cursor.xbegin >= self.xbegin and cursor.xbegin <= self.xend and cursor.ybegin >= self.ybegin and cursor.ybegin <= self.yend:
			return True
		return False

	def press_cursor_collide(self, cursor):
		if pygame.mouse.get_pressed()[0] and self.cursor_collide(cursor):
			return True
		return False
		#cursor -> 1px/1px
	def event(self, callback, args=None):
			if args == None:
				callback()
			else:
				callback(args)



class Drawblock(Block):

	def __init__(self, x=0, y=0, larg=100, haut=100, speed=5, color=(255,255,255), fill=0, window=None):
		Block.__init__(self, x, y, larg, haut, speed)
		if window is None:
			print("Error: no window to draw block-id #{}".format(self.id))
			sys.exit(0)
		self.color = color
		self.window = window
		self.fill = fill

	def draw(self, form="rect"):
		if form is "rect":
			pygame.draw.rect(self.window, self.color, (self.xbegin, self.ybegin, self.larg, self.haut), self.fill)
		elif form is "circle":
			pygame.draw.circle(self.window, self.color, (int(self.xbegin), int(self.ybegin)), self.larg//2, self.fill)

class Picblock(Block):

	def __init__(self, x=0, y=0, larg=100, haut=100, speed=0, pic="unknown", window=None):
		Block.__init__(self, x, y, larg, haut, speed)
		if window is None:
			print("Error: no window to print block-id #{}".format(self.id))
			sys.exit(0)
		elif pic is "unknown":
			print("Error: impossible to load picture about block-id #{}".format(self.id))
			sys.exit(0)
		self.window = window
		self.namepic = pic
		self.pic = pygame.image.load(self.namepic).convert_alpha()
		self.pic = pygame.transform.scale(self.pic, (self.larg, self.haut))

	def print(self):
		self.window.blit(self.pic, (self.xbegin, self.ybegin))





