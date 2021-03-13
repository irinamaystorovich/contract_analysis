import lexnlp.extract.en.dates
import lexnlp.extract.en.entities.nltk_re
import lexnlp.extract.en.durations
import lexnlp.extract.en.dates
import lexnlp.extract.en.entities.nltk_re
import lexnlp.extract.en.constraints
import lexnlp.extract.en.conditions
import lexnlp.extract.en.pii
import lexnlp.nlp.en.segments.sentences

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
    return (string[0 + i:length + i] for i in range(0, len(string), length))


def get_summarization(text):
    # api-endpoint
    URL = "https://api.meaningcloud.com/summarization-1.0"
    # location given here

    sentences = '5'
    key = '025a2c5b45b844ee075667a525abf1a2'
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'txt': text, 'sentences': sentences, 'key': key}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    # extracting data in json format
    data = r.json()
    # print(type(data))
    '''print(data)
    print(data['summary'])'''
    # sleep to not exceed rate limit of api
    time.sleep(3)
    return data['summary']


def get_pdf_summarization(pdf_path):
    output_string = StringIO()
    # path needs to correct path in folder to file location
    with open(pdf_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    pdf_text = output_string.getvalue()
    # print(pdf_text)

    pdf_chunked = list(chunkstring(pdf_text, 6000))
    # create summary list to add summarized chunks too
    summary = []

    # print(type(pdf_text))
    # count = 0
    for line in pdf_chunked:
        output = get_summarization(line)
    summary.append(output)
    separator = ' '
    summary = separator.join(summary)
    return summary
    # print(count)


#should be in local file storage where app is run
path = 'month-to-month-residential-rental-lease-agreement.pdf'

pdfsummary = get_pdf_summarization(path)



try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
    text = pytesseract.image_to_string(Image.open(filename))
    text_names=list(lexnlp.extract.en.entities.nltk_re.get_companies(text))

    text_pii = list(lexnlp.extract.en.pii.get_pii(text))

    sentence_list = lexnlp.nlp.en.segments.sentences.get_sentence_list(text)
    constraints_and_conditions_dict = {}

    for sentence in sentence_list:
        constraints_list = list(lexnlp.extract.en.constraints.get_constraints(sentence))
        conditions_list = list(lexnlp.extract.en.conditions.get_conditions(sentence))

        constraints_list.extend(conditions_list)
        if len(constraints_list) > 0:
            constraints_and_conditions_dict[sentence] = constraints_list

    #pii_text=str(text_pii) + "Actionable Items: " + str(constraints_and_conditions_dict)

    pii_text = ''
    if len(text_pii) > 0:
        pii_text = pii_text + 'PII: ' + ' '.join([str(elem) for elem in text_pii])
    if len(constraints_and_conditions_dict.keys()):
        pii_text = pii_text + '\n 3: Action Items: ' + ' '.join(
            [str(elem) for elem in constraints_and_conditions_dict.keys()])

    text_dates = list(lexnlp.extract.en.dates.get_dates(text))
    #
    # duration = (list(lexnlp.extract.en.durations.get_durations(text)))
    #
    # set_duration = next(iter(duration))
    #
    # def convert(set):
    #     return list(set)
    #
    # dates = convert(set_duration)
    # print("The contract duration is " + str(dates[1]) + " " + dates[0] + 's' + " (" + str(dates[2]) + " days)")


    listToStr = ' '.join([str(elem) for elem in text_names])

    extract_text=  "1. Agreement's Entities: " + str(listToStr)
    extract_text2 = "2. Effective Dates: " + str(text_dates[0])

    extract_text3 = str(pii_text)
    extract_text4 = "4. Agreement's Summarization: " + str(pdfsummary)
    # extract_text4 = "2. The agreement start date is " + str(text_dates[0]) + '. The end date is ' + str(text_dates[1]) + '.'"The contract duration is " + str(dates[1]) + " " + dates[0] + 's' + " (" + str(dates[2]) + " days)"



    return  extract_text, extract_text2, extract_text3, extract_text4

#print(ocr_core('test1.png'))