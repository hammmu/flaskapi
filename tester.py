import pymssql

# Establishing connection to the MySQL database
try:
    # Replace 'username', 'password', 'hostname', 'database_name' with your credentials
    conn = pymssql.connect(server="209.134.48.123", user="SA",
                                    password="9ypybzq97ylVPVsdhQRw", database="HomeHealthStaging", as_dict=True)
    print("Connected to MySQL database successfully")

    # Perform operations here...
    # Creating a cursor object
    # Creating a cursor object
    cursor = conn.cursor()

    # Executing the query to fetch all tables
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")

    # Fetching all tables from the cursor
    tables = cursor.fetchall()

    # Displaying the tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Closing the cursor and connection
    cursor.close()
    # Closing the connection
    conn.close()
    print("Connection closed")
except pymssql.Error as error:
    print("Failed to connect to MySQL: {}".format(error))
