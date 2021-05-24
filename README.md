# IVR_CovibotWebsite
So our basic idea is to make a covid resource website using a database verified by our own covid bot using Interactive voice response which is generally used in the call center industry. IVR bot is used to call, play automated voice recording and then receive keypad inputs from the user. This greatly helps in verifying everything. The data can then be stored in the database with a verified tick and then be shown on the website. This data can be scrapped multiple times and can be verified by our bot to at last been shown on the website. With data being collected both by the website submit link and web scrapping. During this pandemic there was huge influx of covid-19 resources but limited human resource which could verify the resources. So we came up with the solution . We use the already existing IVR technology  to confirm the resources. IVR which is interactive voice response is the same technology which asks you to press 1 for English.

SOFTWARE -Python, At commands , serial port connections , DTMF Input , pygame library , Html , CSS , Php , Mysql , phpmyadmin , getpass , csv, selenium.webdriver.common.keys , selenium.common.exceptions , selenium.webdriver , mysql.connector , Html Apis 

Hardware side- Ardruino Uno , Connecting wires , DC buck converter or lipo battery , serial to ardruino wire , resistors ,Gsm module sim 800 l

#Files description
1. https://github.com/DevbyHitanshu/IVR_CovibotWebsite/blob/main/IVR%20BOT%20CODE.py - is for the bot code
It calls the mobile numbers from the database and runs series of pre recorder voice for telling them to put in input, then it records the input and modifies the data into the database wiith verified
2. https://github.com/DevbyHitanshu/IVR_CovibotWebsite/blob/main/Database.sql is for the database maintained
3. https://github.com/DevbyHitanshu/IVR_CovibotWebsite/blob/main/site.php is the backend framework for calling html on a local server and mke paths for web hosting
4. https://github.com/DevbyHitanshu/IVR_CovibotWebsite/blob/main/Web%20scapping.py is the script for filtering thousands of tweets for mobile numbers and data and entering everything into the database created for the input for the bot
5. https://github.com/DevbyHitanshu/IVR_CovibotWebsite/blob/main/index1.text is the homepage site 
