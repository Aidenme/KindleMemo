from bs4 import BeautifulSoup
from pathlib import Path

class HTMLReader:
    def __init__(self, import_folder='Input/'):
        self.import_folder = Path(import_folder)
        
    def get_soup(self, file_name):
        
        path_name = self.import_folder / file_name

        with open(path_name, 'r', encoding='utf-8') as html_file:
            return BeautifulSoup(html_file, 'lxml')