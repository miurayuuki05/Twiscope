import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

user_email = os.getenv("EMAIL")
user_handle = os.getenv("HANDLE")
password = os.getenv("PWD")

# Initialize data list
data = []

def fkTwitter():
    try :
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")

        # Use undetected_chromedriver for stealth mode
        driver = uc.Chrome(options=options)  # Ensure compatibility with your Chrome version

        # Open Twitter login page
        driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        # Enter username/email
        email_input = driver.find_element(By.CSS_SELECTOR, "[autocomplete='username']")
        email_input.send_keys(user_email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(5)

        # Check if username or phone number is required
        try:
            user_handle_input = driver.find_element(By.CSS_SELECTOR, "[autocomplete='on']")
            user_handle_input.send_keys(user_handle)
            user_handle_input.send_keys(Keys.RETURN)
            time.sleep(5)
        except:
            pass

        # Enter password
        password_input = driver.find_element(By.CSS_SELECTOR, "[autocomplete='current-password']")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)

        # Navigate to search page
        driver.get("https://twitter.com/search?q=kebijakan%20pemerintah&src=typeahead_click&f=live")
        time.sleep(5)

        i = 0

        # Scroll and collect tweets
        while i < 30:
            tweets = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
            for tweet in tweets:
                data.append(tweet.text)

            old_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(10) 
            new_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
            i += 1
            with open("tweetsref2.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            if new_scroll_height == old_scroll_height:
                break

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if driver:
            driver.quit()


fkTwitter()
