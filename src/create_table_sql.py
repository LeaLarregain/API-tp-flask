from sqlalchemy import create_engine
from sqlalchemy import text

db_string = "postgresql://root:root@localhost:5432/store"

engine = create_engine(db_string)
connection = engine.connect()

create_user_table_query = """
CREATE TABLE IF NOT EXISTS Users (
    id serial primary key,
    firstname text,
    lastname text,
    age int,
    email char(50),
    job char(50)
);
"""

create_application_table_query = """
CREATE TABLE IF NOT EXISTS Application (
    id serial primary key,
    appname text,
    username text,
    lastconnection date,
    user_id int references Users(id)
);
"""

#CREATE

#insert_data_query = """INSERT INTO films(title, director, year) VALUES('Doctor Strange','Scott Derrickson','2016')"""


connection.execute(text(create_user_table_query))
connection.execute(text(create_application_table_query))

connection.commit()
connection.close()