import pymssql

# Establishing connection to the MySQL database
try:
    # Replace 'username', 'password', 'hostname', 'database_name' with your credentials
    conn = pymssql.connect(server="209.134.48.122", user="SA",
                                    password="9ypybzq97ylVPVsdhQRw", database="HomeHealthStaging", as_dict=True)
    print("Connected to MySQL database successfully")

    # Perform operations here...

    # Closing the connection
    conn.close()
    print("Connection closed")
except pymssql.Error as error:
    print("Failed to connect to MySQL: {}".format(error))
