import csv
import sqlite3

def main():
	conn = sqlite3.connect('test.db')
	print ("\nCSV file created")
	cursor=conn.execute("SELECT TID,Totrating, Fdate, Tdate FROM GEN")

	fields=[['Week','Rating','From Date','To Date']]

	# with open('weeklyrating.csv','w',newline='') as fp:
	with open('weeklyrating.csv','w') as fp:
		a=csv.writer(fp,delimiter=',')
		a.writerows(fields)
		for x in cursor:
			data=[[x[0],x[1],x[2],x[3]]]
			a.writerows(data)

	conn.close()