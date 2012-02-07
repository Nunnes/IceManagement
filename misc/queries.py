#!/usr/bin/env python

import pymysql

#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')

conn = pymysql.connect(host='localhost', user='ice_manager', passwd='ice', db='ice_db')
   

cur = conn.cursor()

cur.execute("SELECT * FROM customer")

# print cur.description

# r = cur.fetchall()
# print r
# ...or...
for r in cur.fetchall():
   print r

cur.close()
conn.close()

