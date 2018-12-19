import pygame, pygame.mixer
from pygame.locals import*
import sys


class Window:
	"""
	Window -> create a basic pygame window
	win: the pygame window -> pygame.Surface()
	wwidth = width of the window
	wheight = height of the window
	wtitle = title of the window
	"""
	def __init__(self, wwidth=500, wheight=500, wtitle="unknown"):
		self._wwidth = wwidth
		self._wheight = wheight
		self._wtitle = wtitle
		self.win = pygame.display.set_mode((wwidth, wheight))
		pygame.display.set_caption(wtitle)
	
	def get_wtitle(self):
		return self._wtitle
	def set_title(self, string):
		self._wtitle = string
		pygame.display.set_caption(string)
	wtitle = property(get_wtitle, set_title, "the title of the Window")

	def get_wwidth(self):
		return self._wwidth
	def set_wwidth(self, width):
		self.set_size(width, self._wheight)
	wwidth = property(fget=get_wwidth, fset=set_wwidth, doc="the width of the window")

	def get_wheight(self):
		return self._wheight
	def set_wheight(self, height):
		self.set_size(self._width, height)
	wheight = property(fget=get_wheight, fset=set_wheight, doc="the height of the window")

	
	def fill(self, color):
		"""same role as Surface.fill()"""
		self.win.fill(color)
	
	def get_canva(self):
		"""return the pygame window"""
		return self.win
	surface = get_canva
	
	def set_size(self, wwidth=500, wheight=500):
		"""set the size of the window"""
		self._wwidth = wwidth
		self._wheight = wheight
		self.win = pygame.display.set_mode((wwidth, wheight))
