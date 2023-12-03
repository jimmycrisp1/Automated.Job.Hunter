
# Automated Job Hunter

This repository contains a Python script designed to automate the process of scraping job postings for Salesforce Administrator positions from websites like Indeed and LinkedIn. The script supports both email automation to send scraped job listings and an option to run without email automation.

## Features

- **Web Scraping**: Automated scraping of job listings using Selenium and BeautifulSoup.
- **Email Automation**: Sends scraped job listings via email.
- **Customizable Configuration**: Easily configurable for different job titles, locations, and other preferences.
- **Scheduled Execution**: Runs daily at a specified time.

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/automated-job-hunt.git
cd automated-job-hunt
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### WebDriver Setup
- Download the appropriate WebDriver (e.g., ChromeDriver for Google Chrome).
- Ensure it is either in your system's PATH or specify its path in the `config_script.py`.

### Configure the Script
Update `config_script.py` with your specific details such as email configuration, job search criteria, and schedule timing.

### Running the Script
Run the script using:
```bash
python scraper.py
```

## Running Without Email Automation

If you prefer to manually review the scraped job listings without sending them via email, you can disable the email feature:

### Disable Email Feature
- Open `scraper.py` in a text editor.
- Find and comment out the `send_email` function call in the `save_and_send_jobs` function.

### Review the Results
- The script will save the scraped job listings in a `jobs.json` file in the project directory.
- Open `jobs.json` to review the scraped listings.

## Note
Ensure that your web scraping activities comply with the terms of service of the websites and that the use of automated scripts for job applications is in line with the ethical guidelines and legal regulations of your region.
