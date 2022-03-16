from bs4 import BeautifulSoup
import requests
print("Setup Complete!")

postcode =  input()

if len(str(postcode))>4 or len(str(postcode))<4:
  print("Invalid postcode, must be 4 digits long!")
  exit()

url = f"https://www.allhomes.com.au/sale/search?page=1&postcode={postcode}"
response = requests.get(url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')

pages_num = scraped.find_all(class_ = 'css-3ebg57')
pages=[1]
for x in pages_num:
  pages.append(int(x.get_text()))
last_page = max(pages)

for x in range(0,last_page):
  url = f"https://www.allhomes.com.au/sale/search?page={x}&postcode={postcode}"
  response = requests.get(url)
  html = response.content
  scraped = BeautifulSoup(html, 'html.parser')

  houses = scraped.find_all(class_ = 'css-1l8qi96')

  for y in houses:
    house = y.get_text()
    print(house) #outputs all houses