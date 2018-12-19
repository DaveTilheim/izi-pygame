	def __init__(self, window, callback, cursor, x=0, y=0, width=100, height=50, color=(255,255,255), text=None, font=None, ajust=False, ajust_value=0, text_color=(0,0,0)):
		Button.__init__(self, callback, cursor, text=text, window=window, font=font, ajust=ajust, ajust_value=ajust_value, text_color=text_color)
		Drawblock.__init__(self, color=color, fill=0, window=window, x=x, y=y, width=width, height=height)
