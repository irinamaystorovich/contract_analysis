import os
from flask import Flask, render_template, request
#from ocr import ocr_core
from ocr import ocr_core
from pdf import *
from ocr1 import ocr_core1


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', msg='please select file')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('upload.html', msg='no file selected')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))
            #path = 'month-to-month-residential-rental-lease-agreement.pdf'
            # file='test_2.png'
            # call the OCR function on it
            extracted_text, extracted_text2, extracted_text3, extracted_text4 = ocr_core(file)
            # extract the text and display it
            return render_template('upload.html',
                                   msg='successfully processed',
                                   extracted_text=extracted_text,
                                   extracted_text2=extracted_text2,
                                   extracted_text3=extracted_text3,
                                   extracted_text4=extracted_text4,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')



if __name__ == '__main__':
    app.run()