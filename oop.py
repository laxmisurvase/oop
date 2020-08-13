print("demonstration of class and obj")

class Demo:

	def __init__(self,value1,value2):
		print("inside init method")
		self.i=value1
		self.j=value2
	def fun(self):
		print("inside fun")
		print(self.i,self.j)
	def add(self):
		print(self.i+self.j)
obj1=Demo(10,20)
obj1.fun()
obj2=Demo(50,60)
obj2.fun()
obj1.add()
obj2.add()
		

