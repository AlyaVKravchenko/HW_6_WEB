import psycopg2
from contextlib import contextmanager
from psycopg2 import Error


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """

    try:
        conn = psycopg2.connect(host='localhost', database='myhw', user='postgres', password='pass', port='5432')
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")



#import sqlite3
#from contextlib import contextmanager

#database = './test.db'


#@contextmanager
#def create_connection(db_file):
 #   """ create a database connection to a SQLite database """
  #  conn = sqlite3.connect(db_file)
   # yield conn
    #conn.rollback()
    #conn.close()