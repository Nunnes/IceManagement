#!/usr/bin/env python

import io
import sys
import Manager
import ClientDTO
import TransactionDTO

Man = Manager.Manager()


# Listas para os menus 
mainMenuList = ["1 - Create Client",
		"2 - Remove Client", 
		"3 - Clients' list",
		"4 - Regist transaction", 
		"5 - Debts","6 - Pay credit", 
		"7 - Exit", 
		"\n"]

subMenuDebtsList = ["1 - List clients with credit", 
		    "2 - Pay debt", 
		    "3 - back to main menu", 
		    "\n"]

subMenuList = ["putt", "stuff", "here!"]


def printMenuList(MenuList):
	for option in MenuList:
		print(option)
	
def main():

	while(True):
		print("\n Welcome to the ICE") 
		menu()	
	return 0

#Menu Principal
def menu():
	
	#imprime mainMenu
	printMenuList(mainMenuList)

	try:
		sys.stdout.flush()
		cmd =  input("Please enter a value:")
	except:
		print("Not an option. Try other stuff! ")
		
	if(cmd == 0):
		print("subMenu...")
		subMenu()
		
	elif(cmd == 1):
		#receive info to create a client
		name = raw_input("First name: ")
		lastName = raw_input("Last name: ")
		phone =  input("Phone: ")
		email = raw_input("Email: ")

		clientDTO = ClientDTO.ClientDTO(name, lastName, phone, email)
		Man.createClient(clientDTO) 

	elif(cmd == 2):
		#receive info to delete a specific client
		name = raw_input("First name: ")
		lastName = raw_input("Last name: ")
		clientDTO = ClientDTO.ClientDTO(name, lastName)
		Man.removeClient(clientDTO)
		
	elif(cmd == 3):
		#Print Client List
		Man.printClientList()

	elif(cmd == 4):
		print("4 - Registar Compra")
	        
                #cria uma venda
		print ("Venda")
		clientName = raw_input("Client: ")
		price = input("Price: ")
		quantity = input("Quantity: ")
		credit = raw_input("Credit (y/N): ")

		transactionDTO = TransactionDTO.TransactionDTO(clientName, quantity, price, credit)
		Man.makeTransaction(transactionDTO)


	elif(cmd == 5):
		subMenuDebts()

	elif(cmd == 6):
		print("6 - Pagar fiado")
	
	elif(cmd == 7):
		Man.closeDb() # disconecta da BD
		print("Bye")
		exit()
				
	else:
		print("Command not available!")


#SubMenu dos Fiados
def subMenuDebts():
	
	while(True):
		printMenuList(subMenuDebtsList)
		
		try:
			sys.stdout.flush()
			cmd =  input("Please enter an option:")
		except:
			print("Not an option. Try other stuff! ")
			
		if(cmd == 1):
			print("List Clients with credit")

		elif(cmd == 2):
			print("Pay something!")

		elif(cmd == 3):
			print("Back to main menu")
			break

		
#subMenu para usar no futuro
def subMenu():
	while(True):
		printMenuList(subMenuList)
		
		try:
			sys.stdout.flush()
			cmd =  input("Please enter an option:")
		except:
			print("Not an option. Try other stuff! ")
			
		if(cmd == 1):
			print("List Clients with credit")

		elif(cmd == 2):
			print("Pay something!")

		elif(cmd == 3):
			print("Back to main menu")
			break
				

if __name__ == '__main__':
	main()
	

	
