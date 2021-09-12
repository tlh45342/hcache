import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

# -------------------------------------------------------------------

def have_position(x):
    database = r"hcache.db"
    rows = []
    conn = create_connection(database)
    if conn is not None:
        query = ("SELECT * FROM position WHERE ticker = '"+x+"';")                             
        cursor = conn.cursor()
        count = cursor.execute(query)
        rows = cursor.fetchall() 
        #print ("OUT:",rows)
        cursor.close()
    else:
        print("Error! cannot create the database connection.")
    if rows == []:
        found = False
    else:
        found = True    
    return found

# -------------------------------------------------------------------

def return_position(x):
    database = r"hcache.db"
    rows = []
    conn = create_connection(database)
    if conn is not None:
        query = ("SELECT * FROM position WHERE 1=1;")                             
        cursor = conn.cursor()
        count = cursor.execute(query)
        rows = cursor.fetchall() 
        cursor.close()
    else:
        print("Error! cannot create the database connection.")
    return rows

# ------------------------------

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# ------------------------------
    
def create_1m():
    database = r"hcache.db"
    sql_create_trades_table = """ CREATE TABLE IF NOT EXISTS history_1m (
	                                    symbol text,
                                        open text,
                                        close text,
                                        high text,
                                        low text,
                                        volume text
                                    ); """
    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_trades_table)
    else:
        print("Error! cannot create the database connection.")

# ------------------------------

def create_listings():
    database = r"hcache.db"
    sql_create_trades_table = """ CREATE TABLE IF NOT EXISTS listings (
	                                    symbol text,
                                        securityname text,
                                        etf text
                                    ); """
    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_trades_table)
    else:
        print("Error! cannot create the database connection.")
        
# ------------------------------     
        
def insert_into_listings(symbol,securityname,etf):
    database = r"hcache.db"
    conn = create_connection(database)
    sqlite_statement = ("INSERT INTO listings (symbol, securityname, etf)\n" +
                           "VALUES(\""+symbol+"\"," +
                             "\""+securityname+"\","+
                             "\""+etf+"\""+");")
    cursor = conn.cursor()
    count = cursor.execute(sqlite_statement)
    conn.commit()
    cursor.close()

# ------------------------------
    
def download(tickers="", interval="", start=""):
    print("Searching:", tickers)
    return
