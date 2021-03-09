# ocr-using-python-flask-heroku
Optical Character Recognition wep app using pytesseract and flask.

[pytesseract](https://pypi.org/project/pytesseract/)
## To run

1. Clone this Project
2. Run this command in project directory: python -m venv env
3. In linux source env/bin/activate or In windows .\env\Scripts\activate
4. Run this:pip install -r requirements.txt
5. Run this command:python app.py

## To Deploy on heroku
1. Run this cmd: heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
2. heroku config:set TESSDATA_PREFIX=./.apt/usr/share/tesseract-ocr/4.00/tessdata
3. Then Deploy

* Deployed link--> [Ghost](https://ghost-ocr-text.herokuapp.com/)

## gHost ;)
