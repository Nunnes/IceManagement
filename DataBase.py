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

    # change nc
    def setNumClient(self):
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM customer")
        nc_t = cur.fetchall() # retorna uma lista de tuples
        self.nc = nc_t[0][0] # a primeira entrada do primeiro tuple
        cur.close()

    # return list of clients
    def listClient(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM customer")
        listc = cur.fetchall() # retorna uma lista de tuples
        cur.close()
        return listc

    # add new client
    #def addClient(self):

    # add new 