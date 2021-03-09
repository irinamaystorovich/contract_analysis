import lexnlp.extract.en.dates
import lexnlp.extract.en.entities.nltk_re
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
    text_dates=list(lexnlp.extract.en.dates.get_dates(text))
    text_names=list(lexnlp.extract.en.entities.nltk_re.get_companies(text))
    return "Dates: " + str(text_dates) + "Names: " + str(text_names)

print(ocr_core('test1.png'))