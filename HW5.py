#1 Person

class Person(object):
	
	def __init__(self, age, name):
		self.age = age
		self.name = name
		self.list_of_persons = []

	def know_person(self, person):
		self.list_of_persons.append(person)
		print('{} now added to list of {} known persons'.format(person.name, self.name))	

	def is_known_person(self, person):
		if person in self.list_of_persons:
			print('{} and {} know each other'.format(self.name, person.name))
		else:
			print('{} and {} do not know each other'.format(self.name, person.name))	

person1 = Person(28, 'Dima')
person2 = Person(55, 'Sasha')
person3 = Person(31, 'Masha')
person1.know_person(person2)
person1.is_known_person(person3)


#2 Printer

class Printer(object):
	
	def log(self, *values):
		for value in values:
		    print(value)

class FormattedPrinter(Printer):
	def formatted_log(self, *values):
		for value in values:
		    print('*' * 20)
		    self.log(value)
		    print('*' * 20)

to_print = Printer()
to_print.log('I wanna print!')
star_print = FormattedPrinter()
star_print.formatted_log('I wanna beautiful print')

#3 Animal & Human

class Animal(object):

	def __init__(self, animal, danger_level = False):
		self.animal = animal
		self.danger_level = danger_level	
				

class Human(object):

	def __init__(self, name):
		self.name = name

	def is_dangerous(self, animal):
		if animal.danger_level :
			print('Be carefull! {} is dangeous!'.format(animal.name))	
		else :
			print('{} is not dangerous'.format(animal.name))	

human1 = Human('Stan')
animal1 = Animal('tiger', True)
animal2 = Animal('parrot')
animal3 = Animal('snake', True)
human1.is_dangerous(animal1)
human1.is_dangerous(animal2)
human1.is_dangerous(animal3)












						

		
