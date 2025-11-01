from flask import Flask, render_template, request, redirect
import pandas as pd
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)
cors=CORS(app)
model = pickle.load(open('LinearRegressionModelLaptop.pkl', 'rb'))
laptop = pd.read_csv('cleaned_laptops.csv')

@app.route("/")
def index():
    brand = sorted(laptop['brand'].unique())
    processor_brand = sorted(laptop['processor_brand'].unique())
    processor_name = sorted(laptop['processor_name'].unique())
    processor_gen = sorted(laptop['processor_gnrtn'].unique())
    ram_gb = sorted(laptop['ram_gb'].unique())
    ram_type = sorted(laptop['ram_type'].unique())
    hdd = sorted(laptop['hdd'].unique())
    ssd = sorted(laptop['ssd'].unique())
    os = sorted(laptop['os'].unique())
    graphics = sorted(laptop['graphic_card_gb'].unique())
    weight=sorted(laptop['weight'].unique())
    warranty= sorted(laptop['warranty'].unique())
    touchscreen= sorted(laptop['Touchscreen'].unique())
    msoffice= sorted(laptop['msoffice'].unique())
    ratings= sorted(laptop['rating'].unique())
    number_of_ratings= sorted(laptop['Number of Ratings'].unique())
    number_of_reviews= sorted(laptop['Number of Reviews'].unique())

    context = {
    'brands': brand,
    'processor_brands': processor_brand,
    'processor_names': processor_name,
    'processor_gens': processor_gen,
    'ram_gbs': ram_gb,
    'ram_types': ram_type,
    'hdds': hdd,
    'ssds': ssd,
    'oss': os,
    'graphics': graphics,
    'weights': weight,
    'warrantys': warranty,
    'touchscreens': touchscreen,
    'msoffices': msoffice,
    'rating': ratings,
    'number_of_ratings': number_of_ratings,
    'number_of_reviews': number_of_reviews
    }

    return render_template('index.html', **context)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form or query parameters (works for both GET and POST)
    brand = request.values.get('brand')
    processor_brand = request.values.get('processor_brand')
    processor_name = request.values.get('processor_name')
    processor_gen = request.values.get('processor_gen')
    ram_gb = request.values.get('ram_gb')
    ram_type = request.values.get('ram_type')
    hdd = request.values.get('hdd')
    ssd = request.values.get('ssd')
    graphics = request.values.get('graphics')
    weight = request.values.get('weight')
    warranty = request.values.get('warranty')
    touchscreen = request.values.get('touchscreen')
    os=request.values.get('os')
    msoffice = request.values.get('msoffice')
    ratings = request.values.get('ratings')
    number_of_ratings = request.values.get('number_of_ratings')
    number_of_reviews = request.values.get('number_of_reviews')

    # Create a DataFrame for model prediction

    input_data = pd.DataFrame([{
        'brand': brand,
        'processor_brand': processor_brand,
        'processor_name': processor_name,
        'processor_gnrtn': processor_gen,
        'ram_gb': ram_gb,
        'ram_type': ram_type,
        'ssd': ssd,
        'hdd': hdd,
        'os': os,
        'graphic_card_gb': graphics,
        'weight': weight,
        'warranty': warranty,
        'Touchscreen': touchscreen,
        'msoffice': msoffice,
        'rating': ratings,
        'Number of Ratings': number_of_ratings,
        'Number of Reviews': number_of_reviews,
    }])
    # Get prediction from model
    prediction = model.predict(input_data)[0]
    print(prediction)
    return f"<div class='result-box'>💻 Estimated Price: <b>{prediction}</b> ₹</div>"

    # Return as JSON
if __name__ == '__main__':
    app.run(debug=True)


