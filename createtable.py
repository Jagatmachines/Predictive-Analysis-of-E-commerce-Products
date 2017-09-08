import sqlite3

def main():
	conn = sqlite3.connect('test.db')
	print ("Opened database successfully")

	conn.execute('''CREATE TABLE RATING
	            (ID     INT PRIMARY KEY NOT NULL,
	            Rating  DECIMAL         NOT NULL,
	            Rdate   DATE            NOT NULL)''')
	print ("RATING table created successfully")

	conn.execute('''CREATE TABLE GEN
	            (TID        INT PRIMARY KEY NOT NULL,
	            Totrating   DECIMAL         NOT NULL,
	            Fdate       DATE            NOT NULL,
	            Tdate       DATE            NOT NULL)''')
	print ("GEN table created successfully")

	conn.commit()

	conn.close();