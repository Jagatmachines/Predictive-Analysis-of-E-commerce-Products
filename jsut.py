#set up matplotlib and the figure
import matplotlib.pyplot as plt
import sqlite3

def main():
	pass
	plt.figure
	conn = sqlite3.connect('test.db')

	week=[0]
	rate=[0]

	i=1

	cursor = conn.execute("SELECT TID, Totrating from GEN")
	for row in cursor:
	   week.append(row[0])
	   rate.append(row[1])
	   i+=1
	 
	#create data
	x_series = week
	y_series_1 = rate

	 
	#plot data
	plt.plot(week, rate, label="Week:Rating")

	 
	#add in labels and title
	plt.xlabel("Week")
	plt.ylabel("Rating")
	plt.title("Graph")
	 
	#add limits to the x and y axis
	#plt.xlim(0, 10)
	plt.ylim(0, 10) 
	 
	#create legend
	plt.legend(loc="upper left")
	 
	#save figure to png
	plt.savefig("maj.png")
	plt.show()
	print("\nLine graph plotted")