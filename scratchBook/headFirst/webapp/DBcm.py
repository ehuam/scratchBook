#! /usr/bin/python3
import mysql.connector

class ConnectionError(Exception):
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass

class UseDatabase:
    
    def __init__(self, config: dict) -> None:
        # set up code. Define the connection.
        self.__configuration = config
        
    
    def __enter__(self) -> 'cursor':
        # using the mysql.connector module
        # then create a connection and a cursor
       try:
           self.__conn = mysql.connector.connect(**self.__configuration)
           # create a cursor
           self.__cursor = self.__conn.cursor()
           return self.__cursor
       except mysql.connector.errors.InterfaceError as err:
           raise ConnectionError(err)
       except mysql.connector.errors.ProgrammingError as err:
           raise CredentialsError(err)
       return self.__cursor
        

    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        # after ensuring the data is saved, tidy up
        self.__conn.commit()
        self.__cursor.close()
        self.__conn.close()
