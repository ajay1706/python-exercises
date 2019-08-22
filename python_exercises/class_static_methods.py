class Foo:
	@classmethod
	def hi(cls):
		print(cls.__name__)
my_object = Foo()
my_object.hi()

class Bar:
	@staticmethod
	def hi():
		print("I don't take param")
anoth_object = Bar()
anoth_object.hi()
		