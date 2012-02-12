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
        self.conn.close()

    #func interna para determinar qual o maior id
    def maxId (self):
        cur = self.conn.cursor()
        cur.execute("SELECT MAX(id) FROM Customer")
        nc_t = cur.fetchall() # retorna uma lista de tuples
        cur.close()
        return nc_t[0][0]

    # add new client
    # dif py3 [:-1]
    def addClient(self, clientDTO):
        cur = self.conn.cursor()
        query_str = "INSERT INTO Customer" + \
            " VALUES(" + \
            " " + repr(self.maxId()+1)[:-1] + "," + \
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
    

    # add new transaction
    def addTransaction(self, transactionDTO):
        print("to implement")

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

    
