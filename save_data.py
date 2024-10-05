import os
import pandas as pd


class DataSaver:
    def __init__(self, directory: str = 'ScrapedData'):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def get_file_path(self, file_name: str) -> str:
        return os.path.join(self.directory, f'{file_name}.xlsx')

    def load_existing_data(self, file_path: str) -> pd.DataFrame:
        if os.path.exists(file_path):
            return pd.read_excel(file_path)
        return pd.DataFrame()

    def save_data(self, products_data: list, file_name: str) -> None:
        if not products_data:
            print("No data to save.")
            return

        file_path = self.get_file_path(file_name)
        new_data_df = pd.DataFrame(products_data)

        existing_data_df = self.load_existing_data(file_path)
        combined_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)

        try:
            combined_df.to_excel(file_path, index=False)
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")


# Example usage
if __name__ == "__main__":
    products_data = [
        {'Name': 'Product1', 'Price': '10$', 'Rating': '5 stars', 'Image URL': 'http://example.com/image1.jpg',
         'Product Link': 'http://example.com/product1'}]
    saver = DataSaver()
    saver.save_data(products_data, 'products')
