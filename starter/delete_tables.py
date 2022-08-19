import psycopg2
from psycopg2 import Error

from database import get_connected

from customers import create_customers, insert_customers
from invoices import create_invoices, insert_invoices


try:
    
    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()

    ############### CREATING TABLES AND INSERTING INFORMATION ###############

    delete_customers = """ DROP TABLE customers; """
    delete_invoices = """ DROP TABLE invoices; """

    cursor.execute(delete_customers)
    connection.commit()
    print("customers deleted")

    cursor.execute(delete_invoices)
    connection.commit()
    print("invoices deleted")


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")
