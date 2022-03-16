# Homes For Sale

https://homes-for-sale-web-scraper.herokuapp.com/

## Goal
Answer the question, What houses are for sale in my local postcode ?

## Solution
I have built a web scraper that looks at https://www.allhomes.com.au/ and extracts the houses for sale depending on the postcode entered.

### What is happening?
The postcode you entered gets inputted in to https://www.allhomes.com.au/ . It then searches the web page and extracts all addresses for that given postcode and this is what you see.</br>
The Python library used for web scraping is [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).</br>
The Pyhton web framework used is [Flask](https://flask.palletsprojects.com/en/2.0.x/).</br>
All data comes from https://www.allhomes.com.au/

### Deployement
The app is deployed in [heroku](https://www.heroku.com/).
