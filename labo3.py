def title(s):
	print('\n', s, len(s)*'-', sep='\n')

# 1, 2 et 3
class Item:
	def __init__(self, code, name, cent):
		self.__code = code
		self.__name = name
		self.__cent = cent

	@property
	def unitprice(self):
		return self.__cent / 100

	def price(self, quantity):
		return self.unitprice * quantity

	def __str__(self):
		return '{} (code: {}, prix: {})'.format(self.__name, self.__code, self.__cent)

title('Question 1, 2 et 3')
beer = Item (56273, 'Zundert 33 cl', 250)
print("unitprice:", beer.unitprice)
print("price(10):", beer.price(10))
print("beer:", beer)

# 4
class Answer:
	def __init__(self, id, text):
		self.__id = id
		self.__text = text

	@property
	def id(self):
		return self.__id

	@property
	def text(self):
		return self.__text

	def __str__(self):
		return '[{}] {}'.format(self.id, self.text)

title('Question 4')
a1 = Answer ('A1', 'Il est blanc.')
a2 = Answer ('A2', "Il n'en a pas.")
a3 = Answer ('A1', 'Shuuut, je joue à Fortnite.')
a4 = Answer ('A3', 'Il est rayé.')
print (a1, a2, a3, a4, sep='\n')

# 5
class Question:
	def __init__(self, id, text):
		self.__id = id
		self.__text = text
		self.__answers = []
		self.__correct = {}

	@property
	def id(self):
		return self.__id

	@property
	def text(self):
		return self.__text

	def add(self, answer, correct):
		if answer.id not in self.__correct:
			self.__correct[answer.id] = correct
			self.__answers.append(answer)

	def __str__(self):
		question = '[{}] {}'.format(self.id, self.text)
		answers = ['    {} ({})'.format(answer, self.__correct[answer.id]) for answer in self.__answers]
		return '\n'.join([question] + answers)



title('Question 5')
q1 = Question('Q1', 'Quelle est la couleur du chat de Marchand?')
q1.add(a1, True)
q1.add(a2, True)
q1.add(a3, False) # Ne sera pas ajoutée, car identifiant déjà existant
q1.add(a4, False)
print(q1)