from typing import Callable
funcDict:dict[str,dict[str,Callable]]={}

from inspect import signature, stack



def findParams(funcPath,*args,**kwargs):
	pass

def overload(func:Callable)->Callable:
	funcPath=str(func).split(' ')[1]
	funcParams=str(signature(func))
	if(funcPath not in funcDict):
		funcDict[funcPath]={}
	
	funcDict[funcPath][funcParams]=func

	def returned(*arguments,**keywordArguments):
		params=findParams(funcPath,args=arguments,kwargs=keywordArguments)
		if(params not in funcDict[funcPath]):
			raise NotImplementedError(f'\n\n\nAn error occured with an overloaded function:\n	The argument collection that was passed in was not found in any overloads of this function\n	{funcPath = }\n	{arguments = }\n	{keywordArguments = }\n	Called from:\n		Function: "{stack()[1][3]}"\n		Line: {stack()[1][2]}\n		File: "{stack()[1][1]}"')
		return funcDict[funcPath][params]()
	return returned


if(__name__=='__main__'):
	@overload
	def test(test:int):
		pass
	class test2:
		@overload
		def test(test,othertest:str):
			pass
	def hi():
		test2.test(5,'hello there',a='hi',b=2)
	hi()

