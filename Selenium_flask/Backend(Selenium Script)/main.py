
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    return driver

def search_google_maps(driver, query):
    driver.get("https://www.google.com/maps")
    time.sleep(5)
    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(10)

def scroll_results(driver, scrolls=30):
    for _ in range(scrolls):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

def extract_listing_data(driver, listings):
    data = []
    for listing in listings[:50]:  # Limit to first 50 results
        try:
            listing.click()
            time.sleep(5)
            name = driver.find_element(By.CSS_SELECTOR, 'h1.DUwDvf').text
            address = driver.find_element(By.CSS_SELECTOR, 'div.Io6YTe span').text

            phone = "N/A"
            details = driver.find_elements(By.CSS_SELECTOR, 'div.Io6YTe')
            for d in details:
                if "+" in d.text:
                    phone = d.text
                    break

            data.append([name, phone, address])
            print(f"Collected: {name}")
        except:
            continue
    return data

def save_to_csv(data, filename):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Company Name", "Phone Number", "Address"])
        writer.writerows(data)

def scrape_it_companies(output_csv="it_companies_noida.csv", scrolls=15):
    driver = setup_driver()
    try:
        search_google_maps(driver, "IT companies in Noida")
        scroll_results(driver, scrolls)
        listings = driver.find_elements(By.CSS_SELECTOR, 'div.Nv2PK')
        data = extract_listing_data(driver, listings[:100])
    finally:
        driver.quit()

    save_to_csv(data, output_csv)
    return output_csv, data