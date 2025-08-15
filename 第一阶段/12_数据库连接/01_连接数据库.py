from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='1234',
    autocommit=True # 设置自动提交，就不用手动commit
)

# print(conn.get_server_info())

# 创建数据库
cursor = conn.cursor()
create_db_sql = 'CREATE DATABASE IF NOT EXISTS test'
cursor.execute(create_db_sql)

# 选择数据库
conn.select_db('test')
# 创建表
sql = """
create table if not exists student(
    id int auto_increment primary key,
    name varchar(20) not null,
    age int
)"""
cursor.execute(sql)

# 插入数据
insert_sql = 'insert into student(name, age) values (%s, %s)'
stu1 = ('张三', 15)
cursor.execute(insert_sql, stu1)
# 批量插入数据
data = [
    ('李四', 24),
    ('王五', 18),
]
cursor.executemany(insert_sql, data)
# 提交事务，对数据库有修改操作行为，需要commit
conn.commit()

# 查询数据
cursor.execute('select * from student')
results = cursor.fetchall() # ((1, '张三', 15), (2, '李四', 24), (3, '王五', 18))
for r in results:
    print(r)

cursor.close()
conn.close()