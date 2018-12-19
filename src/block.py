import pygame, pygame.mixer
from pygame.locals import*
import sys

class Block:
	"""
	Block -> hitbox no visible
	xbegin = xorigin of the block
	ybegin = yorigin of the block
	width = width of the block
	height = height of the block
	speed = the speed of the block if it moved
	id = the id of the block
	"""
	nb_block = 0
	list_block = []
	def __init__(self, x=0, y=0, width=100, height=100, speed=5):
		self._xbegin = x
		self._ybegin = y
		self._width = width
		self._height = height
		self.rect = pygame.Rect(x, y, width, height)
		self.xend = x+width
		self.yend = y+height
		self.speed = speed
		self.id = Block.nb_block
		self.time = None
		Block.nb_block += 1
		Block.list_block.append(self)

	def get_x(self):
		return self._xbegin
	def set_x(self, x):
		self.set_position(x, self._ybegin)
	xbegin = property(fget=get_x, fset=set_x, doc="the x position of the Block")
	
	def get_y(self):
		return self._ybegin
	def set_y(self, y):
		self.set_position(self._xbegin, y)
	ybegin = property(fget=get_y, fset=set_y, doc="the y position of the Block")

	def get_width(self):
		return self._width
	def set_width(self, width):
		self.set_dimension(width) 
	width = property(fget=get_width, fset=set_width, doc="the width of the Block")

	def get_height(self):
		return self._height
	def set_height(self, height):
		self.set_dimension(None, height) 
	height = property(fget=get_height, fset=set_height, doc="the height of the Block")


	def set_position(self, x, y):
		"""set the position of the block"""
		self._xbegin = x
		self._ybegin = y
		self.xend = x+self._width
		self.yend = y+self._height
		self.rect = pygame.Rect(x, y, self._width, self._height)
	
	def set_dimension(self, width=None, height=None):
		"""set the dimanension of the block"""
		new_width = width
		new_height = height
		if width is None:
			new_width = self._width
		if height is None:
			new_height = self._height
		self._width = new_width
		self._height = new_height
		self.set_position(self._xbegin, self._ybegin)
	
	def is_in_collision_with(self, other):
		"""detect collision between rects"""
		if type(other) is list:
			return self.rect.collidelist(other)
		else:
			return self.rect.colliderect(other)
	#alias
	collision = is_in_collision_with

	
	def set_mouse_position(self, pos="center"):
		"""the block position has the same position as the mouse"""
		mx,  my = pygame.mouse.get_pos()
		if pos is "origin":
			self.set_position(mx, my)
		elif pos is "center":
			self.set_position(mx-self._width//2, my-self._height//2)

	def move(self, direction, spd=None):
		"""the block move with a direction and a speed"""
		speed = self.speed
		if spd is not None:
			speed = spd
		if direction == "right":
			self._xbegin += speed
		elif direction == "left":
			self._xbegin -= speed
		elif direction == "up":
			self._ybegin -= speed
		elif direction == "down":
			self._ybegin += speed
		self.set_position(self._xbegin, self._ybegin)

	
	def gravity(self, g=10):
		"""the block is influenced by the gravity"""
		self.time = pygame.time.get_ticks()/1000
		self.speed = g*self.time
		self._ybegin += self.speed
		self.set_position(self._xbegin, self._ybegin)

	
	def delete_from_class_list(self):
		"""delete the block from the classblock_list"""
		del Block.list_block[self.id]
		Block.nb_block -= 1

	
	def cursor_collide(self, cursor):
		"""detect a collision with a block (width=1, height=1)"""
		if cursor._xbegin >= self._xbegin and cursor._xbegin <= self.xend and cursor._ybegin >= self._ybegin and cursor._ybegin <= self.yend:
			return True
		return False

	
	def press_cursor_collide(self, cursor):
		"""detect a collision with a 1px/1px block and detect a keypress event"""
		if pygame.mouse.get_pressed()[0] and self.cursor_collide(cursor):
			return True
		return False

	
	def mult_size(self, fact=1):
		"""mult the size of the block by fact"""
		if fact <= 0:
			return 'error'
		self._width = int(self._width * fact)
		self._height = int(self._height * fact)
		self.set_position(self._xbegin, self._ybegin)
	
	def div_size(self, fact=1):
		"""divide the size of the block by fact"""
		if fact <= 0:
			return 'error'
		self._width = self._width//fact
		self._height = self._height//fact
		self.set_position(self._xbegin, self._ybegin)
	
	def pow_size(self, power=2):
		"""pow the size of the block by fact"""
		if power < 0:
			return 'error'
		self._width = self._width**power
		self._height = self._height**power
		self.set_position(self._xbegin, self._ybegin)
	
	def __imul__(self, fact):
		"""mult the size of the block by fact with *="""
		if fact <= 0:
			return self
		self._width = int(self._width * fact)
		self._height = int(self._height * fact)
		self.set_position(self._xbegin, self._ybegin)
		return self
	
	def __itruediv__(self, fact):
		"""divide the size of the block by fact with /="""
		if fact <= 0:
			return self
		self._width = self._width//fact
		self._height = self._height//fact
		self.set_position(self._xbegin, self._ybegin)
		return self
	
	def __ifloordiv__(self, fact):
		"""divide the size of the block by fact with //="""
		if fact <= 0:
			return self
		self._width = self._width//fact
		self._height = self._height//fact
		self.set_position(self._xbegin, self._ybegin)
		return self
	
	def __ipow__(self, power):
		"""pow the size of the block by fact with **="""
		if power < 0:
			return self
		self._width = self._width**power
		self._height = self._height**power
		self.set_position(self._xbegin, self._ybegin)
		return self
	
	def __lshift__(self, other):
		"""add the size of the block with an other block with <<"""
		self._width += other._width
		self._height += other._height
		self.set_position(self._xbegin, self._ybegin)
	
	def __rshift__(self, other):
		"""add the size of an other block with the instance with >>"""
		other << self

	def __str__(self):
		return "{}x{} ({}x{}y)".format(self._width, self._height, self._xbegin, self._ybegin)

	def __repr__(self):
		string = "pos: ({}, {})\ndim: ({}, {})\nspeed: {}\nid: #{}\n".format(
			self._xbegin, self._ybegin, self._width, self._height, self.speed, self.id)
		return string

	def delete(self):
		Block.list_block.remove(self)
		del self

class Cursor(Block):
	"""It is a 1x1 Block object that follow the mouse cursor"""
	def __init__(self):
		Block.__init__(self, width=1, height=1, speed=0)

	def update(self):
		"""update the position of the object to the mouse cursor position"""
		self.set_mouse_position()

	def visible(self, boolean=True):
		"""set the visibility of the mouse cursor"""
		pygame.mouse.set_visible(boolean)
#alias
Pixelblock = Cursor



class Drawblock(Block):
	"""
	Drawblock -> visible drawing hitbox 
	color = the color of the block
	window = pygame.Surface()
	fill = 0 -> the block is filled with color
	"""
	def __init__(self, x=0, y=0, width=100, height=100, speed=5, color=(255,255,255), fill=0, window=None):
		Block.__init__(self, x, y, width, height, speed)
		if window is None:
			print("Error: no window to draw block-id #{}".format(self.id))
			sys.exit(0)
		self._color = color
		self.window = window
		self.fill = fill

	def get_color(self):
		return self._color
	def set_color(self, color):
		for c in color:
			if c < 0 or c > 255:
				return None
		self._color = color
	color = property(fget=get_color, fset=set_color, doc="the color of the Drawblock")
	
	def draw(self, form="rect"):
		"""draw the block on the screen"""
		if form is "rect":
			pygame.draw.rect(self.window, self._color, self.rect, self.fill)
		elif form is "circle":
			pygame.draw.circle(self.window, self._color, (int(self._xbegin), int(self._ybegin)), self._width//2, self.fill)

	@classmethod
	def draw_all(cls):
		"""draw all the blocks on the screen"""
		for db in Block.list_block:
			if type(db) is Drawblock:
				db.draw()

	def __repr__(self):
		string = Block.__repr__(self)
		string += "color: {}".format(self._color)
		return string



class Picblock(Block):
	"""
	Picblock -> visible picture hitbox
	window = pygame.Surface()
	namepic = name of the picture
	pic = picture load
	"""
	def __init__(self, x=0, y=0, width=100, height=100, speed=0, namepic=None, window=None):
		Block.__init__(self, x, y, width, height, speed)
		if window is None:
			print("Error: no window to print block-id #{}".format(self.id))
			sys.exit(0)
		elif namepic is None:
			print("Error: impossible to load picture about block-id #{}".format(self.id))
			sys.exit(0)
		self.window = window
		self._namepic = namepic
		self.pic = pygame.image.load(self._namepic).convert_alpha()
		self.pic = pygame.transform.scale(self.pic, (self._width, self._height))

	def get_namepic(self):
		return self._namepic
	def set_namepic(self, nop):
		print("use set_pic to change the picture of the block...")
	namepic = property(fget=get_namepic, fset=set_namepic, doc="the name of the picture of the block")

	
	def print(self):
		"""print the picture block on the screen"""
		self.window.blit(self.pic, (self._xbegin, self._ybegin))

	@classmethod
	def print_all(cls):
		"""print all the picture blocks on the screen"""
		for pb in Block.list_block:
			if type(pb) is Picblock:
				pb.print()

	def set_dimension(self, width=None, height=None):
		"""set dimensions of the picblock"""
		new_width = width
		new_height = height
		if width is None:
			new_width = self._width
		if height is None:
			new_height = self._height
		self._width = new_width
		self._height = new_height
		self.rect = pygame.Rect(self._xbegin, self._ybegin, new_width, new_height)
		self.pic = pygame.transform.scale(self.pic, (self._width, self._height))
		self.set_position(self._xbegin, self._ybegin)

	
	def set_pic(self, pic, width=None, height=None):
		"""set the picture with an other pic and other dimensions"""
		if width is not None:
			self._width = width
		if height is not None:
			self._height = height
		self._namepic = pic
		self.pic = pygame.image.load(self._namepic).convert_alpha()
		self.pic = pygame.transform.scale(self.pic, (self._width, self._height))
		self.set_position(self._xbegin, self._ybegin)

	def __repr__(self):
		string = Block.__repr__(self)
		string += "picture: {}".format(self.pic)
		return string


class Spriteblock(Picblock):

	"""
	Spriteblock -> animated Picblock
	sprites = list of pictures that composed the block
	frequence = speed of animation (not the same with each fps)
	first_sprite = the index of the first sprite
	"""
	def __init__(self, sprites, window, first_sprite=0, x=0, y=0, width=100, height=100, speed=0, frequence=10):
		Picblock.__init__(self, x, y, width, height, speed, sprites[first_sprite], window)
		self._sprite_list = sprites
		self.index_picture = 0
		self._number_pictures = len(self._sprite_list)
		self.frequence = frequence
		self.index_frequence = 0

	def get_sprite_list(self):
		return self._sprite_list
	def set_sprite_list(self, sprites):
		self._sprite_list = sprites
		self.index_picture = 0
		self._number_pictures = len(self._sprite_list)
	sprite_list = property(fget=get_sprite_list, fset=set_sprite_list, doc="the list of the sprites")

	def get_number_pictures(self):
		return self._number_pictures
	def set_number_pictures(self, nop):
		print("you can not set this attribute...")
	number_pictures = property(fget=get_number_pictures, fset=set_number_pictures, doc="the len of list of the sprites")

	def anime(self, jump=1):
		"""
		print the Spriteblock with animation
		"""
		if self.index_frequence < self.frequence:
			self.index_frequence += 1
			self.print()
			return
		elif self.index_frequence >= self.frequence:
			self.index_frequence = 0
		if jump < 1 or jump > self._number_pictures:
			jump = 1
		self.print()
		self.set_pic(self._sprite_list[self.index_picture])
		self.index_picture += jump
		if self.index_picture >= self._number_pictures:
			self.index_picture = 0

	@classmethod
	def anime_all(cls):
		"""
		print all the Spriteblock with animation
		"""
		for sb in Block.list_block:
			if type(sb) is Spriteblock:
				sb.anime()









