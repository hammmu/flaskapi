from flask import Flask,request
from isbntools.app import *
import json
from flask_cors import CORS
app = Flask(__name__)

CORS(app,origins='*') 


def get_book_metadata(isbn):
    metadata = meta(isbn)
    print(metadata)
    return metadata['Title']


@app.route('/getBookData',methods=['POST'])
def hello():
    print('i am called')
    barcodes=request.get_json()
    print(barcodes)
    temp=[]
    for value in barcodes['barcodes']:
        temp.append(get_book_metadata(str(value)))
    return temp

@app.route('/')
def home():
	html = """
<html>
 <head>
  <title>
   Google Cloud Run - Sample Python Flask Example
  </title>
 </head>
 <body>
  <p>Hello Hyder</p>
 </body>
</html>
"""
	return html
    
if __name__ == '__main__':
    app.run(debug=True)



# # Access data
# data = sheet.get_all_records()
# print(data)
