from flask import Flask,request
from flask_cors import CORS
from isbntools.app import *
app= Flask(__name__)

CORS(app,origins='*') 
import gspread
from oauth2client.service_account import ServiceAccountCredentials







@app.route('/upload', methods=['POST'])
def getBookDetails():
    print("im here")
    author_name=''
    book_name=''
    publisher=''
    year=''    
    json=request.get_json()
    barcodes = json['barcode']
    for barcode in barcodes:
        if(len(barcode) == 13):
            metadata = meta(barcode)
            string=''
            for idx, author in enumerate(metadata['Authors']):
                if idx == len(metadata['Authors']) - 1:
                    string += author
                else:
                    string += author + ','
            author_name=string
            print('author',author_name)
            book_name = metadata['Title']
            publisher = metadata['Publisher']
            year = metadata['Year']
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
            credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
            client = gspread.authorize(credentials)
            sheet = client.open_by_key('18R1iIEU8BoeWYREOvl879jcQriH8zHFLt9P6FbJ4Sks').sheet1
        
            barcode_str = str(barcode)
            book_name_str = str(book_name)
            author_name_str = str(author_name)
            publisher_str = str(publisher)
            year_str = str(year)

            # Append the row to the sheet
            sheet.append_row([barcode_str, book_name_str, author_name_str, publisher_str,year_str])
    return [author_name,book_name]

        
      
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=80)






