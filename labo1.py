from math import sqrt

# 1.a
E = set("Je suis un as en programmation.")
print("1.a:", E)

# 1.b
E = {n for n in range(1, 1001) if n%3 == 0 and n%13 == 0}
print("1.b:", E)

# 1.c
E = set("Maitriser les listes est crucial!") & set("aeiouAEIOU")
print("1.c:", E)

# 2
def set2list(E):
	res = []
	for elem in E:
		res.append(elem)
	return res

print("set2list:", set2list({1, 2, 3, 3}))

# 3.1
def common(A, B):
	count = 0
	for elem in A:
		if elem in B:
			count += 1
	return count

print("common avec for:", common({1, 2, 3}, {2, 3, 4}))

# 3.2
def common(A, B):
	return len(A&B)

print("common sans for:", common({1, 2, 3}, {2, 3, 4}))

# 4
def xor(A, B):
	return (A|B) - (A&B)

print("xor:", xor({1, 2, 3}, {2, 3, 4}))

# 6
D = {n: n-1 for n in range(2, 21, 2)}
print("6:", D)

# 7
D = {2*n+1: (2*n+1)%3 == 0 for n in range(1, 11)}
print("7:", D)

# 8
def vowel(word):
	count = 0
	for letter in word:
		if letter in "aiueoAIUEO":
			count += 1
	return count

fruits = ['lemon', 'apple', 'banana', 'watermelon']
D = {fruit: vowel(fruit) for fruit in fruits}
print("8:", D)

# 9.a
def hasKey(key, dico):
	for k in dico.keys():
		if k == key:
			return True
	return False

print("9.a:", hasKey('apple', D))

# 9.b
def hasKey(key, dico):
	return key in dico

print("9.b:", hasKey('apple', D))

# 10
def distance(p1, p2):
	x1, y1, z1 = p1
	x2, y2, z2 = p2
	return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

print("distance:", distance((1, 2, -1), (0, 2, 1)))

# 11
def buildsentence(words):
	res = ""
	for word in words:
		res += word + " "
	return res[:-1] # ne renvoie pas le dernier espace

words = ("Bonjour", "monsieur", "Lurkin,", "ça", "va", "bien", "?")
sentence = buildsentence(words)
print("11 avec for:", sentence)

# 11 alternative
def buildsentence(words):
	return " ".join(words)

words = ("Bonjour", "monsieur", "Lurkin,", "ça", "va", "bien", "?")
sentence = buildsentence(words)
print("11 avec join:", sentence)