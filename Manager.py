#!/usr/bin/env python

import ClientDTO
import TransactionDTO
import DataBase

# ligacao ah base de dados
DB = DataBase.DataBase( 'localhost',
                        'ice_manager',
                        'ice',
                        'ice_db');


class Manager:
    '''Represents Manager: trata da base de dados e da logica de negocio'''

    def __init__(self):
        '''Initializes the Data manager'''
        print("Voodoo magic is about to happen!")

    #Fechar DB
    def closeDb(self):
        DB.closeDb()

    ### Clientes ###
    #Cria Client

    def createClient(self, clientDTO):
        DB.addClient(clientDTO)
        print("\n Cliente %s acabou de ser criado! \n" % clientDTO.firstname)

    #Remove Client
    def removeClient(self, clientDTO):
        '''Remove Client from database'''
        DB.rmClient(clientDTO)
        print ("Client %s removed" % clientDTO.firstname)

    # imprime a lista de clientes
    def printClientList(self):
        print ("Lista de clientes: ")
        clist = DB.listClient()

        for c in clist:
            print (c)

    ### Transactions ###
    #Insere Transaction na DB
    def makeTransaction(self, transactionDTO):
        DB.addTransaction(transactionDTO)

    #imprime a lista de Transaccoes
    def printTransactionList(self):
        print ("Lista de transaccoes: ")
        tlist = DB.listTransaction()

        for t in tlist:
            print (t)

    #Pede ah base de dados pelos fiados de dado
    def listClient_with_Debt(self):
        '''Lista os fiados de dado cliente'''
        listaClientes = DB.listClient_with_Debt()

        for c in listaClientes:
            print (c)



    def calcAVG(self, clientName, frequency):
        '''calculates average incomes from a client over weeks, day...'''


    def calcDebt(self, clientDTO):
        '''Calculates total debt of a costumer'''

    def listClientDebt(self, clientDTO):
        '''ainda nao faz nada'''

    #Insert Transaction in DB
    def makeTransaction(self, transactionDTO):
        DB.addTransaction(transactionDTO)
