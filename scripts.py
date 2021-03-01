import mysql.connector as mysql
from mysql.connector import errorcode
# Current date time in local system 
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table,Column,Integer,String,Float,Date,SmallInteger,Text,ForeignKey
from sqlalchemy.orm import mapper,sessionmaker
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
from sqlalchemy.ext.declarative import declarative_base
import enum
import sqlalchemy as sa

import os

Base = declarative_base()
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

print('\n--- MYSQL Datase `classicmodels` connection ok --- ')

metadata = MetaData()

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
                Column('salesRepEmployeeNumber',Integer,nullable = True),
                Column('creditLimit',Float(10,2)),
                    )

employees = Table('employees',metadata,
                Column('employeeNumber',Integer,primary_key = True),
                Column('lastName',String(50)),
                Column('firstName',String(50)),
                Column('extension',String(10)),
                Column('email',String(100)),
                Column('officeCode',String(10)),
                Column('reportsTo',Integer,nullable = True),
                Column('jobTitle',String(50)),
                    )

offices = Table('offices',metadata,
                Column('officeCode',String(10),primary_key = True),
                Column('city',String(50)),
                Column('phone',String(50)),
                Column('addressLine1',String(50)),
                Column('addressLine2',String(50),nullable = True),
                Column('state',String(50),nullable = True),
                Column('country',String(50)),
                Column('postalCode',String(15)),
                Column('territory',String(10))
                    )
orderdetails = Table('orderdetails',metadata,
                Column('orderNumber',Integer,primary_key = True),
                Column('productCode',String(15),primary_key = True),
                Column('quantityOrdered',Integer),
                Column('priceEach',Float(10,2)),
                Column('orderLineNumber',SmallInteger)
                    )
orders = Table('orders',metadata,
                Column('orderNumber',Integer,primary_key = True),
                Column('orderDate',Date),
                Column('requiredDate',Date),
                Column('shippedDate',Date,nullable = True),
                Column('status',String(15)),
                Column('comments',Text,nullable = True),
                Column('customerNumber',Integer)
                    )
payments = Table('payments',metadata,
                Column('customerNumber',Integer,primary_key = True),
                Column('checkNumber',String(50),primary_key = True),
                Column('paymentDate',Date),
                Column('amount',Float(10,2))
                    )
productlines = Table('productlines',metadata,
                Column('productLine',String(50),primary_key = True),
                Column('textDescription',String(4000),nullable = True),
                Column('htmlDescription',MEDIUMTEXT,nullable = True),
                Column('image',MEDIUMBLOB,nullable = True),
                    )
products = Table('products',metadata,
                Column('productCode',String(15),primary_key = True),
                Column('productName',String(70)),
                Column('productLine',String(50)),
                Column('productScale',String(10)),
                Column('productVendor',String(50)),
                Column('productDescription',TEXT),
                Column('quantityInStock',SMALLINT),
                Column('buyPrice',Float(10,2)),
                Column('MSRP',Float(10,2))
                    )


class Office(Base):
     __tablename__ = 'offices'

     officeCode = Column(String(10),primary_key = True)
     country = Column(String(50))
     state = Column(String(50),nullable = True)
     city = Column(String(50))

     def __repr__(self):
        return "<offices(officeCode='%s', country='%s', state='%s', city='%s')>" % (self.officeCode, self.country, self.state, self.city)

class MyEnum(enum.Enum):
    first = "1:10"
    second = "1:12"
    third = "1:18"
    four = "1:24"
    five = "1:32"
    six = "1:50"
    seven = "1:700"
    eight = "1:72"

class product(Base):
    __tablename__ = "products"
    # Pass the enum table (not the enum class) to enumtables.EnumColumn
    # It replaces sqlalchemy.Column, but aside from the enum table,
    # it can take the same parameters.
    # It will automatically create a ForeignKeyConstraint referencing the enum table.
    enum_value = db.EnumColumn(product, primary_key = True)


Session=sessionmaker()
Session.configure(bind=engine)
session=Session()

office_list = session.query(offices);
employee_number = session.query(employees);
#payments_list = session.query();

for offices in office_list:
    print(offices.officeCode,offices.country,offices.state,offices.city)


# pull metadata of a table
#metadata = db.MetaData(bind=engine)
#metadata.reflect(only=['test_table'])

#test_table = metadata.tables['test_table']
#test_table

print('--- Pull Metadata done -- \n')
