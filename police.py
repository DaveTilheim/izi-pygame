import pygame, pygame.mixer
from pygame.locals import*
import sys

class Policestr:
	"""
	Policestr -> create a drawing string and it police
	"""
	def __init__(self, name=None, size=20, string="text", color=(0,0,0), window=None, x=0, y=0, italic=0, bold=0, underline=0):
		self.police = pygame.font.Font(name, size)
		self.police.set_italic(italic)
		self.police.set_bold(bold)
		self.police.set_underline(underline)
		self.policename = name
		self.policesize = size
		self.txt = string
		self.string = self.police.render(string, True, color)
		self.color = color
		if window is None:
			print("police error: no window")
			sys.exit(0)
		self.window = window
		self.x = x
		self.y = y

	def refresh(self):
		self.string = self.police.render(self.txt, True, self.color)

	def write(self):
		self.window.blit(self.string, (self.x, self.y))

	def set_text(self, string):
		if type(string) is not str:
			string = str(string)
		self.txt = string
		self.refresh()

	def set_font(self, name=None, size=None):
		if name is not None:
			self.policename = name
		if size is not None:
			self.policesize = size
		self.police = pygame.font.Font(self.policename, self.policesize)
		self.refresh()

	def set_style(self, it=False, bd=False, ul=False):
		self.police.set_italic(it)
		self.police.set_bold(bd)
		self.police.set_underline(ul)
		self.refresh()

	#Police >> "str"
	def __rshift__(self, string):
		if type(string) is not str:
			string = str(string)
		self.txt = string
		self.refresh()



