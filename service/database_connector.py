import mariadb

class DatabaseConnector:
    def __init__(self, user : str, password: str, host: str, port: int, database: str) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

        self.connected = False
    
    def connect(self) -> bool:
        try:
            self.conn = mariadb.connect(    user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            port=self.port,
                                            database=self.database
                                        )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")            
            return False

        self.cursor = self.conn.cursor()
        self.connected = True

        return True

    def close_connection(self) -> None:
        if self.connected:
            self.conn.close()

    def query(self, query: str):
        if not self.connected:
            print("Error : Not connected to database !")
            return

        self.cursor.execute(query)

        data = [ ]
        column_names = [ x[0] for x in self.cursor.description ]

        for row in self.cursor:
            row_data = { }
            for i in range(len(row)):
                col_name = column_names[i]
                row_data[col_name] = row[i]
            data.append(row_data)

        return data