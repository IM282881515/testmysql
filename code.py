#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='282881515',
        db ='test'
        )

cur = conn.cursor()

#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
sqli="insert into student values(%s,%s,%s,%s)"
cur.execute(sqli,('3','Huhu','2 year 1 class','7'))
rec = cur.execute('select * from student')
bdr = cur.fetchall()
print bdr
cur.close()
conn.commit()
conn.close()