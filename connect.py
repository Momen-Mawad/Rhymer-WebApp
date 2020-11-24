import psycopg2, pandas as pd

try:
    connection = psycopg2.connect(user="postgres",
                                  password="126134",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Rhymer")
    cursor = connection.cursor()
    postgreSQL_select_Query = 'SELECT * FROM public."Sylvia Plath"'

    cursor.execute(postgreSQL_select_Query)
    poem_records = cursor.fetchall()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

#poem_records= poem_records[1:50]

df = pd.DataFrame(poem_records, columns=['poemName', 'text', 'syllables'])
