## Job Scraper for TimesJobs

### Introduction

This project is a web scraper designed to fetch job listings from the TimesJobs website. It filters job opportunities based on user-defined skills, enabling users to find relevant positions in their desired field. The primary purpose is to save time by automating the process of searching for jobs that match specific skillsets while ignoring those that require unfamiliar skills.

### Features

1. **Skill Filtering:**
   - Users can input skills they are not familiar with to filter out job listings that require those skills.
   - The script dynamically adjusts the search criteria based on user input.

2. **Job Information Extraction:**
   - Extracts relevant information from job listings, including company name, required skills, published date, and a link to more information.
   - Saves the extracted information in individual text files for each job post.

3. **Continuous Monitoring:**
   - The script runs in an infinite loop, regularly fetching and filtering job listings.
   - Includes a wait time between iterations to avoid overloading the website.

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-scraper.git
   cd job-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python job_scraper.py
   ```
   - Input skills you are not familiar with when prompted.
   - The script will continuously fetch and filter job listings, saving relevant information to text files.

### Dependencies

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): Used for pulling data out of HTML files.
- [Requests](https://docs.python-requests.org/en/master/): Used for making HTTP requests to fetch the HTML content of the job listings.

