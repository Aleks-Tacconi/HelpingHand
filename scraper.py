from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import json

# Base URL of the wiki
base_url = "https://minecraft.wiki"


# Set up Selenium WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Disable sandboxing
    chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage

    # Automatically download and manage ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


# Function to scrape a single page
def scrape_page(driver, url):
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'mw-page-title-main'))
        )
    except:
        print(f"Failed to load page: {url}")
        return None

    # Extract the title of the page
    title = driver.find_element(By.CLASS_NAME, 'mw-page-title-main').text.strip()

    # Extract the main content
    content = driver.find_element(By.CLASS_NAME, 'mw-parser-output').text.strip()

    # Extract infobox data (if available)
    infobox_data = {}
    try:
        infobox = driver.find_element(By.CLASS_NAME, 'infobox')
        for row in infobox.find_elements(By.TAG_NAME, 'tr'):
            try:
                key = row.find_element(By.TAG_NAME, 'th').text.strip()
                value = row.find_element(By.TAG_NAME, 'td').text.strip()
                infobox_data[key] = value
            except:
                continue  # Skip rows without key-value pairs
    except:
        pass  # Infobox not found

    return {
        "title": title,
        "content": content,
        "infobox": infobox_data
    }


# Function to crawl a category page
def crawl_category(driver, category_url):
    driver.get(category_url)

    # Wait for the category page to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mw-category-generated"]//a'))
        )
    except:
        print(f"Subpage links did not load on {category_url}")
        return []

    # Find all links to subpages in the category using XPath
    subpage_links = driver.find_elements(By.XPATH, '//div[@class="mw-category-generated"]//a')

    if not subpage_links:
        print(f"No subpage links found on {category_url}")
        return []

    subpage_urls = [link.get_attribute('href') for link in subpage_links]

    # Scrape each subpage
    all_data = []
    for url in subpage_urls:
        print(f"Scraping: {url}")
        page_data = scrape_page(driver, url)
        if page_data:
            all_data.append(page_data)
        time.sleep(2)  # Add a delay to avoid overloading the server

    return all_data


# Save data to a CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Content", "Infobox"])
        for item in data:
            writer.writerow([item["title"], item["content"], json.dumps(item["infobox"], ensure_ascii=False)])


# Save data to a JSON file
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# Main script
if __name__ == "__main__":
    driver = setup_driver()

    categories = {
        "blocks": "https://minecraft.wiki/w/Category:Blocks",
        "items": "https://minecraft.wiki/w/Category:Items",
        "mobs": "https://minecraft.wiki/w/Category:Mobs"
    }

    for category_name, category_url in categories.items():
        print(f"Scraping category: {category_name}")
        data = crawl_category(driver, category_url)

        # Save to CSV
        save_to_csv(data, f"{category_name}_data.csv")
        print(f"Saved {len(data)} entries to {category_name}_data.csv")

        # Save to JSON
        save_to_json(data, f"{category_name}_data.json")
        print(f"Saved {len(data)} entries to {category_name}_data.json")

    driver.quit()
