import matplotlib.pyplot as plt
import sqlite3

def main():
	pos=0
	neg=0
	neu=0
	conn = sqlite3.connect('test.db')
	cursor = conn.execute("SELECT Rating FROM RATING")
	for row in cursor:
		if row[0]>5.5:
			pos+=1
		elif row[0]<5:
			neg+=1
		else:
			neu+=1

	labels = ['Positive','Neutral','Negative']
	sizes = [pos,neu,neg]
	colors = ['green','yellow','red']
	patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
	plt.legend(patches, labels, loc="best")
	plt.axis('equal')
	plt.tight_layout()
	plt.savefig("majpie.png")
	print("\nPie Chart plotted")
	conn.close()

if __name__ == "__main__":
    main()