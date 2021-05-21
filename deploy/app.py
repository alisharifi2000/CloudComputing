import pandas as pd
from flask import Flask, jsonify, request,render_template
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    req = request.get_json()
    input_data = req['data']
    input_data_df = pd.DataFrame.from_dict(input_data)

    model = joblib.load('model.pkl')
	
    prediction = model.predict(input_data_df)

    if prediction[0] == 1.0:
        cancer_type = 'Malignant'
    else:
        cancer_type = 'Benign'

    return jsonify({'output':{'cancer_type':cancer_type}})
        

@app.route('/')
def home():
    return render_template('index.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', port='80')