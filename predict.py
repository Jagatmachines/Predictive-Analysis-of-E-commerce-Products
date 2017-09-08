import sqlite3

def main():
	conn = sqlite3.connect('test.db')

	rt1=0
	rt=0
	b=0
	a=0
	b=0
	ft=[]
	cursor = conn.execute("SELECT TID,Totrating FROM GEN")
	for row in cursor:
		wk=row[0]
		rt=row[1]
#		print("Wk=%d and rt=%2f"%(wk,rt))
		if wk==1:
			rt1=rt
		else:
			ft.append(rt-rt1)
			rt1=rt
	f = open("predict.txt","w")

	for row in ft:
#		print("ft=%2f"%row)
		b+=row
	if b>1 or rt1>5:
#		print("\nSuccess=%2f"%b)
		print("\nThe product will be a success in the future")
		f.write("The product will be a success in the future")
	elif b<1 or rt1<5:
#		print("\nFailure=%2f"%b)
		print("\nThe product will be a failure in the future")
		f.write("The product will be a failure in the future")
	else:
#		print("\nNeutral=%2f"%b)
		print("\nThe product will be a neutral in the future")
		f.write("The product will be a neutral in the future")
	conn.commit()
	conn.close()
	f.close()

if __name__ == "__main__":
    main()