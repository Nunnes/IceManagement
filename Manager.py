#!/usr/bin/env python

import ClientDTO
import TransactionDTO
import DataBase

# ligacao ah base de dados
DB = DataBase.DataBase('localhost', 'ice_manager', 'ice', 'ice_db');


class Manager:
    '''Represents Manager: trata da base de dados e da logica de negocio''' 
    
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
        DB.addClient(clientDTO)
        print ("\n Client %s was born! \n" % clientDTO.firstname  )
        
        
    #Remove Client
    def removeClient(self, clientDTO):
        '''Remove Client from database'''
        DB.rmClient(clientDTO)
        print ("Client %s removed" % clientDTO.firstname)
      

    def calcAVG(self, clientName, frequency):
        '''calculates average incomes from a client over weeks, day...'''


    def calcDebt(self, clientDTO):
        '''Calculates total debt of a costumer'''


    def listClientDebt(self, clientDTO):
        '''ainda nao faz nada'''
        
    #Insert Transaction in DB
    def makeTransaction(self, transactionDTO):
      DB. addTransaction(transactionDTO)
    
    
    
    
