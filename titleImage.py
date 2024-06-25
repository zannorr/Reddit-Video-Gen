from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
# Replace with the URL of the Reddit post you want to capture
def capture_title_image(reddit_url):
    # Replace with your desired user agent
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument('--force-dark-mode')

    # Set up the Chrome driver
    chrome_service = ChromeService()  # Update with the path to your chromedriver

    # Initialize the Chrome browser
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Open the Reddit post
    browser.get(reddit_url)

    # Locate the element with ID that starts with a specific string
    element_start = 't3_'  # Replace with the starting string of the ID
    wait = WebDriverWait(browser, 20)  # Adjust the timeout as needed
    post_element = wait.until(
        EC.presence_of_element_located((By.XPATH, f"//*[starts-with(@id, '{element_start}')]"))
    )

    # Creates a directory for the title image if it doesnt exist
    if not os.path.exists('titleImage'):
        os.makedirs('titleImage')

    # Capture a screenshot of the located element
    screenshot_path = 'titleImage//reddit_post_screenshot.png'
    post_element.screenshot(screenshot_path)

    # Close the browser
    browser.quit()

    print(f"Screenshot saved to {screenshot_path}")
    return screenshot_path
