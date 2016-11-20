import pymysql

connection = pymysql.Connect(host='localhost',
                             user='root',
                             password='',
                             db='xLuis',
                              charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             );
