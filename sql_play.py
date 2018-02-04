
import pymysql

from db_setup import SQL_SETUP

connection = pymysql.connect(host='localhost',
                             user='justin',
                             password='sonic',
                             db='play',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# setup
cursor =  connection.cursor()
sql = SQL_SETUP
cursor.execute(sql)



