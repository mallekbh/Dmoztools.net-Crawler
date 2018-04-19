
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


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
    	return False
    if isinstance(element, Comment):
        return False
    return True


options = Options()
browsers={}
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
options.add_argument("--headless")
web=webdriver.Firefox(firefox_options=options,capabilities=firefox_capabilities)






categories = ['Society','Health','Business','Recreation','Sports','Computers','Home','Reference','Shopping','Kids_and_Teens','News','Science']
max=0
total=0
files={}
lis={}
problems={}
for i in categories:
	f=open('SitesName/'+str(i),'r')
	tex=f.read()
	lis[str(i)]=tex.split('#^$')
	total=total+len(lis)
	if len(lis[str(i)])>max:
		max=len(lis)
	f.close()
	files[str(i)]=open('SitesContent/'+str(i),'w')
	problems[str(i)]=open('SitesProblem/'+str(i),'w')


i=0
for d in range(0,max):
	succ=0
	prob=0
	for x in categories:
		if len(lis[str(x)])>d:
			i=i+1
			try:
				files[str(x)].write(str(scrap(str(lis[str(x)][d])))+'#^$')
				print('Success : '+str(i))
				succ=succ+1
			except:
				problems[str(x)].write(str(lis[str(x)][d])+'#^$')
				print('Problem : '+str(i))
				prob=prob+1
		print('Remaining : '+str(total-i))
print(' Success : '+str(succ))
print(' Failed : '+str(prob))
print(' Percentage : '+str((succ/(prob+succ))*100)+'%')

for r in categories:
	files[str(r)].close()
	problems[str(r)].close()
