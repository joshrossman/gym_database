import mysql.connector
from mysql.connector import Error

db_name='my_gym'
user='root'
password='rootPassword1919'
host='localhost'

def my_connect():
    try: 
        conn=mysql.connector.connect(
            database=db_name,
            user=user,
            host=host,
            password=password
        )
        print('MySQL connected.')
        return conn
    except Exception as e:
        print(f'Error:{e}. Could not create connection')
        return None
    

