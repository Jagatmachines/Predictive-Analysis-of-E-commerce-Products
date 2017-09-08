import sqlite3
import datetime

def main():
    conn = sqlite3.connect('test.db')

    cursor = conn.execute("SELECT Rdate FROM RATING ORDER BY Rdate")
    row = cursor.fetchone()
    flag = False if row is None else True

    while flag:
        u = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
        d = datetime.timedelta(days=7)
        t = u + d
        ttdd = u.strftime('%Y-%m-%d')
        tt = t.strftime('%Y-%m-%d')

        cursor = conn.execute("SELECT Rating FROM RATING WHERE Rdate BETWEEN ? AND ?", [ttdd, tt])
        tot = 0
        rlist = [row[0] for row in cursor]
        for i, x in enumerate(rlist):
#            print ("{}) Rating = {:.2f}\n".format(i+1, x))
            tot += x

        count = len(rlist)
        if not count:
            count = 1
        avg = tot / count
#        print("Final rating = %.2f" % avg)

        cursor = conn.execute("SELECT TID FROM GEN ORDER BY TID DESC")
        row = cursor.fetchone()
        ident = 1 if row is None else row[0] + 1

        conn.execute("INSERT INTO GEN (TID, Totrating, Fdate, Tdate) VALUES (?, ?, ?, ?)", [ident, avg, ttdd, tt])

        cursor = conn.execute("SELECT Rdate FROM RATING WHERE Rdate > ? ORDER BY Rdate", [tt])
        row = cursor.fetchone()
        flag = False if row is None else True

    conn.commit()
    
    print("\n")

    cursor = conn.execute("SELECT TID, Totrating, Fdate, Tdate from GEN")
    for row in cursor:
        print ("WEEK = ", row[0])
        print ("TOTAL RATING = %.2f"% row[1])
        print ("FROMDATE = ", row[2])
        print ("TODATE = ", row[3], "\n")

    conn.close()