#
# Kirjasto / Library sqlite3-sovellus
#

import sqlite3
from sqlite3 import Error
import csv

def create_database_connection(dbname):
    try:
        connection = sqlite3.connect(dbname)
        print(sqlite3.version)
        if connection is not None:
            create_table(connection, sql_create_customer_table)
            create_table(connection, sql_create_book_table)
            create_table(connection, sql_create_reserved_table)
        return connection    
    except Error as e:
        print(e)
    # finally:
    #    connection.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_customers_from_csv(conn):
    try:
        with open ('tieto.csv', 'r') as f:
            reader = csv.reader(f)
            columns = next(reader)
            query = 'INSERT INTO Asiakkaat({0}) values ({1})'
            query = query.format(','.join(columns), ','.join('?' * len(columns)))
            cursor = conn.cursor()
            for data in reader:
                cursor.execute(query, data)
                print(data)
                
    except Error as e:
        print(e)

def create_customer(conn, customer):
    """
    Create a new customer into the customers table
    :param conn:
    :param customer:
    :return: customer id
    """
    sql = ''' INSERT INTO Asiakkaat(id, name)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, customer)
    return cur.lastrowid

def create_book(conn, book):
    """
    Create a new book into the books table
    :param conn:
    :param book:
    :return: book id
    """
    sql = ''' INSERT INTO Kirjat(id, name, tekija, status, lainaaja, varaaja)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, book)
    return cur.lastrowid

def print_customer(connection, id):
    try:
        conn = connection.cursor()
        conn.execute('SELECT name FROM Asiakkaat WHERE id = %s' % id)
        rows = conn.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

def print_book(connection, id):
    try:
        conn = connection.cursor()
        conn.execute('SELECT name FROM Kirjat WHERE id = %s' % id)
        rows = conn.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

        
dbname = "C:\\development\\python_koodit\\PythonTutorial\\sqlitetesti.db"

# 0 = kirjastossa
# 1 = lainassa

# status    lainaaja    varauksia on
# 0         0           0
# 0         0           1
# 1         <id>        0
# 1	    <id>        1

# Varaukset-taulu
# id
# asiakasid
# kirjaid

sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS Asiakkaat (
                                id integer PRIMARY KEY,
                                name text NOT NULL
                            ); """
 
sql_create_book_table = """ CREATE TABLE IF NOT EXISTS Kirjat (
                                 id integer PRIMARY KEY,
                                 name text NOT NULL,
                                 tekija text NOT NULL,
                                 status integer DEFAULT 0,
                                 lainaaja integer DEFAULT 0,
                                 varaaja integer DEFAULT 0
                        ); """

sql_create_reserved_table = """ CREATE TABLE IF NOT EXISTS Varaukset (
                                id integer PRIMARY KEY,
                                asiakas integer,
                                kirja integer
                            ); """


# Kirjat
kirja1 = (1, "Arosusi", "Hermann Hesse", 0, 0, 0)
kirja2 = (2, "Seitsemän veljestä", "Aleksis Kivi", 0, 0, 0)
kirja3 = (3, "Kolme muskettisoturia", "Aleksandre Dumas", 0, 0, 0)
# Asiakkaat
asiakas1 = (1, "Janne")
asiakas2 = (2, "Sari")

dbconnection = create_database_connection(dbname)
"""
with dbconnection:
    create_customer(dbconnection, asiakas1)
    create_customer(dbconnection, asiakas2)
    create_book(dbconnection, kirja1)
    create_book(dbconnection, kirja2)
    create_book(dbconnection, kirja3)
"""

lopetus = False
asiakasid = 0
kirjaid = 0
while lopetus == False:
    print( "0. Lopeta")
    print( "1. Näytä asiakkaat")
    print( "2. Näytä kirjat")
    print( "3. Luo oletustietokanta")
    print( "4. Tyhjennä oletustietokanta")
    print( "5. Hae asiakas id:llä")
    print( "6. Hae kirja id:llä")
    print( "7. Lainaa kirja")
    print( "8. Palauta kirja")
    print( "9. Uusi asiakas")
    print( "10. Uusi kirja")
    print( "11. Tuhoa asiakas")
    print( "12. Tuhoa kirja")
    print( "13. Varaa kirja")
    print( "14. Peruuta kirjan varaukset")
    print( "15. Näytä kaikki varaukset")
    
    x = input()

    if x == "0":
        lopetus = True
        dbconnection.close()
    if x == "1":
        print("Kirjaston asiakkaat ovat: \n")
        for rivi in dbconnection.execute('SELECT * FROM Asiakkaat ORDER BY id'):
            print(rivi)
    if x == "2":
        print("Kirjaston kirjat ovat: \n")    
        for rivi in dbconnection.execute('SELECT * FROM Kirjat ORDER BY id'):
            print(rivi)
    if x == "3":
        #create_customer(dbconnection, asiakas1)
        #create_customer(dbconnection, asiakas2)
        create_customers_from_csv(dbconnection)
        create_book(dbconnection, kirja1)
        create_book(dbconnection, kirja2)
        create_book(dbconnection, kirja3)
    if x == "4":
        dbconnection.execute('DELETE FROM Asiakkaat')
        dbconnection.execute('DELETE FROM Kirjat')
    if x == "5":
        print("Anna asiakkaan id: ")
        asiakasid = input()
        cur = dbconnection.cursor()
        cur.execute('SELECT * FROM Asiakkaat WHERE id = ?', asiakasid)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    if x == "6":
        print("Anna kirjan id: ")
        kirjaid = input()
        cur = dbconnection.cursor()
        cur.execute('SELECT * FROM Kirjat WHERE id = ?', kirjaid)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    if x == "7":
        print("Lainataan kirja")
        print("Asiakas on %s" % asiakasid)
        print("Kirja on %s" % kirjaid)
        cur = dbconnection.cursor()
        cur.execute('UPDATE Kirjat SET status = 1, lainaaja = %s WHERE id = %s' % (asiakasid, kirjaid))
    if x == "8":
        print("Palautetaan kirja")
        print("Asiakas on %s" % asiakasid)
        print("Kirja on %s" % kirjaid)
        cur = dbconnection.cursor()
        cur.execute('UPDATE Kirjat SET status = 0, lainaaja = 0 WHERE id = %s' % (kirjaid))    
    if x == "9":
        print("Luo uusi asiakas")
        print("Anna uuden asiakkaan nimi")
        uusinimi = input()
        cur = dbconnection.cursor()
        cur.execute('INSERT INTO Asiakkaat(name) VALUES ("%s")' % (uusinimi))
    if x == "10":
        print("Luo uusi kirja")
        print("Anna uuden kirjan nimi")
        uusikirja = input()
        print("Anna uuden kirjan tekija")
        uusitekija = input()
        cur = dbconnection.cursor()
        cur.execute('INSERT INTO Kirjat(name, tekija) VALUES ("%s", "%s")' % (uusikirja, uusitekija))
    if x == "11":
        print("Poista asiakas id:llä")
        print("Anna poistettavan asiakkaan id")
        id_del = input()
        cur = dbconnection.cursor()
        cur.execute('DELETE FROM Asiakkaat WHERE id = %s' % (id_del))
    if x == "12":
        print("Poista kirja id:llä")
        print("Anna poistettavan kirjan id")
        id_del = input()
        cur = dbconnection.cursor()
        cur.execute('DELETE FROM Kirjat WHERE id = %s' % (id_del))
    if x == "13":
        print("Varaa kirja")
        print("Anna asiakas id")
        id_cust = input()
        print_customer(dbconnection, id_cust)
        print("Anna kirja id")
        id_book = input()
        print_book(dbconnection, id_book)
        cur = dbconnection.cursor()
        cur.execute('INSERT INTO Varaukset(asiakas, kirja) VALUES ("%s", "%s")' % (id_cust, id_book))
    if x == "14":
        print("Poista kirjavaraus")
        print("Anna asiakas id")
        id_cust = input()
        print_customer(dbconnection, id_cust)
        print("Anna kirja id")
        id_book = input()
        print_customer(dbconnection, id_book)
        cur = dbconnection.cursor()
        cur.execute('DELETE FROM Varaukset WHERE asiakas = %s AND kirja = %s' % (id_cust, id_book))
    if x == "15":
        print("Varatut kirjat")
        cur = dbconnection.cursor()
        cur.execute('SELECT Varaukset.id, Asiakkaat.name, Kirjat.name FROM Varaukset \
                     LEFT JOIN Asiakkaat ON Varaukset.asiakas = Asiakkaat.id \
                     LEFT JOIN Kirjat ON Varaukset.kirja = Kirjat.id')
        rows = cur.fetchall()
        for row in rows:
            print(row)







