# import neccesary libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

def amazon_earphone():
    # connect to the the website
    url = "https://www.amazon.in/s?k=earphones+wired&ref=nb_sb_ss_ts-doa-p_1_9"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page,"html.parser")

    # Find all the earphone detail
    earphones= soup.find_all('div',class_= "puisg-col-inner")
    

    # iterate through all the earphone d
    for index,earphone in enumerate(earphones):
        brand = earphone.find('span',class_= "a-size-medium a-color-base a-text-normal").text
        rating = earphone.find('i',class_ = "a-icon a-icon-star-small a-star-small-4 aok-align-bottom")
        reviewer = earphone.find('span',class_= "a-size-base s-underline-text")
        price = earphone.find("span",class_="a-price-whole")

        # Check if brand_element, price_element, and reviewer_element are not None before accessing their attributes
        brand = brand.text.strip().split(':')[0] if brand else 'N/A'
        rating = rating.text.strip() if rating else 'N/A'
        reviewer = reviewer.text.strip() if reviewer else 'N/A'
        price = price.text if price else 'N/A'

        # storing 
        with open(f'data/{index}.txt','w') as f:
            f.write(f'brand : {brand} \n')
            f.write(f'rating :{rating} \n')
            f.write(f'reviewer : {reviewer} \n')
            f.write(f'price : {price}')

    # Print a message indicating the file has been saved
    print(f'File saved: {index}')

# Run the job search function in an infinite loop with a delay
if __name__ == '__main__':
    while True:
        amazon_earphone()
        time_wait = 10
        print(f'waiting {time_wait} minute.....')
        time.sleep(time_wait*60)