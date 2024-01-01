from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import schedule
import time
import json
from config_script import *

def setup_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(BROWSER_DRIVER_PATH, options=options)
    return driver

def scrape_jobs():
    driver = setup_driver()
    job_data = []

    urls = ["https://www.indeed.com", "https://www.linkedin.com"]
    for url in urls:
        for title in JOB_TITLES:
            search_url = f"{url}/jobs?q={'+'.join(title.split())}&l={JOB_LOCATION}"
            driver.get(search_url)
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            selector = WEBSITE_INSTRUCTIONS['Indeed']['class_name'] if 'indeed' in url.lower() else WEBSITE_INSTRUCTIONS['LinkedIn']['class_name']
            job_list = soup.find_all('div', class_=selector)

            for job in job_list[:5]:
                job_title = job.find('h2').get_text().strip() if job.find('h2') else 'No Title'
                job_data.append({'title': job_title})

                if len(job_data) >= 5:
                    break
            if len(job_data) >= 5:
                break
        if len(job_data) >= 5:
            break

    driver.quit()
    return job_data

def save_jobs(jobs):
    file_path = 'jobs.json'
    with open(file_path, 'w') as file:
        json.dump(jobs, file, indent=4)

def scheduled_scraping():
    scraped_jobs = scrape_jobs()
    save_jobs(scraped_jobs)

schedule.every().day.at(SCHEDULE_TIME).do(scheduled_scraping)

while True:
    schedule.run_pending()
    time.sleep(60)
