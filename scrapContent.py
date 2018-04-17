from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4.element import Comment
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def scrap(body):
    global web
    web.get(str(body))
    html=web.page_source
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


options = Options()
browsers={}
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
options.add_argument("--headless")
web=webdriver.Firefox(firefox_options=options,capabilities=firefox_capabilities)






categories = ["Arts", "Games"]

for d in categories:
	succ=0
	prob=0
	f=open('SitesName/'+str(d),'r')
	c=f.read()
	lis=c.split('#^$')
	f2=open('SitesContents/'+str(d),'w')
	f3=open('SitesNotScrapped/'+str(d),'w')
	for i in lis:
		try:
			f2.write(str(scrap(i))+'#^$')
			print('Success : '+str(i))
		except:
			f3.write(str(i)+'#^$')
			print('Problem : '+str(i))

	f.close()
	f2.close()
	f3.close()
	f4=open('done','w+')
	f4.write(str(d)+'Content#')
	f4.close()
	print(' Success : '+str(succ))
	print(' Failed : '+str(prob))
	print(' Percentage : '+str((succ/(prob+succ))*100))	
