# Jumia Product Scraper

## Description
A web scraper for extracting product data from Jumia's Egyptian site using Selenium and BeautifulSoup. It gathers product names, prices, ratings, images, and links, saving the results to a user-defined Excel file. The modular design allows for easy maintenance and future enhancements.

## Features
- Scrapes product details from Jumia.
- Supports pagination to gather data from multiple pages.
- Saves extracted data in an Excel file.
- Modular design with separate classes for scraping and data saving.

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup
- Pandas
- ChromeDriver (ensure it matches your installed Chrome version)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anasnashat/jumia-product-scraper.git
   cd jumia-product-scraper
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```

2. Enter your desired filename when prompted.

3. Access the saved Excel file in the `ScrapedData` directory.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues or pull requests for improvements!


Feel free to modify the content to better suit your project!
