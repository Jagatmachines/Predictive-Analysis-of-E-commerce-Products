from lxml import html  
import csv,os,json
import requests
from exceptions import ValueError
from time import sleep
#Files
import test


from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

def AmzonParser(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url,headers=headers)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_TITLE = '//a[@data-hook="review-title"]//text()'
            XPATH_REVIEW = '//span[@data-hook="review-body"]//text()'
            XPATH_DATE = '//span[@data-hook="review-date"]//text()'
 
            RAW_TITLE = doc.xpath(XPATH_TITLE)
            RAW_REVIEW = doc.xpath(XPATH_REVIEW)
            RAW_DATE = doc.xpath(XPATH_DATE)
 
            TITLE = ' \n '.join([i.strip() for i in RAW_TITLE]) if RAW_TITLE else None
            REVIEW = ' \n '.join([i.strip() for i in RAW_REVIEW]) if RAW_REVIEW else None
            RDATE = ' \n '.join([i.strip() for i in RAW_DATE]) if RAW_DATE else None
            
            if page.status_code!=200:
                raise ValueError('captha')
            data = {
                    'URL':url,
                    'TITLE':TITLE,
                    'REVIEW' :REVIEW,
                    'RDATE' :RDATE
                    }
 
            return data
        except Exception as e:
            print (e)
 
def ReadAsin(AsinList, pstart, pstop):
    #Apple iPhone 5S 16GB Silver GSM Unlocked (Certified Refurbished)
    
    f=open("data.json","wb")
    
    extracted_data = []
    for j in range(int(pstart),int(pstop)):
    	url = "https://www.amazon.com/product-reviews/"+AsinList+"/ref=cm_cr_arp_d_viewopt_srt?sortBy=recent&pageNumber="+str(j)

    	print ("Processing: "+url)
    	extracted_data.append(AmzonParser(url))
    	sleep(5)
    json.dump(extracted_data,f,indent=4)
    

@app.route('/success/<name>')
def success(name):
	#ReadAsin(name)
	return 'Success %s' % name

	#return 'Succes %s' % name

@app.route('/fail/<name>')
def fail(name):
	print name
	return 'Fail %s' % name

@app.route('/scraptjgt', methods = ['GET', 'POST'])
def scraptjgt():
	if request.method == 'POST':
		asin = request.form['inputASIN']
		pname = request.form['inputName']
		pstart = request.form['inputstart']
		pstop = request.form['inputstop']
		ReadAsin(asin, pstart, pstop)
		test.main()
		
		return redirect('sucss.html')
	else:
		asin = request.args.get('inputASIN')
		pname = request.args.get('inputName')
		pstart = request.args.get('inputstart')
		pstop = request.args.get('inputstop')
		ReadAsin(asin, pstart, pstop)
		test.main()
		
		return redirect('sucss.html')

if __name__ == "__main__":
	app.debug = True
	app.run()
	app.run(debug = True)