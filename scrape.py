import requests
from bs4 import BeautifulSoup
import pandas as pd

# Job
job_title = 'python-developer-jobs'

def scrape_job_listings(job_title)->pd.DataFrame:
    # URL
    URL = 'https://www.reed.co.uk'

    # set the number of pages to scrape
    Numpage = 0
    
    # Number of jobs to scrape 
    JOB_COUNT = 1

    agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 Vivaldi/5.3.2679.70.'}

    #create DataFrame
    df = pd.DataFrame(columns=['title', 'company', 'location', 'posted_date', 'description', 'skills'])

    while len(df) < JOB_COUNT:
        # Update page number
        Numpage += 1

        url = f"{URL}/jobs/{job_title}?pageno={Numpage}"
        print(url)
        page = requests.get(url, headers=agent)
        soup = BeautifulSoup(page.content, 'html.parser')

        # find all job listings on the page
        job_listings = soup.find_all('article', class_='job-result-card')

        # loop through each job listing and extract the data
        for job in job_listings:
            if len(job_listings) == JOB_COUNT:
                break

            job_url = job.find('h2', class_='job-result-heading__title').find('a')['href']
            print(job_url)
            job_page = requests.get(URL+job_url)
            job_soup = BeautifulSoup(job_page.content, 'html.parser')

            # get the job title
            job_title = job.find(name='h2', attrs = {'class':'job-result-heading__title'}).find('a')['title']

            # get the job location
            job_location = job.find(name='li', attrs= {'class':'job-metadata__item job-metadata__item--location'}).text.strip()
            
            # get the job description
            job_description = job_soup.find(name='span', attrs = {'itemprop': 'description'}).text.strip()

            # # get the job technologies
            if job_soup.find(name='ul', attrs={'class':'list-unstyled skills-list'}) is not None:
                skills = job_soup.find(name='ul', attrs={'class':'list-unstyled skills-list'}).text.strip()
            else:
                skills = "Not Specified"

            # # get the job posted date
            posted_date = job_soup.find(name='div', attrs = {'class': 'posted'}).find('meta')['content']

            # # get the company name
            company_name = job.find(name='a', attrs = {'class': 'gtmJobListingPostedBy'}).text.strip()

            # create a pandas DataFrame with the extracted data
            df_temp = pd.DataFrame({'title': [job_title], 'company': [company_name], 'location': [job_location], 
                'posted_date': [posted_date], 'description': [job_description], 'skills': [skills]})
            
            # Append DataFrame
            df = pd.concat([df, df_temp], axis= 0)

    return df


def save_in_database():
    #establishing the connection
    #conn = psycopg2.connect(
    #database="postgres", user='postgres', password='password', host='localhost', port= '5432'
    #)
    pass

df_job_listings = scrape_job_listings(job_title)
df_job_listings.to_csv("jobs.csv")
