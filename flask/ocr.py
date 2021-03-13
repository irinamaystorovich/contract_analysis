import lexnlp.extract.en.dates
import lexnlp.extract.en.entities.nltk_re
import lexnlp.extract.en.constraints
import lexnlp.extract.en.conditions
import lexnlp.extract.en.pii
import lexnlp.nlp.en.segments.sentences

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
    text_pii = list(lexnlp.extract.en.pii.get_pii(text))

    sentence_list = lexnlp.nlp.en.segments.sentences.get_sentence_list(text)
    constraints_and_conditions_dict = []
    for sentence in sentence_list:
        constraints_list = list(lexnlp.extract.en.constraints.get_constraints(sentence))
        conditions_list = list(lexnlp.extract.en.conditions.get_conditions(sentence))

        constraints_list.extend(conditions_list)
        if len(constraints_list)>0:
            constraints_and_conditions_dict = []

    return "Dates: " + str(text_dates) + "Names: " + str(text_names) + "PII: " + str(text_pii) + "Actionable Items: " + str(constraints_and_conditions_dict)

print(ocr_core('test1.png'))