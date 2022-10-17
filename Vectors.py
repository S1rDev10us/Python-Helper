
class Vector3():
	def __init__(self,x:float|int=None,y:float|int=None,z:float|int=None,/) -> None:
		if(x==None):
			self.x:float=float(0)
			self.y:float=float(0)
			self.z:float=float(0)
		elif(y==None):
			if(isinstance(x,Vector3)):
				self.x=x.x
				self.y=x.y
				self.z=x.z
			else:
				self.x:float=float(x)
				self.y:float=float(x)
				self.z:float=float(x)
		else:
			self.x:float=float(x)
			self.y:float=float(y)
			self.z:float=float(z)


	# Shorthands (+ != etc)

	def __add__(self,other):
		if(isinstance(other,Vector3)):
			return Vector3(other.x+self.x,other.y+self.y,other.z+self.z)
		elif(isinstance(other,int) or isinstance(other,float)):
			return Vector3(other)+self
		else:
			raise NotImplementedError("That variable type is not supported for addition")
		pass

	def __sub__(self,other):
		if(isinstance(other,Vector3)):
			return Vector3(self.x-other.x,self.y-other.y,self.z-other.z)
		elif(isinstance(other,int),isinstance(other,float)):
			return self-Vector3(other)


	def __truediv__ (self,other):
		if(isinstance(other,Vector3)):
			return Vector3(self.x/other.x,self.y/other.y,self.z/other.z)
		elif(isinstance(other,int)|isinstance(other,float)):
			return Vector3(self.x/other,self.y/other,self.z/other)
		else:
			raise NotImplementedError("That variable type is not supported for division")
		 
		pass


	#region Properties

	@property
	def magnitude(self):
		return math.sqrt(self.x**2+self.y**2+self.z**2)

	@property
	def normalized(self):
		return self/self.magnitude

	#endregion



	def __repr__(self) -> str:
		return f'Vector3(x:{self.x},y:{self.y},z:{self.z})'
	
	#region Static Properties
	
	@property
	def one (self):
		return Vector3(1,1,1)

	@property
	def zero (self):
		return Vector3(0,0,0)

	#endregion


	#region math

	@staticmethod
	def distance(loc1,loc2)->float:
		return (loc1-loc2).magnitude

	#ENDREGION
