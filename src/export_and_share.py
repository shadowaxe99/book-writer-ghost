```python
import os
from fpdf import FPDF
from epublib import EpubBook
from pymongo import MongoClient

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.get_database('autobiographyDB')
narratives = db.get_collection('narratives')

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Autobiography', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def print_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

def export_to_pdf(narrative_id):
    narrative = narratives.find_one({"_id": narrative_id})
    pdf = PDF()
    for chapter in narrative['chapters']:
        pdf.print_chapter(chapter['title'], chapter['body'])
    pdf.output('autobiography.pdf', 'F')

def export_to_epub(narrative_id):
    narrative = narratives.find_one({"_id": narrative_id})
    book = EpubBook()
    book.set_identifier(narrative_id)
    book.set_title('Autobiography')
    book.set_language('en')
    for chapter in narrative['chapters']:
        book.add_item(EpubHtml(title=chapter['title'], file_name=f'{chapter["title"]}.xhtml', content=chapter['body']))
    book.create_epub('autobiography.epub')

def export_to_print(narrative_id):
    # This function would integrate with a third-party print-on-demand service API
    # to send the generated autobiography for printing and delivery to the user.
    pass
```