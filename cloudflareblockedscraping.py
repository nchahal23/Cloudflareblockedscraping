from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# creating a chrome webdriver instance with custom options disabling some arguments preventing web scraping using cloudfare
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-browser-side-navigation')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-xss-auditor')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-features=IsolateOrigins,site-per-process')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# list to store the scraping time
scraping_times = []
# store main page content
page_content = ""

# URL of the website we want to scrape
url = 'https://www.exodus.com'
# url = 'https://tripiecointrade.com/'
# url = 'https://speedexpresstrade.com/'
# url = 'https://pfxlt.com/'

# Performing the website scraping 10 times to calculate the average scraping time (we can skip this)
for _ in range(10):
    # Recording the start time
    start_time = time.time()

    # Navigating to the web page and performing scraping actions
    driver.get(url)
    
    # Waiting for the page to load completely
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Toget the textual content of the main page
    page_content = driver.page_source

    # Recording the end time
    end_time = time.time()
    # Calculating the elapsed time for scraping
    elapsed_time = end_time - start_time
    # Adding the elapsed time to the list
    scraping_times.append(elapsed_time)

# Calculating the average scraping time
average_time = sum(scraping_times) / len(scraping_times)

# Closing the browser
driver.quit()

# Printing the average time
print(f"Average scraping time: {average_time:.2f} seconds")

# using BeautifulSoup to save the main page content in a file
soup = BeautifulSoup(page_content, 'html.parser')
text_content = soup.get_text()

# defining the file path where we want to save the content
file_path = './data/webpage_content.txt'

# saving the page content to a text file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(text_content)
