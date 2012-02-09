#!/usr/bin/env python

import io
import sys
import Manager
import ClientDTO

ListaClientes = []
Man = Manager.Manager()

def main():
	

	while True:
		print("\n Welcome to the ICE") 
		menu()	
	return 0

def menu():
	
	print("0 - Venda")
	print("1 - Create Client")
	print("2 - Remove Client")
	print("3 - Clients' list")
	print("4 - Register")
	print("5 - Debts")
	print("6 - Exit")
	print ("\n")
	
	try:
		sys.stdout.flush()
		cmd =  input("Please enter a value:")
	except:
		print("Not an option. Try other stuff! ")
		
	if(cmd == 0):
		print ("Venda: \n")
		Man.makeTransaction()

		
	elif(cmd == 1):
		''' Receive Client info '''
		
		name = raw_input("First name: ")
		lastName = raw_input("Last name: ")
		phone =  input("Phone: ")
		email = raw_input("Email: ")
		clientDTO = ClientDTO.ClientDTO(name, lastName, phone, email)
		Man.createClient(clientDTO) 

		
	elif(cmd == 2):
		name = raw_input("First name: ")
		lastName = raw_input("Last name: ")
		clientDTO = ClientDTO.ClientDTO(name, lastName)
		Man.removeClient(clientDTO)
		

	elif(cmd == 3):
		Man.printClientList()


	elif(cmd == 4):
		print("4 - Registar Compra")


	elif(cmd == 5):
		print("5 - Ver Fiados")


	elif(cmd == 6):
		Man.closeDb() # disconecta da BD
		print("Bye")
		exit()
				
	else:
		print("Command not available!")

		
if __name__ == '__main__':
	main()
	

	
