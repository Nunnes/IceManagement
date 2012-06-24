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

    #Faz commit da BD e fecha o conector
    def closeDb(self):
        self.conn.commit()
        self.conn.close()
        

    #func interna para determinar qual o maior id
    def maxId (self, table):
        cur = self.conn.cursor()
        query_str = "SELECT MAX(id) FROM %s" % table 
        #"SELECT MAX(id) FROM Customer"
        cur.execute(query_str)
        nc_t = cur.fetchall() #retorna uma lista de tuples
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

    #fazer parse do nome ? ou acrescentar mais first e last name no DTO
    def getClientID(clienDTO):
        cur = self.conn.cursor()
        
        query_str = "SELECT * FROM Customer" 
        cur.execute(query_str)
        results = cur.fetchall() #retorna uma lista de tuples
        cur.close()
        return results[0][0]

    # return list of clients
    def listClient(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Customer")
        listc = cur.fetchall() # retorna uma lista de tuples
        cur.close()
        return listc

    # add new transaction
   # def addTransaction(self, transactionDTO, clientDTO):
    #    ''' Add transaction to db'''
     #   cur = self.conn.cursor()
      #  #select client ID to insert in the transaction
       # clientID = self.getClientID(clientDTO)
       # query_str = "INSERT INTO Transaction" + \
       #     " VALUES(" + \
        #    " " + repr(self.maxId("Transactions")+1)[:-1] + "," + \
         #   " " + repr(transactionDTO.quantity) + "," + \
          #  " " + repr(transactionDTO.price) + "," + \
           # " " + repr(transactionDTO.credit) + "," + \
           # " " + " SYSDATE," + \ 
           # " " + clientID + "," + \

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
        
    #return list of all transactions ordered by date 
    def listTransaction(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Transaction ORDER BY data_transaction")
        listc = cur.fetchall() #retorna uma lista de tuples
        cur.close()
        return listc


    #retorna lista de clientes com fiados
    def listClient_with_Debt(self):
        cur = self.conn.cursor()
        cur.execute("SELECT first_name, price, data_transaction, amount  FROM Customer, Transaction WHERE Transaction.on_credit= true AND Transaction.customer_id = Customer.id ORDER BY data_transaction ")
        listc = cur.fetchall() #retorna uma lista de tuples
        cur.close()
        return listc

        #cur.execute("INSERT INTO Transaction VALUES (1, 2, 23.00, false, '2010-03-12', 1)")
       # cur.close()
       # print("Inserted")

    #def calcDebt(self, ClientName):
        #'''Calculates total debt of a costumer'''


    #def listClientDebt(self,clientDTO):
        
        
        

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

    
