# Configuration for Web Scraping Script

# Browser Driver Path
BROWSER_DRIVER_PATH = '/path/to/driver'

# Email Configuration
EMAIL_SENDER = 'sender@example.com'
EMAIL_RECEIVER = 'receiver@example.com'
EMAIL_PASSWORD = 'password123'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Job Search Criteria
JOB_TITLES = [
    'Salesforce Administrator',
    'Salesforce Admin',
    'Junior Salesforce Administrator',
    'Junior Salesforce Admin'
]
JOB_LOCATION = 'Remote'
KEYWORDS = ['Salesforce', 'Admin', 'Junior', 'Jr', 'Entry']

# Schedule Timing
SCHEDULE_TIME = '10:00 AM'

# Website-Specific Scraping Instructions
WEBSITE_INSTRUCTIONS = {
    'Indeed': {
        'search_element': 'div',
        'class_name': 'jobsearch-SerpJobCard'
    },
    'LinkedIn': {
        'search_element': 'li',
        'class_name': 'listed-job-posting'
    }
}

# Proxy/VPN Details
PROXY_SERVER = 'proxy.example.com'
PROXY_PORT = 8080
PROXY_USERNAME = 'proxyuser'
PROXY_PASSWORD = 'proxypass'
