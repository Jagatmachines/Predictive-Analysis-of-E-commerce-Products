#!/usr/bin/python

import sqlite3

def main():
	conn = sqlite3.connect('test.db')
	print ("Opened database successfully")


	'''
	haha=CREATE PROCEDURE myproc\
	AS\
	BEGIN\
	Declare @MaxNo int,@No varchar(50);\
		Select @MaxNo=ISNULL(Max(Cast(RIGHT(ID,9) as Int)),0)+1 From RATING;\
		Set @No='RT'+Right('00000'+CAST(@MaxNo AS varchar),5);\
	END'''


	conn.execute("DROP TABLE RATING")
	conn.execute("DROP TABLE GEN")
	conn.commit()

	conn.close()






