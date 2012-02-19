#!/usr/bin/env python

# Classe para interagir com a base de dados

import pymysql

class DataBase:

    # Construtor
    # 'localhost', 'ice_manager', 'ice', 'ice_db'
    def __init__(self, dbHost, dbUser, dbPass, dbDb):
        # ligacao ah bd
        self.conn = pymysql.connect(host=dbHost, user=dbUser, 
                                    passwd=dbPass, db=dbDb)
        # number of clients in db
        self.nc = 0 
        self.setNumClient()

    def closeDb(self):
        self.conn.commit()
        self.conn.close()

    #func interna para determinar qual o maior id
    def maxId (self, str_table):
        cur = self.conn.cursor()
        cur.execute("SELECT MAX(id) FROM " + str_table)
        nc_t = cur.fetchall() # retorna uma lista de tuples
        cur.close()
        return nc_t[0][0]

    # add new client
    # dif py3 [:-1]
    def addClient(self, clientDTO):
        cur = self.conn.cursor()
        query_str = "INSERT INTO Customer" + \
            " VALUES(" + \
            " " + repr(self.maxId("Customer")+1)[:-1] + "," + \
            " '" + clientDTO.firstname + "'," + \
            " '" + clientDTO.lastname + "'," + \
            " " + repr(clientDTO.phone)  + "," + \
            " '" + clientDTO.email + "'" + \
            " )"
        cur.execute(query_str)
        cur.close()

    # remove a client
    def rmClient(self, clientDTO):
        cur = self.conn.cursor()
        query_str = "DELETE FROM Customer WHERE" + \
            " first_name = '" + clientDTO.firstname + "'" + \
            " AND" + \
            " last_name = '" + clientDTO.lastname + "'"
        cur.execute(query_str)
        cur.close()

    # change nc
    def setNumClient(self):
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM Customer")
        nc_t = cur.fetchall() # retorna uma lista de tuples
        self.nc = nc_t[0][0] # a primeira entrada do primeiro tuple
        cur.close()


        
    # return list of clients
    def listClient(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Customer")
        listc = cur.fetchall() # retorna uma lista de tuples
        cur.close()
        return listc

    # get client id
    def getClientId(self, firstName, lastName):
        cur = self.conn.cursor()
        cur.execute("SELECT id FROM Customer WHERE first_name = '" 
                    + firstName + "' AND last_name = '" + lastName + "'")
        id_t = cur.fetchall() # retorna uma lista de tuples
        id_int = id_t[0][0] # a primeira entrada do primeiro tuple
        cur.close()
        return id_int


    # add new transaction
    def addTransaction(self, transactionDTO):
        cur = self.conn.cursor()

        # saber qual o id do cliente
        client_id = self.getClientId(transactionDTO.clientFirstName, 
                                transactionDTO.clientLastName)

        # Passar para inteiro e depois string o credito
        if (transactionDTO.credit):
            credit = "true"
        else:
            credit = "false"

        query_str = "INSERT INTO Transaction" + \
            " VALUES(" + \
            " " + repr(self.maxId("Transaction")+1)[:-1] + "," + \
            " " + repr(transactionDTO.quantity) + "," + \
            " " + repr(transactionDTO.price) + "," + \
            " " + credit + "," + \
            " '" + "2010-03-12" + "'," + \
            " " + repr(client_id)[:-1] + \
            " )"
        cur.execute(query_str)
        cur.close()


        #cur.execute("INSERT INTO Transaction VALUES (1, 2, 23.00, false, '2010-03-12', 1)")
       # cur.close()
       # print("Inserted")

    #def calcDebt(self, ClientName):
        #'''Calculates total debt of a costumer'''


    #def listClientDebt(self,name):
        

    #return a clientDTO
        
    def getClient(self, clientDTO):
        print("to implement")

    #return a TransactionDTO
    #def getTransactionDTO(self, clientDTO)

    #list of a client's credit transactions
    #def getClientCredit(self, clientDTO):
    
    # pay credit -> change credit to false
    # pay a transaction
    #def setTransactionCredit(self, credit=false)

    
