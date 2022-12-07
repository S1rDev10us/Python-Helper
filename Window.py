# if(__name__!='__main__'):raise NotImplementedError('Code is not done')
print('This code is experimental and unstable, use with caution')

import tkinter
from PIL import Image
import numpy as np


# class Window:
# 	import os	
# 	def __init__(self) -> None:
# 		import pygame
# 		self.pygame=pygame
# 		self.pygame.init()
# 		# self
		
# 		self.display=self.pygame.display.set_mode()
# 		pass
# 	def updateScreen(self,screen:list[list[tuple[int,int,int,int]]]) -> None:
		
# 		pass
# 	def updateCaption(self,caption:str=None):
# 		if(caption!=None):
# 			self.pygame.display.set_caption(caption)
# 		else:
# 			import __main__
# 			if('__file__' in __main__.__dict__):
# 				self.pygame.display.set_caption(self.os.path.basename(__main__.__file__).split('.py')[0])
# 		pass

class Window(tkinter.Tk):
	def __init__(self,image:list[list[tuple[int,int,int,int]]],updateFunc:function, screenName: str ='Image Display') -> None:
		tkinter.Tk.__init__(self)
		self.iteration=0
		self.label=tkinter.Label(text="Image",compound='top')
		self.image=image
		self.UpdateImage(100)
		self.updateFunc=updateFunc



		self.mainloop()
	def imageArrayToPILImage(image:list[list[tuple[int,int,int,int]]])->Image.Image:
		npImage=np.asarray(image,dtype=np.uint8)
		return Image.fromarray(npImage)
	def PILImageToTkImage(image:Image.Image)->tkinter.PhotoImage:
		return tkinter.PhotoImage(image)
	def imageArrayToTkImage(self,image:list[list[tuple[int,int,int,int]]])->None:
		pilImage=self.imageArrayToPILImage(image)
		tkImage=self.PILImageToTkImage(pilImage)
		return tkImage
	def UpdateImage(self,delay,event=None):
		
		self.updateFunc(self)

		self.iteration+=1
		self.label.configure(image=self.image)
		self.after(delay,self.UpdateImage,delay)
		
