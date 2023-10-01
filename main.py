from flask import Flask,request
from isbntools.app import *
import json
from flask_cors import CORS
app = Flask(__name__)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
CORS(app,origins='*') 


@app.route('/upload', methods=['POST'])
def getBookDetails():
        json=request.get_json()
        barcodes = json['barcode']
        for barcode in barcodes:
                metadata = meta(barcode)
                author_name = metadata['Authors']
                book_name = metadata['Title']
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
                credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                client = gspread.authorize(credentials)
                # Open the Google Sheets document
                sheet = client.open_by_key('18R1iIEU8BoeWYREOvl879jcQriH8zHFLt9P6FbJ4Sks').sheet1
                # Convert the values to strings explicitly
                barcode_str = str(barcode)
                book_name_str = str(book_name)
                author_name_str = str(author_name)

                # Append the row to the sheet
                sheet.append_row([barcode_str, book_name_str, author_name_str])
        return [author_name,book_name]
    

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
