# Selenium related librares
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome related libraries
from webdriver_manager.chrome import ChromeDriverManager

# Other libraries
import os
import time
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Path to google chrome account
google_path = os.getenv("GOOGLE_PATH")

# URL to the page
imported_url = os.getenv("URL")

# Word to search inside the page
imported_word = os.getenv("WORD")


# Main function
def main():
    pickup_locations = ["Parque Arauco"]
    dropoff_locations = ["Metro Tobalaba"]
    results = scrape_prices(pickup_locations, dropoff_locations)
    save_to_csv(results)


def setup_webdriver():
    # Setupt options
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={google_path}")

    # Maintain updated chrome driver
    service = Service(ChromeDriverManager().install())

    return webdriver.Chrome(service=service, options=options)


def enter_locations(driver, pickup, dropoff):

    # Get the inputs and send the pickup locations
    time.sleep(1)
    pickup_input = driver.find_elements(By.TAG_NAME, "input")
    pickup_input[0].send_keys(" ")
    pickup_input = driver.find_elements(By.TAG_NAME, "input")
    pickup_input[0].send_keys(pickup)
    time.sleep(1)
    pickup_input = driver.find_elements(By.TAG_NAME, "input")
    pickup_input[0].send_keys(Keys.ENTER)
    time.sleep(1)

    # Enter the inputs and send the dropoff locations
    dropoff_input = driver.find_elements(By.TAG_NAME, "input")
    dropoff_input[1].send_keys({dropoff})
    time.sleep(1)
    dropoff_input = driver.find_elements(By.TAG_NAME, "input")
    dropoff_input[1].send_keys(Keys.ENTER)
    time.sleep(1)


def click_search_button(driver):

    # Find and click the search button
    search_button = driver.find_elements(By.TAG_NAME, "button")
    time.sleep(1)
    search_button[4].click()
    time.sleep(1)


def extract_prices(driver):

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Get the paragraphs to extract the information
    paragraphs = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'div[data-baseweb="block"] p')
        )
    )
    product, price = None, None

    # Iterate over the paragraphs to get the product and price
    for index, p in enumerate(paragraphs):
        if imported_word in p.text:
            product = p.text
            price = paragraphs[index + 3].text.split()[0]
            break

    return product, price


def scrape_prices(pickup_locations, dropoff_locations):

    # Initialize the row to store information
    rows = []

    # Use the functions to scrape the information
    for pickup, dropoff in zip(pickup_locations, dropoff_locations):
        driver = setup_webdriver()
        driver.get(imported_url)
        enter_locations(driver, pickup, dropoff)
        click_search_button(driver)
        product, price = extract_prices(driver)

        # Get actual date and hour
        date = datetime.now().strftime("%m/%d/%Y")
        hour = datetime.now().strftime("%H:%M")

        # Append the information to the rows
        rows.append(
            {
                "Pickup": pickup,
                "Dropoff": dropoff,
                "Price": price,
                "Product": product,
                "Date": date,
                "Hour": hour,
            }
        )
        driver.quit()
    return rows


def save_to_csv(data, filename="results.csv"):

    # Save the information to a csv file
    df = pd.DataFrame(data)
    if not os.path.exists(filename):
        df.to_csv("results.csv", index=False)
    else:
        df.to_csv(filename, mode="a", header=False, index=False)


if __name__ == "__main__":
    main()
