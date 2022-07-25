from sqlalchemy import create_engine
import pyodbc

#class Config:
SERVER='localhost'
#DRIVER='odbc_driver'
DRIVER='ODBC Driver 17 for SQL Server'
DATABASE='recetas'
    #SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://sa:sa@{SERVER}/{DATABASE}'
SQLALCHEMY_DATABASE_URI = f'mssql://sa:sa@{SERVER}/{DATABASE}?driver={DRIVER}'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
engine=create_engine(SQLALCHEMY_DATABASE_URI)
conn = engine.connect()
print(conn)

cursor = conn.cursor()
cursor.execute('select * from recetas')

for row in cursor.fetchall():
    print (row)