
# define your connection characteristics
dbconfig = { 'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'vsearchpasswd',
             'database': 'vsearchlogDB', }

# import the database driver
import mysql.conector


#establish a connection
conn = mysql.connector.connect(**dbconfig)

#and create a cursor (file handler equivalent)
cursor = conn.cursor()

#assign a query to a string (note the five place holder args)
_SQL = """insert into log
          (phrase, letters, ip, browser_string, results)
          values
          (%s,%s,%s,%s,%s)"""

#send the query to the server, remembering to provide values
# for each of the required arguments (in a tuple).
cursor.execute(_SQL, ('galaxy', 'xyz', '127.0.0.1', 'Opera', "{'x','y'}"))


#force the database to write your data.
conn.commit()

#retrieve the (just written) data from the table,
_SQL = """select * from log"""

for row in cursor.fetchall():
    print(row) #displaying the output row by row

#tidy up when you're done
cursor.close()
conn.close()

cursor.execute(_SQL)

