from izi_pygame.block import *
from izi_pygame.police import *
from izi_pygame.window import *


class Button(Block):
	"""
	A Block which you can attach a callback function. Run it when you click on the button
	callback = the callback function
	cursor = a Cursor object
	text = the text of the button
	ajust = True -> the text is centralized
	ajust_value = padding
	"""
	list_button = list()
	def __init__(self, callback, cursor, x=0, y=0, width=100, height=50, text=None, text_color=(0,0,0), window=None, font=None, ajust=False, ajust_value=0):
		Block.__init__(self, x=x, y=y, width=width, height=height)
		self.callback = callback
		self.click = False
		self.cursor = cursor
		self._text = None
		self.sensitive = True
		self.ajust = ajust
		self.ajust_value = ajust_value
		if text and window and font:
			if type(text) is Printstring:
				self._text = text
			else:
				self._text = Printstring(main_font=font, string=text, color=text_color, x=0, y=0)
			self.ajust_button()
		Button.list_button.append(self)

	def get_text(self):
		if self._text:
			return self._text.get_text()
		return None
	def set_text(self, text):
		if type(text) == str:
			self._text << text
		else:
			self._text = text
	text = property(fget=get_text, fset=set_text, doc="the text of the button")

	def set_sensitive(self, boolean):
		"""set the sensitivity of the button"""
		self.sensitive = boolean

	def ajust_button(self):
		"""reorganise the position and the size of the button"""
		self._text.set_position(self.xbegin+self.ajust_value, self.ybegin+self.ajust_value)
		if self.ajust:
			self.set_dimension(self._text.get_width()+self.ajust_value*2, self._text.get_height()+self.ajust_value*2) 
	
	def launch(self):
		"""print the button and wait detection"""
		if self.sensitive:
			if pygame.mouse.get_pressed()[0] and not self.cursor_collide(self.cursor):
				self.click=True
			elif self.press_cursor_collide(self.cursor):
				if not self.click:
					self.click = True
					self.callback()
			elif not pygame.mouse.get_pressed()[0]:
				self.click = False
		if self._text:
			self.ajust_button()
			self._text.write()

	def delete(self):
		Button.list_button.remove(self)
		del self

class Drawbutton(Button, Drawblock):
	"""
	a button with a background color
	"""
	def __init__(self, window, callback, cursor, x=0, y=0, width=100, height=50, color=(255,255,255), text=None, font=None, ajust=False, ajust_value=0, text_color=(0,0,0)):
		Button.__init__(self, callback, cursor, text=text, window=window, font=font, ajust=ajust, ajust_value=ajust_value, text_color=text_color)
		Drawblock.__init__(self, color=color, fill=0, window=window, x=x, y=y, width=width, height=height)
	
	def launch(self):
		"""draw the button"""
		self.draw()
		Button.launch(self)


	@classmethod
	def launch_all(cls):
		"""draw all the buttons"""
		for b in cls.list_button:
			b.launch()

class Picbutton(Button, Picblock):
	"""
	a button with a picture as background
	"""
	def __init__(self, window, callback, cursor, namepic, x=0, y=0, width=100, height=50, text=None, font=None, ajust=False, ajust_value=0):
		Button.__init__(self, callback, cursor, window=window, text=text, font=font, ajust=ajust, ajust_value=ajust_value)
		Picblock.__init__(self, window=window, x=600, y=200, width=width, height=height, namepic=namepic)
	
	def launch(self):
		"""print the button"""
		self.print()
		Button.launch(self)

class Spritebutton(Button, Spriteblock):
	"""
	a button with a list of pictures as background
	"""
	def __init__(self, window, callback, cursor, sprites, first_sprite=0, frequence=10, x=0, y=0, width=100, height=50, text=None, font=None, ajust=False, ajust_value=0):
		Button.__init__(self, callback, cursor, window=window, text=text, font=font, ajust=ajust, ajust_value=ajust_value)
		Spriteblock.__init__(self, sprites=sprites, window=window, first_sprite=first_sprite, x=x, y=y, 
			width=width, height=height, speed=0, frequence=frequence)
	
	def launch(self, jump=1):
		"""anime the button"""
		self.anime(jump)
		Button.launch(self)



