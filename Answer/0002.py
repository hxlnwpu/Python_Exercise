#coding=utf-8

import pymysql.cursors, uuid

def getCoupon(n):
    uuids = []
    for i in range(n):
	    uuids.append(uuid.uuid1())
    return uuids

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='pythontest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
       code=getCoupon(10)
       for i in range(len(code)):
        # Read a single record
            sql = "insert into code values (i,code[i]);"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
finally:
    connection.close()