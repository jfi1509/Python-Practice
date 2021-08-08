# #it is clearly seen that self and obj is referring to the same object

# class check:
# 	def __init__(self):
# 		print("Address of self = ",id(self))
#         print("abc")

# obj = check()
# print("Address of class object = ",id(obj))

# # this code is Contributed by Samyak Jain

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Write Python3 code here

# class car():
	
# 	# init method or constructor
# 	def __init__(self, model, color):
# 		self.model = model
# 		self.color = color
		
# 	def show(self):
# 		print("Model is", self.model )
# 		print("color is", self.color )
		
# # both objects have different self which
# # contain their attributes
# audi = car("audi a4", "blue")
# ferrari = car("ferrari 488", "green")

# audi.show()	 # same output as car.show(audi)
# ferrari.show() # same output as car.show(ferrari)

# # Behind the scene, in every instance method
# # call, python sends the instances also with
# # that method call like car.show(audi)


# Python3 program to
# demonstrate instantiating
# a class

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Dog:
	
	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
