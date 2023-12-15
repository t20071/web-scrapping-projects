# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import time

# Prompt user to input skills they are not familiar with
print('put some skill that you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering_out {unfamiliar_skills}')

# Function to find and save relevant job listings
def find_jobs():
    # Define the URL for job search
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Research+Associate%22&txtKeywords=%22Research+Associate%22&txtLocation="
    
    # Fetch HTML content from the URL
    html_text = requests.get(url).text
   
    # Create a BeautifulSoup object for parsing HTML
    soup = BeautifulSoup(html_text,'lxml')
    
    # Find all job listings on the page
    jobs = soup.find_all("li",class_ ="clearfix job-bx wht-shd-bx")
   
    # Iterate through each job listing
    for index,job in enumerate(jobs):
        # Extract the published date of the job
        published_date = job.find('span',class_="sim-posted").text

        # Check if the job was posted recently
        if 'few' in published_date:
            # Extract company name, required skills, and more information link
            company_name = job.find('h3',class_="joblist-comp-name").text.replace("  ",' ')
            skills = job.find('span',class_ = "srp-skills").text
            more_info = job.header.h2.a['href']
            
            # Check if unfamiliar skills are not required for the job
            if unfamiliar_skills not in skills:
                # Save job information to a text file
                with open(f'post/{index}.txt','w') as f:
                    f.write(f'company Name : {company_name.strip()} \n')
                    f.write(f'Required skills :{skills.strip()} \n')
                    f.write(f'published data : {published_date.strip()} \n')
                    f.write(f'more_info : {more_info}')

                # Print a message indicating the file has been saved
                print(f'File saved: {index}')

# Run the job search function in an infinite loop with a delay
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minute.....')
        time.sleep(time_wait*60)
