import pygame, pygame.mixer
from pygame.locals import*
import sys


class Window:

	def __init__(self, wlarg=500, whaut=500, wtitle="unknown"):
		self.wlarg = wlarg
		self.whaut = whaut
		self.wtitle = wtitle
		self.win = pygame.display.set_mode((wlarg, whaut))
		pygame.display.set_caption(wtitle)

	def fill(self, color):
		self.win.fill(color)

	def get_canva(self):
		return self.win