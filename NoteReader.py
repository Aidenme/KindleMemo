from bs4 import BeautifulSoup
class NoteReader:
    DEFAULT_IMPORT = 'Input/'
    def __init__(self, fileName, importFolder=DEFAULT_IMPORT):
        self.fileName = fileName
        self.IMPORT_FOLDER = importFolder

    def getSoup(self, fileName=None, importFolder=None):
        target_file = fileName or self.fileName
        target_folder = importFolder or self.IMPORT_FOLDER