import sqlite3

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

# -------------------------------------------------------------------

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# ------------------------------------------------------------------- 
    
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
        
def insert_into_history_1m(bar):
    database = r"tradinghook.db"
    conn = create_connection(database)
    print(account)
    print(type(account))
    sqlite_statement = ("INSERT INTO hisotry_1m (userid,fundid,exchangeid,settled,unsettled)\n" +
                           "VALUES(\""+str(account['userid'])+"\"," +
                             "\""+str(account['fundid'])+"\","+
                             "\""+str(account['exchangeid'])+"\","+
                             "\""+str(account['settled'])+"\","+
                             "\""+str(account['unsettled'])+"\");")
    print(sqlite_statement)
    cursor = conn.cursor()
    count = cursor.execute(sqlite_statement)
    conn.commit()
    print("Record inserted successfully into TRADINGHOOK.DB table ", cursor.rowcount)
    cursor.close()

# ------------------------------
    
def download(tickers="", interval="", start=""):
    print("Searching:", tickers)
    return
