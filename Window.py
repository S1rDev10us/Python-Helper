
raise NotImplementedError('Code is not done')

class Window:
	import os	
	def __init__(self) -> None:
		import pygame
		self.pygame=pygame
		self.pygame.init()
		# self
		
		self.display=self.pygame.display.set_mode()
		pass
	def updateScreen(self,screen:list[list[tuple[int,int,int,int]]]) -> None:
		pass
	def updateCaption(self,caption:str=None):
		if(caption!=None):
			self.pygame.display.set_caption(caption)
		else:
			import __main__
			if('__file__' in __main__.__dict__):
				self.pygame.display.set_caption(self.os.path.basename(__main__.__file__).split('.py')[0])
		pass

if(__name__=='__main__'):
	Window().updateCaption()
	while(True):pass