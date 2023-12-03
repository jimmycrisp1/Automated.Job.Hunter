# Automated Job Hunt

This repository contains a set of scripts designed to automate the process of job hunting for Salesforce Administrator positions. It scrapes job listings from Indeed and LinkedIn, extracts relevant information, and sends the results to a specified email address daily.

## Functionality

- **Web Scraping**: Uses Selenium and BeautifulSoup to scrape job listings.
- **Email Automation**: Compiles scraped data and emails the results using SMTP.
- **Scheduling**: Runs the scraping job once per day at a specified time.
- **Configurable**: Allows for customization of job search criteria and email settings through a `.env` file.

## Installation Instructions

1. **Clone the Repository**:
   ```
   git clone https://github.com/jimmycrisp1/automated.job.hunt.git
   cd automated.job.hunt
   ```

2. **Set Up a Virtual Environment** (Optional, but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Web Driver**:
   - Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).
   - Place the WebDriver in your system's PATH or specify its path in the `.env` file.

5. **Configuration**:
   - Copy the `.env.example` file to create a new `.env` file:
     ```
     cp .env.example .env
     ```
   - Fill in the `.env` file with your email credentials, SMTP details, and the WebDriver path.

6. **Running the Script**:
   - Ensure that the `run.sh` script is executable:
     ```
     chmod +x run.sh
     ```
   - Run the script using the `run.sh` shell script:
     ```
     ./run.sh
     ```

7. **Scheduling the Script** (Optional):
   - Use a cron job or another task scheduler to run `run.sh` script at your preferred frequency.

## Usage

- Modify the search criteria and settings in the `.env` file as needed.
- The script will execute at the time specified in the `.env` file and email the job listings to the specified email address.

## Note

Ensure that your web scraping activities comply with the terms of service of the targeted websites and that the use of automated scripts for job applications is in line with the ethical guidelines and legal regulations of your region.



< Running Without Email Automation >

If you prefer to run the script without the email automation feature to manually review the scraped job listings, you can do so by following these steps:

1. **Disable Email Feature**:
   - Open the `scraper.py` file in a text editor.
   - Locate the section of the code that handles email sending (search for `send_email` function calls).
   - Comment out or remove the `send_email` function call to prevent the script from attempting to send an email.

   ```python
   # Comment out the following line or remove it
   # send_email(file_path=file_path)
   ```

2. **Output to File**:
   - Ensure that the script is set to save the scraped job listings to a file such as `jobs.json`. This is already part of the script's functionality.
   - You can find the relevant code under the function `save_jobs` or similar.

3. **Run the Script**:
   - With the virtual environment activated and dependencies installed, run the script directly using Python:
     ```
     python scraper.py
     ```
   - After the script completes its execution, you'll find the `jobs.json` file in the project directory containing the scraped job listings.

4. **Review the Results**:
   - Open the `jobs.json` file to review the job listings that have been scraped.
   - The `jobs.json` file will be structured in a readable JSON format, where each job listing is a separate entry with details such as job title, company, location, etc.

By following these steps, you can use the script to scrape job listings and save them locally without sending them via email.


---

Make sure to replace `.env.example` with the actual `.env` filename if it's different in your repository. Additionally, you can adjust any paths or commands if they differ in your environment setup.
