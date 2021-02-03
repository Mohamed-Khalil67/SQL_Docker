import mysql.connector as mysql
from mysql.connector import errorcode
# Current date time in local system 
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table,Column,Integer,String,Float,Date
from sqlalchemy.orm import mapper,sessionmaker

import os

# specify database configurations
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'mohamed',
    'password': 'mohamed',
    'database': 'classicmodels'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
connection = engine.connect()

print('--- MySQL Docker Container Python connection ok -- \n')

print('--- docker ps info --- \n')

os.system("docker ps")

print('--- MYSQL Datase `classicmodels` connection ok --- ')

metadata = MetaData()

payments = Table('payments',metadata,
                Column('customerNumber',Integer,primary_key = True),
                Column('checkNumber',String(50),primary_key = True),
                Column('paymentDate',Date),
                Column('amount',Float(10,2))
                    )

customers = Table('customers',metadata,
                Column('customerNumber',Integer,primary_key = True),
                Column('customerName',String(50)),
                Column('contactLastName',String(50)),
                Column('contactFirstName',String(50)),
                Column('phone',String(50)),
                Column('addressLine1',String(50)),
                Column('addressLine2',String(50),nullable = True),
                Column('city',String(50)),
                Column('state',String(50),nullable = True),
                Column('postalCode',String(50),nullable = True),
                Column('country',String(50)),
                Column('salesRepEmployeeNumber',Integer,nullable = True),M,
                Column('creditLimit',String(50),Float(10,2)),
                    )

Session=sessionmaker()
Session.configure(bind=engine)
session=Session()

payment_list = session.query(payments).limit(5);

for payments in payment_list:
    print(payments.customerNumber)


# pull metadata of a table
#metadata = db.MetaData(bind=engine)
#metadata.reflect(only=['test_table'])

#test_table = metadata.tables['test_table']
#test_table

print('--- Pull Metadata done -- \n')
