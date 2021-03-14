from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import json
import requests
import time

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def get_summarization(text):
    # api-endpoint 
    URL = "https://api.meaningcloud.com/summarization-1.0"    
    # location given here 
    
    sentences = '5'
    key = '025a2c5b45b844ee075667a525abf1a2'    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'txt':text,'sentences':sentences, 'key':key}     
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS)     
    # extracting data in json format 
    data = r.json()
    #print(type(data))
    '''print(data)
    print(data['summary'])'''
    #sleep to not exceed rate limit of api
    time.sleep(3)
    return data['summary']


def get_pdf_summarization(pdf_path):
    output_string = StringIO()
#path needs to correct path in folder to file location
    with open(pdf_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    pdf_text = output_string.getvalue()
    #print(pdf_text)

    pdf_chunked = list(chunkstring(pdf_text, 6000))
    #create summary list to add summarized chunks too
    summary =[]

    #print(type(pdf_text))
    #count = 0
    for line in pdf_chunked:
        output = get_summarization(line)
    summary.append(output)
    separator = ' '
    summary = separator.join(summary)
    return summary
    #print(count)

'''#should be in local file storage where app is run
''path = 'EmmisCommunicationsCorp_20191125_8-K_EX-10.6_11906433_EX-10.6_Marketing Agreement.pdf'

pdfsummary = get_pdf_summarization(path)
print(pdfsummary)
'''''
