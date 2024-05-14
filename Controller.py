import mysql.connector


class Controller:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'Baklava21',
            'host': 'localhost',
            'database': 'GamingPlatforms',
            'port': '3306'
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print('Connected to MySQL database')

            self.connection.start_transaction(isolation_level='SERIALIZABLE')

        except mysql.connector.Error as e:
            print(f'Error connecting to MySQL database: {e}')

    def executeQuery(self, query):
        if not self.connection or not self.connection.is_connected():
            print('Not connected to MySQL database')
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            print('Rows:')
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print(f'Error executing query: {e}')
        finally:
            if 'cursor' in locals():
                cursor.close()

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('Disconnected from MySQL database')

    def showAllGames(self):
        if not self.connection or not self.connection.is_connected():
            print('Not connected to MySQL database')
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM Game')
            rows = cursor.fetchall()

            print('Games:')
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print(f'Error executing query: {e}')
        finally:
            if 'cursor' in locals():
                cursor.close()

    def showAllDLCs(self):
        if not self.connection or not self.connection.is_connected():
            print('Not connected to MySQL database')
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM DLC')
            rows = cursor.fetchall()

            print('DLCs:')
            for row in rows:
                print(row)
        except mysql.connector.Error as e:
            print(f'Error executing query: {e}')
        finally:
            if 'cursor' in locals():
                cursor.close()


    def addGame(self, Name, Price, ReleaseDate, AgeRestriction, GameFileSizeInGB, AchievementNumber):
        if not self.connection or not self.connection.is_connected():
            print('Not connected to MySQL database')
            return

        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Game(Name, Price, ReleaseDate, AgeRestriction, GameFileSizeInGB, AchievementNumber) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (Name, Price, ReleaseDate, AgeRestriction, GameFileSizeInGB, AchievementNumber))
            self.connection.commit()
            print('Game added successfully')
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f'Error adding game: {e}')
        finally:
            if 'cursor' in locals():
                cursor.close()

    def deleteGame(self, Id):
        if not self.connection or not self.connection.is_connected():
            print('Not connected to MySQL database')
            return
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Game WHERE Id = %s"
            cursor.execute(query, (Id,))
            self.connection.commit()
            print('Game deleted successfully')
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f'Error deleting game: {e}')
        finally:
            if 'cursor' in locals():
                cursor.close()

    def addDLC(self, GameId, Price, Name, Description):
        if not self.connection or not self.connection.is_connected():
            print('Not connected to MySQL database')
            return
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO DLC (GameId, Price, Name, Description) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (GameId, Price, Name, Description))
            self.connection.commit()
            print('DLC added successfully')
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f'Error adding DLC: {e}')
        finally:
            if 'cursor' in locals():
                cursor.close()

    def deleteDLC(self, Id):
        if not self.connection or not self.connection.is_connected():
            print('Not connected to MySQL database')
            return

        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM DLC WHERE Id = %s"
            cursor.execute(query, (Id,))
            self.connection.commit()
            print('DLC deleted successfully')
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f'Error deleting DLC: {e}')
        finally:
            if 'cursor' in locals():
                cursor.close()
