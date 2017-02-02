#!/usr/bin/env python3.5
import sqlite3
import json

# Below line establishes a connection to sqlite database file named blog.db and is located to thed in the said path. Please edit path based on the file location
conn = sqlite3.connect("/home/base/blog.db")

class post():
	def POST():
		tit = input("enter title: ")
		data = input("enter data to enter in blog: ")
		inser = [tit,data]
		conn.execute("insert into posts (title, body) \
			values (?,?)", inser)
		conn.commit()

class posts():
	def GET():
		cursor = conn.execute("select * from posts;")
		getdata = {row[0] :[row[1], row[2]] for row in cursor}
		print(getdata)

post.POST()
posts.GET()

