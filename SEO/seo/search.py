
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def setup_driver():
    options = uc.ChromeOptions()
    # ❗ Turn off headless mode during testing
    # options.add_argument('--headless')  # Disable for now
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('user-agent=Mozilla/5.0')
    return uc.Chrome(options=options)

def scrape_google(query):
    print(f"Searching for: {query}")
    driver = setup_driver()
    data = []
    seen = set()
    
    try:
        driver.get(f"https://www.google.com/search?q={query}")
        time.sleep(7)  # Wait more to load full content
        
        # Scroll down to load more results
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = soup.select("div.tF2Cxc")

        for idx, result in enumerate(results):
            title_tag = result.find("h3")
            link_tag = result.find("a")
            
            if title_tag and link_tag:
                name = title_tag.get_text(strip=True)
                url = link_tag.get("href")

                if name not in seen:
                    seen.add(name)
                    data.append({
                        "Ranking": idx + 1,
                        "Name": name,
                        "Site": url
                    })
    finally:
        try:
            driver.quit()
        except:
            pass  # Safely suppress the WinError 6

    return data

def save_to_csv(data):
    df = pd.DataFrame(data)
    filepath = os.path.abspath("search.csv")
    df.to_csv(filepath, index=False)
    print(f"🔍 Total results scraped: {len(data)}")
    print(f"✅ Scraping completed. Saved to: {filepath}")

def main():
    query = "Top IT companies in Ghaziabad site=justdial.com"
    results = scrape_google(query)
    save_to_csv(results)

if __name__ == "__main__":
    main()
