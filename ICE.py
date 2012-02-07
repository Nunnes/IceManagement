#!/usr/bin/env python

import io
import Manager

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
		cmd =  input("Please enter a value:")
	except:
		print("not a number")
		cmd  = 6
		
	if(cmd == 0):
		print ("Venda: \n")
		Man.makeTransaction()

		
	if(cmd == 1):
	    	Man.createClient()
		Man.printClientList()

		
	elif(cmd == 2):
		Man.removeClient()
		Man.printClientList()
		

	elif(cmd == 3):
		Man.printClientList()


	elif(cmd == 4):
		print("3 - Registar Compra")


	elif(cmd == 5):
		print("4 - Ver Fiados")


	elif(cmd == 6):
		print("Bye")
		exit()
				
	else:
		print("Command not available!")

		
if __name__ == '__main__':
	main()
	

	
