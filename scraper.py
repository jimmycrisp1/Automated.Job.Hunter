
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import schedule
import time
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
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

def send_email(file_path=None, content=None):
    message = MIMEMultipart()
    message['From'] = EMAIL_SENDER
    message['To'] = EMAIL_RECEIVER
    message['Subject'] = "Daily Job Scraping Results"

    body = content if content else "Please find the attached job scraping results."
    message.attach(MIMEText(body, 'plain'))

    if file_path:
        attachment = open(file_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={file_path}")
        message.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())
    server.quit()

def save_and_send_jobs(jobs):
    file_path = 'jobs.json'
    with open(file_path, 'w') as file:
        json.dump(jobs, file, indent=4)
    send_email(file_path=file_path)

def scheduled_scraping():
    scraped_jobs = scrape_jobs()
    save_and_send_jobs(scraped_jobs)

schedule.every().day.at(SCHEDULE_TIME).do(scheduled_scraping)

while True:
    schedule.run_pending()
    time.sleep(60)
