import psycopg2, pandas as pd
import pandas.io.sql as psql

connection = psycopg2.connect(user="postgres",
                              password="126134",
                              database="Rhymer")

postgreSQL_select_Query = 'SELECT * FROM public.lyrics WHERE'

cursor = connection.cursor()

cursor.execute(postgreSQL_select_Query)

records = cursor.fetchall()


#cursor.close()
#connection.close()