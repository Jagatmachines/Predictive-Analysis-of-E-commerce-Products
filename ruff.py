import sqlite3

def main():
	conn = sqlite3.connect('ruff.db')
	print ("Opened database successfully")

	conn.execute("DROP TABLE GEN")
	conn.commit()

	conn.execute('''CREATE TABLE GEN
	            (TID        INT PRIMARY KEY NOT NULL,
	            Totrating   DECIMAL         NOT NULL)''')
	print ("GEN table created successfully")

	conn.commit()

	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (1, 2)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (2, 5)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (3, 6)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (4, 5)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (5, 6)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (6, 7)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (7, 8)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (8, 6)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (9, 5)")
	conn.commit()
	conn.execute("INSERT INTO GEN (TID, Totrating) VALUES (10, 5)")
	conn.commit()

	conn.close();

if __name__ == "__main__":
    main()