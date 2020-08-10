import pymysql
# 连接配置信息
config = {
    'host':'123.57.53.215',
    'port':3306,
    'user':'root',
    'password':'qingclass@2020',
    'db':'mysb_test',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
}
# 创建连接
connection = pymysql.connect(**config)
a = 101333
b = 101278
# 执行sql语句
try:
    with connection.cursor() as cursor:
        sql = 'SELECT * from user_levels where squirrelUserId in (%s,%s)'
        cursor.execute(sql,(a,b))
        r = cursor.fetchall()
        print(r)
        connection.commit()
        cursor.close()
finally:
    connection.close()

