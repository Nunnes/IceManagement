#!/usr/bin/env python
import Client

import DataBase

# ligacao ah base de dados
DB = DataBase.DataBase('localhost', 'ice_manager', 'ice', 'ice_db');

clientList = []

class Manager:
    '''Represents a Data Manager: trata da base de dados e da logica de negocio''' 
    
    def __init__(self):
        '''Initializes the Data manager'''
        print 'Voodoo magic is about to happen!'

    def closeDb (self):
        DB.closeDb()
 
    # imprime a lista de clientes
    def printClientList(self):
	print ("Client List: ")
        clist = DB.listClient()

        for c in clist:
            print (c)

        '''
        i=0
	print ("Client List: ")
        for cl in clientList:
            i+=1
            print ("%d - %s"  % (i, cl.name ))
        '''
    def createClient(self):
        '''Create a client'''
        name = raw_input("Nome do Cliente: ")
        clientList.append(Client.Client(name))
        print ("\n Client " + name + " was born! \n")
       
    def removeClient(self):
        '''Remove Client from database'''
        name = raw_input("Nome do Cliente a remover: ")

        #procura cliente
        for cl in clientList:
            if(cl.name == name):
                cl.delete() # como eliminar objecto???
                clientList.remove(cl)

    def changeName(self):
        name = raw_input("Nome do Cliente a remover: ")
        #procura cliente
        for cl in clientList:
            if(cl.name == name):
                cl.setName(name)
            else: 
                print ("Client %s not found.\n" % name) 

    def insertClient(self):
        '''Add Client to database'''  
    

    def howMany(self):
        Client.Client.howMany()


    def calcAVG(self, clientName, frequency):
        '''calculates average incomes from a client over weeks, day...'''


    def calcDebt(self, ClientName):
        '''Calculates total debt of a costumer'''


    def listClientDebt(self,name):
        for cl in clientList:
            if(cl.name == name):
                cl.printTransactionList()
            else: 
                print ("Client not found!\n")


    def makeTransaction(self):
       '''Makes a transaction '''
       name = raw_input("Client: ")
       for cl in clientList:
           if(cl.name == name):
               print(name + cl.name)
               cl.buyIce()
               self.listClientDebt(name)
           else: 
               print ("Client not found!\n")
    

    
    
