import copy

# 1
def findAll(L, elem):
	res = []
	for i, value in enumerate(L):
		if value == elem:
			res.append(i)
	
	return len(res)!=0, res

print("findAll([1, 2, 3, 1, 4, 1], 1) =>", findAll([1, 2, 3, 1, 4, 1], 1))
print("findAll([1, 2, 3, 1, 4, 1], 6) =>", findAll([1, 2, 3, 1, 4, 1], 6))

# 2
def buildContacts(name, phone):
	res = []
	for i in range(len(name)):
		res.append({"name":name[i], "phone":phone[i]})
	return {"contacts": res}

print("buildContacts:", buildContacts(["Quentin", "André"],[1234, 5678]))

# Plus court
def buildContacts(name, phone):
	return {"contacts": [{"name": name[i], "phone": phone[i]} for i in range(len(name))]}

print("buildContacts (plus court):", buildContacts(["Quentin", "André"],[1234, 5678]))

# 3
def totalValue(stock):
	res = 0
	for articleName in stock:
		article = stock[articleName]
		res += article['quantity'] * article['price']
	return res

stock = {
	'Coca 33cl': {
		'quantity': 5,
		'price': 1.0
	},
	'Nokia 3310': {
		'quantity': 7,
		'price': 35.99
	}
}

print("totalValue:", totalValue(stock))

# 4
def merge(stock1, stock2):
	res = copy.deepcopy(stock1)
	for articleName in stock2:
		if articleName in res:
			res[articleName]['quantity'] += stock2[articleName]['quantity']
		else:
			res[articleName] = stock2[articleName]
	return res

stock2 = {
	'Coca 33cl': {
		'quantity': 10,
		'price': 1.0
	},
	'Playstation 5': {
		'quantity': 7,
		'price': 499
	}
}

print("merge:", merge(stock, stock2))