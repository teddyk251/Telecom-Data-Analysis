import re
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

def create_schema(table_name: str, data: dict, primary_key: str, foreign_key: str = '', additional_data: dict = {}) -> str:
    """
        A simple function which tries to create a schema for a sql table
        Parameters
        ----------
        table_name:
            Type: str
        data:
            Type: dict
        primary_key:
            Type: str
        foreign_key:
            Type: str
            Default value = ''
        additional_data:
            Type: dict
            Default value = {}

        Returns
        -------
        str
    """
    schema = f"CREATE TABLE IF NOT EXISTS `{table_name}` ("

    for key, value in data.items():
        schema += f"`{key}` {value},\n"

    if(foreign_key != ''):
        schema += f"PRIMARY KEY(`{primary_key}`),\nFOREIGN KEY(`{foreign_key}`)\n)"
    else:
        schema += f"PRIMARY KEY(`{primary_key}`)\n)"

    for key, value in additional_data.items():
        schema += f" {key} = {value} "

    schema += ';'

    return schema


def save_schema(name: str, schema: str):
    """
        A simple function which saves a string on a file returning positive number if it is successful
        Parameters
        ----------
        name:
            Type: str
        schema:
            Type: str

        Returns
        -------
        int
    """
    with open(name, 'w') as schema_file:
        success = schema_file.write(schema)
    return success


def create_and_save_schema(file_name: str, table_name: str, data: dict, primary_key: str, foreign_key: str = '', additional_data: dict = {}):
    """
        A function which combies the create and save schema functions together
        Parameters
        ----------
        file_name:
            Type: str
        table_name:
            Type: str
        data:
            Type: dict
        primary_key:
            Type: str
        foreign_key:
            Type: str
            Default value = ''
        additional_data:
            Type: dict
            Default value = {}

        Returns
        -------
        int
    """
    schema = create_schema(table_name, data,
                           primary_key, foreign_key, additional_data)
    success = save_schema(file_name, schema)

    return success


def DBConnect(dbName=None):
    """
    A simple function which connects to the local database reutrning the connection and cursor of the database
    Parameters
    ----------
    dbName :
        Default value = None

    Returns
    -------
    tuple
    """
    conn = mysql.connect(host='localhost', user='root', password='',
                         database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur


def createDB(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()


def alter_DB(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
    cur.execute(dbQuery)
    conn.commit()


def createTable(dbName: str, table_schema: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)
    fd = open(table_schema, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return


def get_unique_list_values(list_obj: list):
    seen = set()
    return [x for x in list_obj if not (x in seen or seen.add(x))]


def get_table_columns(table_schema: str):
    with open(table_schema, 'r') as schema:
        data = schema.read()
    columns = re.findall('`(.+)`', data)
    columns[0] = columns[0][columns[0].find('(') + 2:]
    columns = get_unique_list_values(columns)
    return columns


def get_selected_row_data(row: list, len: int):
    data = []
    for i in range(len):
        data.append(row[i])

    return set(data)


def insert_to_table(dbName: str, df: pd.DataFrame, table_name: str, table_schema: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (user_id, engagement_score, experience_score, satisfaction_score) VALUES(%s,%s,%s,%s);"""
  
        data = (float(row[0]), int(row[1]), int(row[2]), int(row[3]))


        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            # print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)

    print("All Data Inserted Successfully")
    return


def db_get_values(dbName: str):
    conn, cur = DBConnect(dbName)
    sqlQuery = 'SELECT * FROM user_satisfaction LIMIT 10;'
    try:
        cur.execute(sqlQuery)
        result = cur.fetchall()
        conn.commit()
        return result
    except Exception as e:
        conn.rollback()
        print("Error: ", e)


def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    """

    Parameters
    ----------
    *args :

    many :
         (Default value = False)
    tablename :
         (Default value = '')
    rdf :
         (Default value = True)
    **kwargs :


    Returns
    -------

    """
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} records fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res



