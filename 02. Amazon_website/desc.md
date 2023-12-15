# Amazon Earphone Scraper

This Python script is designed to scrape information about wired earphones available on Amazon.in. The script uses BeautifulSoup to parse the HTML content of the Amazon search results page for earphones, extracting details such as brand, rating, reviewer count, and price for each earphone.

## Features

- **Web Scraping:** Utilizes the BeautifulSoup library to scrape relevant information from the Amazon search results page for earphones.

- **Retry Mechanism:** Implements a retry mechanism to handle connection errors gracefully. If a connection error occurs, the script retries up to a specified number of times before giving up.

- **Data Storage:** Saves the extracted information for each earphone in individual text files within the 'data' directory.

- **Continuous Execution:** Runs the scraping function in an infinite loop with a specified time delay between each execution, allowing for periodic updates on earphone details.
