from application.Controllers.Controller import Controller
from application.Classes.ClientContainer import Client

class UserController(Controller):
	
	def __init__(self, database):
		Controller.__init__(self, database)

	def exampleUserControllerFunction(self):
		print("User Controller")

	#function takes self and a string "username" to get the user from the client table.
	#returns list with client information or emptylist if client doesn't exist in database
	def getClientByUsername(self, username):
		get_client_cursor = self.db.executeQuery("Select * From client WHERE username = ?", (username,))
		
		#using fectchmany(1) because there is only one record with this username.
		found_client = get_client_cursor.fetchmany(1)
		found_client_list = []

		for row in found_client:
			found_client_list.append(Client(row))
		
		if found_client == []:
			print("There are no client with given username")
			return found_client_list
		else:
			print(found_client_list)
			return found_client_list

	#function takes self and a string "email" to get the user from the client table.
	#returns list with client information or emptylist if client doesn't exist in database
	def getClientByEmail(self, email):
		get_client_cursor = self.db.executeQuery("SELECT * FROM client WHERE email = ?", (email,))
		
		#using fectchmany(1) because there is only one record with this email.
		found_client = get_client_cursor.fetchmany(1)
		found_client_list = []

		for row in found_client:
			found_client_list.append(Client(row))
		
		if found_client == []:
			print("There are no client with given email")
			return found_client_list
		else:
			print(found_client_list)
			return found_client_list

	#function takes self and a string "username" & "password" to get the client from the client table.
	#if client exits, returns list with client information and updates value in attribute isLogged to 1. Returns emptylist if client doesn't exist in database
	def getClientByPassword(self, username, password):
		get_client_cursor = self.db.executeQuery("SELECT * FROM client WHERE username = ? AND password = ?", (username, password))
		
		#using fectchmany(1) because there is only one record with this username & password.
		found_client = get_client_cursor.fetchmany(1)
		found_client_list = []

		for row in found_client:
			found_client_list.append(Client(row))
		
		if found_client == []:
			print("There are no client with given username and password")
			return found_client_list
		else:
			print(found_client_list)
			self.db.executeQueryWrite("UPDATE client SET isLogged = 1 WHERE username = ?", (username,))
			return found_client_list
	
	#function takes self and username
	#updates value in attribute isLogged to 0.
	def logoutClient(self, username):
		self.db.executeQueryWrite("UPDATE client SET isLogged = 0 WHERE username = ?", (username,))
		print("Client has been logged out")

	#function takes self and several values to create a client
	#inserts a new client into the client table
	def createClient(self,firstName,lastName,physicalAddress,email,phoneNumber,username,password,isAdmin,isLogged,lastLogged):
		getClientByUsername = self.getClientByUsername(username)
		getClientByEmail = self.getClientByEmail(username)
		
		if len(getClientByUsername) == 0 & len(getClientByEmail) == 0:
			sql_insert_client = '''INSERT INTO client(firstName,lastName,physicalAddress,email,phoneNumber,username,password,isAdmin,isLogged,lastLogged)
					VALUES(?,?,?,?,?,?,?,?,?,?) '''
			client = (firstName,lastName,physicalAddress,email,phoneNumber,username,password,isAdmin,isLogged,lastLogged)
			self.db.executeQueryWrite(sql_insert_client, client)
			print("New user has been successfully created in database")

		else:
			print("User already exist in database")


