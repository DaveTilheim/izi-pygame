import pygame, pygame.mixer
from pygame.locals import*
import sys

class Policestr:

	def __init__(self, name=None, size=20, string="text", ftype='sys', color=(0,0,0), window=None, x=0, y=0):
		if ftype is sys:
			self.police = pygame.font.SysFont(name, size)
		else:
			self.police = pygame.font.Font(name, size)
		self.string = self.police.render(string, True, color)
		self.color = color
		if window is None:
			print("police error: no window")
			sys.exit(0)
		self.window = window
		self.x = x
		self.y = y

	def write(self):
		self.window.blit(self.string, (self.x, self.y))

	def set_string(self, string):
		self.string = self.police.render(string, True, self.color)



