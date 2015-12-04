#!/usr/bin/env python
#   coding:utf-8

import pymssql

class Tools:
	def __init__(self,Host,User,Password,Database):
		self.conn = pymssql.connect(host=Host,user=User,password=Password,database=Database)
		self.cursor = self.conn.cursor()
		
	def Query(self,q):
		r = self.cursor.execute('select * from jc39')
		r.fetchall()
		
		return r
	
	
	
	

