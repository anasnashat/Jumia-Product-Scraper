import time
from bs4 import BeautifulSoup
from selenium import webdriver



class JumiaScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.products_data = []

    def start_driver(self) -> webdriver.Chrome:
        driver = webdriver.Chrome()
        return driver

    def fetch_page(self, driver: webdriver.Chrome, page_number: int,current_url: str) -> None:
        driver.get(f'{current_url}?page={page_number}#catalog-listing')
        time.sleep(1)

    def parse_products(self, soup: BeautifulSoup) -> None:
        products = soup.find('section', class_="card -fh").find_all('article', class_="prd _fb col c-prd")
        for product in products:
            self.products_data.append(self.extract_product_data(product))

    def extract_product_data(self, product) -> dict:
        name = product.find('h3', class_='name').text.strip()
        price = product.find('div', class_='prc').text.strip()
        rating = product.find('div', class_='rev').text.strip() if product.find('div', 'rev') else "No rating"
        image_url = product.find('img')['data-src']
        product_link = f"https://www.jumia.com.eg{product.find('a', class_='core')['href']}"

        return {
            'Name': name,
            'Price': price,
            'Rating': rating,
            'Image URL': image_url,
            'Product Link': product_link
        }

    def scrape(self) -> list:
        driver = self.start_driver()
        try:
            driver.get(self.base_url)
            input('Press Enter to start scraping this page... ')
            page_number = 1
            current_url = driver.current_url
            while True:
                self.fetch_page(driver, page_number,current_url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                self.parse_products(soup)
                page_number += 1
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            driver.quit()  # Ensure driver quits regardless of success or failure
        return self.products_data


