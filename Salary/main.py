import psycopg2
from config import host, user, password, db_name

connection = None

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # the cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")



    # create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE employees(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             salary int NOT NULL);"""
    #     )
    #     print("[INFO] Table created successfully")


    # insert the data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT into employees(first_name, salary) VALUES
    #         ('Andrew', 5000),
    #         ('Arnold', 2500),
    #         ('David', 7000),
    #         ('Daniel', 9000),
    #         ('Harry', 5000),
    #         ('James', 5700);
    #         """
    #     )
    #     print("[INFO] Table created successfully")    

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)

finally:
    if connection is not None:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
