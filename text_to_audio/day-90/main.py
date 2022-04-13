from dotenv import load_dotenv 
import os
import PyPDF2 
import requests
import sys 


load_dotenv()
API_KEY = os.getenv('API_KEY')

URL = 'https://api.voicerss.org/?'

class AudioBook:
    """Returns audio from PDF file"""

    def __init__(self, file, page) -> None:
        """initializes the class and returns the script"""
        self.file = file
        self.file_name = os.path.basename(self.file)
        self.page = page

        # conversion process
        self.grab_pdf()
        self.get_page()
        self.write_mp3_file()


    def grab_pdf(self):
        """Grabs Pdf file and returns pdf object"""

        self.pdf_file = open(self.file, 'rb')
        self.pdf_reader = PyPDF2.PdfFileReader(self.pdf_file)


    def get_page(self):
        """ Gets page and extracts text"""

        self.page = self.pdf_reader.getPage(self.page)
        self.text = self.page.extractText()
        self.text = "+".join(self.text.split())

    def write_mp3_file(self):
        """Function calls api and saves mp3 file of pdf file script"""

        r = requests.get(f'{URL}key={API_KEY}&hl=en-us&src={self.text}')
        with open(f'./day-90/{self.file_name}.mp3', 'wb') as f:
            f.write(r.content)

        # close file 
        self.pdf_file.close()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        audio_book = AudioBook(file=sys.argv[1], page=int(sys.argv[2]))
    else:  
        audio_book = AudioBook(file='./day-90/vm.pdf', page=1)






