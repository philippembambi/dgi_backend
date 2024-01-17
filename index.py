from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(
        {
            'rep':'Api connected successfully'
        })

@app.route('/loadContribution', methods=['POST'])
def retrieve():
    excelDataFile = request.form.get('excelDataFile')

    df = pd.read_excel(excelDataFile, sheet_name="Sheet1")
    dict_data = df.to_dict(orient="records")
    with open("dgi_contrib.json", "w") as infile:
        json.dump(dict_data, infile, indent=3)
        
    return jsonify(
        {
            'rep':'file loaded'
        })
    
if __name__ == '__main__':
    app.run("127.0.0.1", "5000")