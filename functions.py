#Basic functions for  the database. 
""""
Universidad del Valle de Guatemala
Seccion
functions.py
"""

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

#Adds a user to the database. To do this, it needs the basic information
def add_User(db, name, age, email, password):
    Person = db.nodes.create(name=name, age = age, email = email, password = password)
    try:
    	Person.labels.add("User")
    	print ("\nUser has been registered succesfully.\n")
    except Exception:
    	print("\nUser could not be added.\n")
#Adds a game to the database. It needs the basic attributes.
def add_Game(db, title, price, rating):
    Game = db.nodes.create(title=title,price= price, rating=rating)
    try:
    	Game.labels.add("Game")
    	print("\nGame has been registered succesfully.\n")
    except Exception:
    	print("\nGame could not be added.")
#Creates connections between people
def create_PersonConnection(user1,user2):
    try:
    	user1.relationships.create("KNOWS",user2)
    	return "Database has been updated. \n"
    except Exception:
    	print("\n\n---------------------------------------------------------")
    	print("-------------Couldn't add user to the Database------------")
    	print("----------------------------------------------------------")
#Checks the prices and releases a list of them
def check_Prices(db, price, client):
    q = "Match(g: Game) WHERE g.price=" +price+" \n RETURN g"
    result = db.query(q,returns=(client.Node,float,client.Node))
    try:
    	for game in result:
        	print(game[0]["title"])
    	return game
    except Exception:
    	print("\n\n---------------------------------------------------------")
    	print("----------Couldn't find games under such Price----------")
    	print("----------------------------------------------------------")
#Gets usernames to be used in login systems
def get_User(db, username, client):
	users = []
	q = 'MATCH(p: Person) WHERE p.name="'+username+'" RETURN p'
	result = db.query(q, returns=(client.Node, str, client.Node))
	try:
		for user in result:
			if user.count(user)<1:
				users.append(user)
	except Exception:
		print("----------------------------------------------------------")
		print("-----------------Couldn't find this user------------------")
		print("----------------------------------------------------------")
	
	if not users:
	   	return False
	elif users:
		return True
	
	
#Checks the rating and releases a list based off of what it's found
def check_Rating(db, rating, client):
    q = 'MATCH (g: Game) WHERE g.rating="' + rating + '" RETURN g'
    result = db.query(q, returns=(client.Node, str, client.Node))
    try:
    	for r in result:
        	print(r[0]['title'])
    	return r
    except Exception:
    	print("\n\n---------------------------------------------------------")
    	print("----------Couldn't find games under such rating----------")
    	print("----------------------------------------------------------")
#Recommends games
def recommendGame(db, price, rating):
    q = 'MATCH (g: Game) WHERE g.price="'+price+'" RETURN g'
    result = db.query(q, returns=(client.Node, str, client.Node))
    games = []
    try:
    	for game in result:
    		if games.count(game)<1:
    			games.append(game)
    except Exception:
    	print("---------------------------------------------------------")
    	print("----------Couldn't find games under such price----------")
    	print("----------------------------------------------------------")

    q = 'MATCH (g: Game) WHERE g.rating="'+rating+'" RETURN g'
    result = db.query(q, returns=(client.Node, str, client.Node))
    try:
    	for game in result:
    		if games.count(game)<1:
    			games.append(game)
    except Exception:
    	print("---------------------------------------------------------")
    	print("----------Couldn't find games under such rating----------")
    	print("----------------------------------------------------------")
    ## Finishing
    
    for game in games:
    	if game[0]['price'] == price:
    		numero = int(game[0]['rating'])
    		numero = numero + 10
    		game[0]['score'] = str(numero)
    for game in games:
    	if game[0]['rating'] == rating:
    		numero = int(game[0]['rating'])
    		numero = numero + 30
    		game[0]['score'] = str(numero)
    games.sort(key=lambda game:game[0]['rating'])
    for game in games:
    	print("Game: "+game[0]['title']+" 	Rating: "+game[0]['rating'])
