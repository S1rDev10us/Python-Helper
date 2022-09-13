#lol i haven't tested this at all yet

from typing import Iterable
class Enum:
	"""
	A basic enum class
	"""
	pass
	class enum:
		def __init__(self,owner,name:str,index:int) -> None:
			pass
			self.owner=owner
			self.name=name
			self.index=index
		def __eq__(self, __o: object) -> bool:
			pass
			
			if(__o.__class__==self.__class__):
				if(not self.owner is __o.owner):
					raise Exception(f"Value {__o} is not from the same Enum")
				return ((self.index==__o.index))
			elif(__o.__class__==int):
				return self.index==__o
			elif(__o.__class__==str):
				if(__o in self.owner.enums):
					return self.name==__o
				else:
					raise Exception(f"Value {__o} not found in Enum")

			raise Exception(f"Value {__o} is not comparable to an enum")

		def __ne__(self, __o: object) -> bool:
			pass
			#would this work?
			return not self==__o

	def __init__(self,enums:Iterable[str]) -> None:
		pass
		self.enums:tuple=tuple(enums)
	def __getattr__(self,__name:str) -> enum:
		if(__name in self.enums):
			return Enum.enum(self,__name,self.enums.index(__name))
			pass
		pass
	def __call__(self, __name:str) -> enum:
		return self.__getattr__(__name)
		pass



if(__name__=="__main__"):
	months=Enum(['january','febuary','march','april','may','june','july','august','september','october','november','december'])

	months.january
	months.january
	print(months.january==0)
	print(months.january==1)
	print(0==months.january)
	print(1==months.january)
	print(months.january==months.january)
	print(months.january==months.febuary)
	print(months.january=='january')
	print(months.january=='june')

	print('inverted')
	print(months.january!=0)
	print(months.january!=1)
	print(0!=months.january)
	print(1!=months.january)
	print(months.january!=months.january)
	print(months.january!=months.febuary)
	print(months.january!='january')
	print(months.january!='june')



	print(months('january')!=months.january)
	print(months('january')!=months.june)
	print(months('january')==months.january)