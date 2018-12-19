from izi_pygame.block import *
from izi_pygame.police import *
from izi_pygame.window import *
from izi_pygame.button import *


class Entry(Button):
	"""
	a place who you can entry a piece of text
	max_char = maximum of char who you can write on an Entry
	"""
	ajust = 2
	list_entry = list()
	def __init__(self, x=0, y=0, width=100, text=str("your text here"), font=None, window=None, cursor=None, max_char=100, text_color=(0,0,0)):
		if len(text) > max_char:
			text = text[:max_char]
		Button.__init__(self, lambda:Entry.focus_callback(self), cursor, x=x, y=y, width=width, 
			text=text, window=window, font=font, ajust=True, ajust_value=Entry.ajust, text_color=text_color)
		self.height = self._text.get_height()
		if text == "your text here":
			text = ""
			self.set_text(text)
		Entry.list_entry.append(self)
		self.begin = False
		self.focus = False
		self.max_char = max_char

	def focus_callback(self):
		"""get the focus of the entry"""
		self.focus = True

	def launch(self):
		"""print the entry"""
		Button.launch(self)
		if self.focus:
			if not self.cursor_collide(self.cursor) and pygame.mouse.get_pressed()[0]:
				self.focus = False

	def __transform_key(self, key_name):
		if key_name == "backspace":
			self._text << self._text.get_text()[:len(self._text.get_text())-1]
		elif key_name == "space":
			self._text >> " "
		elif key_name in ["left shift", "right shift"]:
			pass
		elif key_name == "tab":
			self._text >> "       "
		elif key_name == "return":
			self.focus = False
		else:
			if pygame.key.get_pressed()[K_LSHIFT] or pygame.key.get_pressed()[K_RSHIFT]:
				if key_name == "&":
					self._text >> "1"
				elif key_name == "world 0":
					self._text >> "2"
				elif key_name == "\"":
					self._text >> "3"
				elif key_name == "'":
					self._text >> "4"
				elif key_name == "(":
					self._text >> "5"
				elif key_name == "world 1":
					self._text >> "6"
				elif key_name == "world 3":
					self._text >> "7"
				elif key_name == "!":
					self._text >> "8"
				elif key_name == "world 2":
					self._text >> "9"
				elif key_name == "world 4":
					self._text >> "0"
				else:
					self._text >> key_name.upper()
			else:
				number = False
				for n in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
					if n in key_name:
						self._text >> n
						number = True
						break
				if number == False:
					self._text >> key_name
		if len(self._text.get_text()) > self.max_char:
			self._text << self._text.get_text()[:self.max_char]

	def grab_key(self, key_name):
		"""catch a keyname thanks to the user and update the entry"""
		if not self.begin and self.focus:
			self.begin = True
			self._text << ""
		if self.focus:
			self.__transform_key(key_name)
			
			if not self.cursor_collide(self.cursor) and pygame.mouse.get_pressed()[0]:
				self.focus = False



class Drawentry(Entry):
	"""
	an entry with color as background
	bg = a Drawblock (represents the background)
	bg_focus = a Drawblock (represents the focus)
	"""
	def __init__(self, x=0, y=0, text=str("your text here"), font=None, window=None, cursor=None, max_char=100, text_color=(0,0,0), bg_color=(255,255,255)):
		Entry.__init__(self, x=x, y=y, text=text, font=font, window=window, cursor=cursor, max_char=max_char, text_color=text_color)
		self.bg = Drawblock(x=self.xbegin, y=self.ybegin, width=self.width, height=self.height, speed=5, color=bg_color, fill=0, window=window)
		self.bg_focus = Drawblock(x=self.xbegin, y=self.ybegin, width=self.width, height=self.height, speed=5, color=(0,0,0), fill=1, window=window)

	def launch(self):
		"""draw the entry"""
		self.bg.set_dimension(self.width, self.height)
		self.bg.draw()
		if self.focus:
			self.bg_focus.set_dimension(self.width, self.height)
			self.bg_focus.draw()
		Entry.launch(self)


class Picentry(Entry):
	"""
	an entry with picture as background
	bg = a Picblock (represents the background)
	bg_focus = a Drawblock (represents the focus)
	"""
	def __init__(self, x=0, y=0, text=str("your text here"), font=None, window=None, cursor=None, max_char=100, text_color=(0,0,0), bg_pic=None):
		Entry.__init__(self, x=x, y=y, text=text, font=font, window=window, cursor=cursor, max_char=max_char, text_color=text_color)
		self.bg = Picblock(x=self.xbegin, y=self.ybegin, width=self.width, height=self.height, speed=5, namepic=bg_pic, window=window)
		self.bg_focus = Drawblock(x=self.xbegin, y=self.ybegin, width=self.width, height=self.height, speed=5, color=(0,0,0), fill=1, window=window)

	def launch(self):
		"""print the entry"""
		self.bg.set_dimension(self.width, self.height)
		self.bg.print()
		if self.focus:
			self.bg_focus.set_dimension(self.width, self.height)
			self.bg_focus.draw()
		Entry.launch(self)


class Spriteentry(Entry):
	"""
	an entry with list of pictures as background
	bg = a Spriteblock (represents the background)
	bg_focus = a Drawblock (represents the focus)
	"""
	def __init__(self, x=0, y=0, text=str("your text here"), font=None, window=None, cursor=None, max_char=100, text_color=(0,0,0), sprites=None):
		Entry.__init__(self, x=x, y=y, text=text, font=font, window=window, cursor=cursor, max_char=max_char, text_color=text_color)
		self.bg = Spriteblock(sprites=sprites, x=self.xbegin, y=self.ybegin, width=self.width, height=self.height, speed=5, frequence=10, window=window)
		self.bg_focus = Drawblock(x=self.xbegin, y=self.ybegin, width=self.width, height=self.height, speed=5, color=(0,0,0), fill=1, window=window)

	def launch(self):
		"""print the entry"""
		self.bg.set_dimension(self.width, self.height)
		self.bg.anime()
		if self.focus:
			self.bg_focus.set_dimension(self.width, self.height)
			self.bg_focus.draw()
		Entry.launch(self)














