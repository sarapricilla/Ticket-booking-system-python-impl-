import pymysql

class DBUtil:
    @staticmethod
    def getDBConn():
        return pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="ticketbookingsystem",
            port=3306
        )
