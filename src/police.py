import pygame, pygame.mixer
from pygame.locals import*
import sys
from random import randint
#police = font
pygame.init()
pygame.font.init()

class Fontstring:
	"""
	represents a pygame.Font
	"""
	def __init__(self, name=None, size=20, italic=0, bold=0, underline=0, window=None):
		self.font = pygame.font.Font(name, size)
		self.font.set_italic(italic)
		self.font.set_bold(bold)
		self.font.set_underline(underline)
		self.win = window


class Printstring:
	police = pygame.font.Font(None, 20)
	list_ps = list()
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
		self._color = color
		self._x = x
		self._y = y
		self.main_font = main_font
		Printstring.list_ps.append(self)
	
	def get_color(self):
		return self._color
	def set_color(self, color=None):
		if not color:
			self._color = (randint(0,255),randint(0,255),randint(0,255))
		else:
			self._color = color
		self.refresh()
	color = property(fget=get_color, fset=set_color, doc="the color of the text")

	def get_x(self):
		return self._x
	def set_x(self, x):
		self._x = x
		self.refresh()
	x = property(fget=get_x, fset=set_x, doc="the x position of the Printstring")

	def get_y(self):
		return self._y
	def set_y(self, y):
		self._y = y
		self.refresh()
	y = property(fget=get_y, fset=set_y, doc="the y position of the Printstring")


	def get_width(self):
		"""get the width of the string"""
		return self.string.get_width()

	def get_height(self):
		"""get the height of the string"""
		return self.string.get_height()

	def refresh(self):
		"""update the printed string"""
		self.string = self.main_font.font.render(self.txt, True, self._color)
	
	def write(self):
		"""print the string"""
		self.main_font.win.blit(self.string, (self._x, self._y))

	@classmethod
	def write_all(cls):
		"""print all the strings"""
		for ps in Printstring.list_ps:
			ps.write()
	
	def set_text(self, string):
		"""set the text to print"""
		if type(string) is not str:
			string = str(string)
		self.txt = string
		self.refresh()
	
	def get_text(self):
		"""return the text printed"""
		return self.txt
	
	def set_font(self, name=None, size=20):
		"""set the policename and his size"""
		self.main_font.font = pygame.font.Font(name, size)
		self.refresh()
	
	def set_style(self, it=False, bd=False, ul=False):
		"""set the style of the police"""
		self.main_font.font.set_italic(it)
		self.main_font.font.set_bold(bd)
		self.main_font.font.set_underline(ul)
		self.refresh()
	
	def strcat(self, string):
		"""concatenation"""
		if type(string) is not str:
			string = str(string)
		self.txt += string
		self.refresh()

	def set_position(self, x, y):
		"""set the position of the Printstring"""
		self._x = x
		self._y = y
		self.refresh()

	
	def __rshift__(self, string):
		"""concatenation with >>"""
		if type(string) is not str:
			string = str(string)
		self.txt += string
		self.refresh()
	
	def __lshift__(self, string):
		"""set the text of the string with <<"""
		if type(string) is not str:
			string = str(string)
		self.txt = string
		self.refresh()

	def __str__(self):
		return self.get_text()

	def __repr__(self):
		return "font: {}\nsize: {}\ntext: {}\ncolor: {}\nitalic: {}\nbold: {}\nunderline: {}".format(
			self.policename, self.policesize, self.txt, self._color,
			self.main_font.font.get_italic(), self.main_font.font.get_bold(), self.main_font.font.get_underline()
			)

	def delete(self):
		Printstring.list_ps.remove(self)
		del self

