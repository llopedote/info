import json

# Ce code ajoute un contact à un fichier JSON nommé contacts.json
# Si le fichier n'existe pas, il est créé

try:
	with open("contacts.json") as file:
		contacts = json.loads(file.read())
except FileNotFoundError:
	# si le fichier n'existe pas, on part d'une liste vide
	contacts = []

name = input("Entrez le nom du nouveau contact: ")
phone = input("Entrez son numéro de téléphone: ")

contacts.append({
	"name": name,
	"phone": phone
})

with open("contacts.json", 'w') as file:
	file.write(json.dumps(contacts, indent='\t'))
