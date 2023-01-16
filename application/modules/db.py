import mysql.connector
import random, string
import os

class UrlExistsError(Exception):
    pass



class url_model():
    def __init__(self) -> None:
        query ="CREATE TABLE IF NOT EXISTS urls(short varchar(5),long_url varchar(255));"
        self.__sql_query(query,fetchtype=3)
        
    def get_short_from_long(self,long: str) -> tuple:
        query = "SELECT short FROM urls WHERE long_url=%s"
        return self.__sql_query(query,(long,),fetchtype=2)[0]
    
    def get_long_from_short(self,short) -> tuple:
        query = "SELECT long_url FROM urls WHERE short=%s"
        return self.__sql_query(query,(short,),fetchtype=2)[0]
    
    def create_short_from_long(self,long) -> str:
        if self.__sql_query("SELECT True FROM urls WHERE long_url = %s;",(long,)):
            raise UrlExistsError("The Value already exists in the database")
        while True:
            short = ''.join(random.choice(string.ascii_letters) for x in range(5))
            print(short)
            if not self.__sql_query("SELECT True FROM urls WHERE short = %s;",(short,)):
                break
        query = f"INSERT INTO urls(short,long_url) VALUES(%s,%s)"
        self.__sql_query(query,(short,long),fetchtype=3)
        return short
    
    def get_all_db_rows(self):
        query = "SELECT short,long_url FROM urls;"
        return self.__sql_query(query,fetchtype=1)
    
    def delete_row(self,short):
        query = "DELETE FROM urls WHERE short=%s"
        return self.__sql_query(query,parameters=(short,),fetchtype=3)
    
    def __sql_query(self,query: str,parameters={},fetchtype: int = 1):
        """Handles a database connection to the hardcoded databases.

        Args:
            query (str): SQL Query as string
            parameters (dict | list | tuple): Parameters of Query passed as iterable
            fetchtype (int, optional): Type of Query and the Fetchtype it should expect: 
                1: Multiple Row 
                2: Single Row
                3: Commit to Database
        Returns:
            tuple | bool: Returns the dataset if its a Fetch, otherwise it returns True on a successful Commit
        """
        conn = mysql.connector.connect(
            user=str(os.environ.get("DB_USER")),
            host=str(os.environ.get("DB_HOST")),
            database=str(os.environ.get("DB_NAME")),
            password=str(os.environ.get("DB_PASS"))
        )
        c = conn.cursor()
        c.execute(query,parameters)
        if fetchtype == 1:
            data_list = c.fetchall()
        elif fetchtype == 2:
            data_list = c.fetchone()
        elif fetchtype == 3:
            conn.commit()
            data_list = True
        conn.close()
        return data_list
