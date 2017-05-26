class Animal(object):
	def run(self):
		print('this is Animal')

class Dog(Animal):
	def run(self):
		print('this is dog')

class Cat(Animal):
	def run(self):
		print('this is cat')

dog = Dog()
dog.run()

cat = Cat()
cat.run()							


def run_twice(Animal):
	Animal.run()
	Animal.run()

run_twice(Animal())	

run_twice(Dog())

run_twice(Cat())

print(type(dog))