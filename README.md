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

---

Make sure to replace `.env.example` with the actual `.env` filename if it's different in your repository. Additionally, you can adjust any paths or commands if they differ in your environment setup.
