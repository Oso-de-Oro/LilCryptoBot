from bs4 import BeautifulSoup
from random import *
import requests
import twitter
import json
import time

api = twitter.Api(consumer_key='xxxxxxxxxxxxxxxxx',
                                consumer_secret='xxxxxxxxxxxxxxxxxxx',
                                access_token_key='xxxxxxxxxxxxx-xxxxxxxxxxxxx',
                                access_token_secret='xxxxxxxxxxxxxxxxxxxxxx')

statuses = api.GetUserTimeline(878690810409222145,include_rts=False,exclude_replies=True,count=200)

def main():

    x = randint(1,100)
    if x <= 12:
        message = bitcoin()
    elif x > 12 and x <= 23:
        message = blockchain()
    elif x > 23 and x <= 34:
        message = altcoin()
    elif x > 34 and x <= 67:
        message = coindesk()
    elif x > 67 and x <= 100:
        message = cnbc()
    try:
	print message
        status = api.PostUpdate(message)
    except Exception as e:
        print e

def bitcoin():

    url = "https://cointelegraph.com/tags/bitcoin"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    tights = []
    links = []
    views = []
    dates = []

    for link in soup.find_all("figure", {"class":"col-sm-8"}):

        x = link.find("a")
        d = link.find_all("span")
        y = link.find("span",{"class":"date"})

        if x.text is not None and x["href"] is not None and y.text is not None and ("HOURS" in y.text or "HOUR" in y.text):

            ch = False
	    for stat in statuses:
                veo = json.loads(str(stat))
                try:
                    if x["href"] == veo["urls"].values()[0]:
			ch = True
		    else:
			continue
                except Exception as e:
                    continue
    	    if ch == False:
	    	tights.append(x.text.encode("utf-8"))
            	links.append(x["href"].encode("utf-8"))
            	views.append(int(d[3].text))
            	dates.append(y.text.encode("utf-8"))
	    else:
		continue
    final = 0

    if len(tights) == 0:
    	time.sleep(60)
	return blockchain()
    else:
    	for i in range(0,len(tights)):
            if views[i] >= views[final]:
            	final = i
    	return tights[final] + " " + links[final] 

def blockchain():

    url = "https://cointelegraph.com/tags/blockchain"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    tights = []
    links = []
    views = []
    dates = []

    for link in soup.find_all("figure", {"class":"col-sm-8"}):

        x = link.find("a")
        d = link.find_all("span")
        y = link.find("span",{"class":"date"})

        if x.text is not None and x["href"] is not None and y.text is not None and ("HOURS" in y.text or "HOUR" in y.text):
            ch = False
	    for stat in statuses:
                veo = json.loads(str(stat))
                try:
                    if x["href"] == veo["urls"].values()[0]:
                        ch = True
		    else: 
			continue
                except Exception as e:
                    continue

            if ch == False:
            	tights.append(x.text.encode("utf-8"))
            	links.append(x["href"].encode("utf-8"))
            	views.append(int(d[3].text))
            	dates.append(y.text.encode("utf-8"))
	    else:
		continue

    final = 0

    if len(tights) == 0:
    	time.sleep(60)
	return altcoin()
    else:
    	for i in range(0,len(tights)):
            if views[i] >= views[final]:
            	final = i
    	return tights[final] + " " + links[final]

def altcoin():

    url = "https://cointelegraph.com/tags/altcoin"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    tights = []
    links = []
    views = []
    dates = []

    for link in soup.find_all("figure", {"class":"col-sm-8"}):
        x = link.find("a")
        d = link.find_all("span")
        y = link.find("span",{"class":"date"})
	ch = False
        if x.text is not None and x["href"] is not None and y.text is not None and ("HOURS" in y.text or "HOUR" in y.text):
            for stat in statuses:
                veo = json.loads(str(stat))
                try:
                    if x["href"] == veo["urls"].values()[0]:
                        ch = True 
		    else:
			continue
                except Exception as e:
                    continue
            if ch == False:
            	tights.append(x.text.encode("utf-8"))
            	links.append(x["href"].encode("utf-8"))
            	views.append(int(d[3].text))
            	dates.append(y.text.encode("utf-8"))
	    else:
		continue

    final = 0

    if len(tights) == 0:
    	time.sleep(60)
	return coindesk()
    else:
    	for i in range(0,len(tights)):
            if views[i] >= views[final]:
            	final = i
    	return tights[final] + " " + links[final]

def coindesk():

    url = "https://www.coindesk.com"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    tights = []
    links = []
    dates = []

    for link in soup.find_all("div", {"class":"post-info"}):
        q = link.find("p")
        x = q.find("time")
        y = link.find("a")
        ch = False

        if y.text is not None and y["href"] is not None and x["datetime"] is not None:
            for stat in statuses:
                veo = json.loads(str(stat))
                try:
                    if y["href"] == veo["urls"].values()[0]:
                        ch = True
                except:
                    continue

	if ch == False:
	    tights.append(y.text.encode("utf-8"))
	    links.append(y["href"].encode("utf-8"))
	    dates.append(x["datetime"])
	else:
	    continue

    final = 0

    if len(tights) == 0:
    	time.sleep(60)
	return cnbc()
    else:
    	for i in range(0,len(dates)):
            if dates[i] >= dates[final]:
            	final = i
    	return tights[final] + " " + links[final]

def cnbc():

    url = "https://search.cnbc.com/rs/search/view.html?source=CNBC.com&categories=exclude&partnerId=2000&keywords=BITCOIN"
    soup = BeautifulSoup(requests.get(url).text,'html.parser')
    sent = False
    for link in soup.find_all("div", {"class":"SearchResultCard"}):
        q = link.find("a")
        if q.text is not None and q["href"] is not None and "video" not in q["href"]:
            x = False
            for stat in statuses:
                veo = json.loads(str(stat))
                try:
                    if q["href"] == veo["urls"].values()[0]:
                        x = True
                    else:
                        continue
                except:
                    continue
            if x == False:
                return q.text.encode("utf-8") + " " + q["href"].encode("utf-8")
		sent = True
                break
            else:
                continue
    if sent == False:
    	time.sleep(60)
	return bitcoin()
    else:
	pass

try:
    main()
except:
    time.sleep(60)
    main()
