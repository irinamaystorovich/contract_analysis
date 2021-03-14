FROM python:3.6-buster

EXPOSE 5000

#ENV VAR1=10

# make a directory for application
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy source code
COPY /flask .

# run application
CMD [ "python", "app.py" ]