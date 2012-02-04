#!/usr/bin/env python
import Classes

clientList = []

class Manager:
    '''Represents a Data Manager: trata da base de dados e da logica de negocio''' 
    
    def __init__(self):
        '''Initializes the Data manager'''
        print 'Voodoo magic is about to happen!'
 
    def printClientList(self):
        i=0
	print 'Client List: '
        for cl in clientList:
            i+=1
            print ('%d - %s'  % (i, cl.name ))

    def createClient(self):
        '''Create a client'''
        name = raw_input('Nome do Cliente: ')
        clientList.append(Classes.Client(name))
        print '\n Client ' + name + ' was born! \n'
       
    def removeClient(self):
        '''Remove Client from database'''
        name = raw_input('Nome do Cliente a remover: ')
        for cl in clientList:
            if cl.name == name:
                cl.delete() # como eliminar objecto???
                clientList.remove(cl)

    def changeName(self):
        name = raw_input('Nome do Cliente a remover: ')
        for cl in clientList:
            if cl.name == name:
                cl.setName(name)
            else: 
                print 'Client %s not found.\n' % name 

    def insertClient(self):
        '''Add Client to database'''  
    
    def howMany(self):
        Classe.Client.howMany()

    def calcAVG(self, clientName, frequency):
        '''calculates average incomes from a client over weeks, day...'''

    def calcDebt(self, ClientName):
        '''Calculates total debt of a costumer'''

    def makeTransaction(self):
       '''Makes a transaction '''
       name = raw_input("Client: ")
       for cl in clientList:
           if cl.name == name:
               cl.buyIce()
           else: print 'Client not found!\n'

    