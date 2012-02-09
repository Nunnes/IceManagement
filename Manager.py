#!/usr/bin/env python

import ClientDTO
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

    #Cria Client
    def createClient(self, clientDTO):
        '''Create client'''
        '''falta chamar o db manager e colocar na db ''' 
        print ("\n Client + %s +  was born! \n" % clientDTO.firstname  )
        
        
    #Remove Client
    def removeClient(self, clientDTO):
        '''Remove Client from database'''
        print ("Client %s removed" % clientDTO.firstname)


    def changeName(self, clientDTO):
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
    

    
    
