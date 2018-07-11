# 导入 mysql 驱动
import mysql.connector
# 注意把 password 设为nide root口令
conn = mysql.connector.connect(user='root', password='root', database='sfy')
cursor = conn.cursor()
# 创建user表
cursor.execute('create table user_python (id varchar(20) primary key, name varchar(20))')
# 插入一条记录,注意Mysql的占位符是%s
cursor.execute('insert into user_python(id, name) values(%s, %s)', ['1', 'shao'])
print(cursor.rowcount)
# 提交事务
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user_python where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection
cursor.close()
conn.close()