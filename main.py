import save_data
import scrap_data

file_name = input('enter the file name u need to save products on it ->   ')

if __name__ == '__main__':
    scraper = scrap_data.JumiaScraper('https://www.jumia.com.eg/')
    products = scraper.scrape()
    saver = save_data.DataSaver()
    saver.save_data(products, file_name)

