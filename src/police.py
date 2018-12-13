import pygame, pygame.mixer
from pygame.locals import*
import sys
from random import randint
#police = font
pygame.init()
pygame.font.init()

class Fontstring:

	def __init__(self, name=None, size=20, italic=0, bold=0, underline=0, window=None):
		self.font = pygame.font.Font(name, size)
		self.font.set_italic(italic)
		self.font.set_bold(bold)
		self.font.set_underline(underline)
		self.win = window


class Printstring:
	police = pygame.font.Font(None, 20)
	"""
	Policestr -> create a drawing string and the police
	main_font = Fontstring()
	txt = text to assign the police
	string = texte to print
	color = color of the string
	window = pygame.Surface()
	x and y = position of the text
	"""
	def __init__(self, main_font, string="text", color=(0,0,0), x=0, y=0):
		self.txt = string
		self.string = main_font.font.render(string, True, color)
		self.color = color
		self.x = x
		self.y = y
		self.main_font = main_font
	"""set a new color"""
	def set_color(self, color=None):
		if not color:
			self.color = (randint(0,255),randint(0,255),randint(0,255))
		else:
			self.color = color
		self.refresh()
	def get_width(self):
		return self.string.get_width()
	def get_height(self):
		return self.string.get_height()
	"""update the printed string"""
	def refresh(self):
		self.string = self.main_font.font.render(self.txt, True, self.color)
	"""print the string"""
	def write(self):
		self.main_font.win.blit(self.string, (self.x, self.y))
	"""set the text to print"""
	def set_text(self, string):
		if type(string) is not str:
			string = str(string)
		self.txt = string
		self.refresh()
	"""return the text printed"""
	def get_text(self):
		return self.txt
	"""set the policename and his size"""
	def set_font(self, name=None, size=20):
		self.main_font.font = pygame.font.Font(name, size)
		self.refresh()
	"""set the style of the police"""
	def set_style(self, it=False, bd=False, ul=False):
		self.main_font.font.set_italic(it)
		self.main_font.font.set_bold(bd)
		self.main_font.font.set_underline(ul)
		self.refresh()
	"""concatenation"""
	def strcat(self, string):
		if type(string) is not str:
			string = str(string)
		self.txt += string
		self.refresh()

	"""concatenation with >>"""
	def __rshift__(self, string):
		if type(string) is not str:
			string = str(string)
		self.txt += string
		self.refresh()
	"""set the text of the string with <<"""
	def __lshift__(self, string):
		if type(string) is not str:
			string = str(string)
		self.txt = string
		self.refresh()

	def __str__(self):
		return self.get_text()

	def __repr__(self):
		return "font: {}\nsize: {}\ntext: {}\ncolor: {}\nitalic: {}\nbold: {}\nunderline: {}".format(
			self.policename, self.policesize, self.txt, self.color,
			self.main_font.font.get_italic(), self.main_font.font.get_bold(), self.main_font.font.get_underline()
			)



