import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
import mysql.connector
#database init
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='abcde123',
    database='tweet'
)
mycursor=mydb.cursor()
formula="INSERT INTO test  VALUES (%s,%s)"
#end of database init
import  re #regex for phone number
def text_and_phone(tweet):
        for i in re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', tweet):
            if(len(i)<=10):
                return i

driver=Chrome()#chrome driver
driver.get("https://twitter.com/i/events/1385596085192691712")#static url for twitter india covid resources

#cards=driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
data=dict()

tweet_ids=set()
last_position=driver.execute_script("return window.pageYOffset;")

def get_tweet_data(card):
    return(card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text)
scrolling=True

while scrolling:
	print("tweets collected =",len(data))
	cards=driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
	for card in cards[-15:]:
		tweet=card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
		data[tweet]=text_and_phone(tweet)
		if tweet:
			tweet_id=''.join(tweet)
			if tweet_id in tweet_ids:
				tweet_ids.add(tweet_id)
				data.append(tweet)
	scroll_attempt=0
	while True:


		driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		sleep(1)
		curr_position=driver.execute_script("return window.pageYOffset;")
		if last_position == curr_position:
			scroll_attempt+=1
			if scroll_attempt>=3:
				scrolling=False
				break
			else:
				sleep(2)
		else:
			last_position = curr_position
			break
mycursor.execute("create table poo (text VARCHAR(500) , phone BIGINT unsigned)") # make database

formula="insert into poo  values ('%s', '%s')" # formula
for i in data:
    if data[i]:
        try:

            mycursor.execute(formula % (i,data[i]))
            mydb.commit()
        except:
            pass
