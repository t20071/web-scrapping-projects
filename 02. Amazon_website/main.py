# import necessary libraries
from bs4 import BeautifulSoup
import requests
import time

def amazon_earphone():
    # Specify the URL for Amazon earphones search
    url = "https://www.amazon.in/s?k=earphones+wired&ref=nb_sb_ss_ts-doa-p_1_9"
    
    # Set headers to mimic a browser's request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    # Set the maximum number of retry attempts on connection error
    max_retries = 3
    for attempt in range(max_retries):
        try:
            # Make a request to the specified URL with headers
            page = requests.get(url, headers=headers)
            break  # If successful, exit the loop
        except requests.exceptions.ConnectionError as e:
            if attempt < max_retries - 1:
                # If a connection error occurs, retry with a delay
                print(f"Connection error, retrying ({attempt + 1}/{max_retries})...")
                time.sleep(5)  # Wait for 5 seconds before retrying
            else:
                # If max retries exceeded, print an error message and exit
                print("Max retries exceeded. Exiting...")
                return

    # Use BeautifulSoup to parse the HTML content of the page
    soup = BeautifulSoup(page.text, "html.parser")
    
    # Find all the earphone details on the page
    earphones = soup.find_all('div', class_="puisg-col-inner")

    # Iterate through all the earphones
    for index, earphone in enumerate(earphones):
        # Extract relevant details for each earphone
        brand = earphone.find('span', class_="a-size-medium a-color-base a-text-normal")
        rating = earphone.find('i', class_="a-icon a-icon-star-small a-star-small-4 aok-align-bottom")
        reviewer = earphone.find('span', class_="a-size-base s-underline-text")
        price = earphone.find("span", class_="a-price-whole")

        # Check if elements are not None before accessing their attributes
        brand = brand.text.strip().split(':')[0] if brand else 'N/A'
        rating = rating.text.strip() if rating else 'N/A'
        reviewer = reviewer.text.strip() if reviewer else 'N/A'
        price = price.text if price else 'N/A'

        # Store extracted information in a text file
        with open(f'data/{index}.txt', 'w') as f:
            f.write(f'brand : {brand} \n')
            f.write(f'rating : {rating} \n')
            f.write(f'reviewer : {reviewer} \n')
            f.write(f'price : {price}')

    # Print a message indicating the file has been saved
    print(f'File saved: {index}')

# Run the job search function in an infinite loop with a specified delay
if __name__ == '__main__':
    while True:
        amazon_earphone()
        time_wait = 10
        print(f'waiting {time_wait} minute(s).....')
        time.sleep(time_wait * 60)
