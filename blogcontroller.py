#!/usr/bin/env python3.5
import sqlite3
import json

# Below line establishes a connection to sqlite database file named blog.db and is located to thed in the said path. Please edit path based on the file location
conn = sqlite3.connect("/home/base/blog.db")

class post():
	def POST():
		conn.execute("insert into posts (title, body) \
			values ('Fifth Post', 'Fifth post content');")
		conn.commit()

class posts():
	def get():
		cursor = conn.execute("select * from posts;")
		for row in cursor:
			print(row[0])
			print(row[1])
			print(row[2])

post.POST()
posts.get()

