class Foo:
	@classmethod
	def hi(cls):
		print(cls.__name__)
my_object = Foo()
my_object.hi()