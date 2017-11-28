#!/usr/bin/python3

import sqlite3

#name your db and connect
db = sqlite3.connect("stuff.db") 

db.execute("drop table if exists items")

#types and columns
db. execute("create table items(id int, name text, color text)")

#just add data
db.execute("insert into items(id, name, color) values(1, 'onething', 'black')")
db.execute("insert into items(id, name, color) values(2, 'twothing', 'orange')")
db.execute("insert into items(id, name, color) values(3, 'threething', 'yellow')")
db.execute("insert into items(id, name, color) values(4, 'fourthing', 'red')")

db.commit()

#simple query
results = db.execute("select * from items")

for row in results:
	print(row)

#specific query
specific_result = db.execute("select * from items where id = 4")

for row in specific_result:
	print(row)

#update
update_entry = db.execute("update items set color = 'blue' where id=3 ")
db.commit()
update_results = db.execute("select * from items")

for row in update_results:
	print(row)

#delete
delete_entry = db.execute("delete from items where id=1 ")
db.commit()
delete_results = db.execute("select * from items")
for row in delete_results:
	print(row)
	
