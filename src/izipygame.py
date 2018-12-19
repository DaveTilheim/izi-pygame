import pygame, pygame.mixer
from pygame.locals import*
from random import randint
from izi_pygame.block import *
from izi_pygame.window import *
from izi_pygame.police import *
from izi_pygame.button import *
from izi_pygame.entry import *

#import file
DEFAULT_FONT = Fontstring()
TIME = pygame.time.Clock()

def init(surface):
	"""init the default font"""
	DEFAULT_FONT.win = surface

def update_screen():
	"""refresh the screen"""
	pygame.display.flip()