from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)
cors=CORS(app)
model = pickle.load(open('LinearRegressionModelLaptop.pkl','rb'))
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
    os_bit=64
    graphics = sorted(laptop['graphic_card_gb'].unique())
    weight=sorted(laptop['weight'].unique())
    warranty= sorted(laptop['warranty'].unique())
    touchscreen= sorted(laptop['Touchscreen'].unique())
    msoffice= sorted(laptop['msoffice'].unique())
    ratings= sorted(laptop['Number of Ratings'].unique())
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
    'os_bits': os_bit,
    'graphics': graphics,
    'weights': weight,
    'warrantys': warranty,
    'touchscreens': touchscreen,
    'msoffices': msoffice,
    'ratings': ratings,
    'number_of_reviews': number_of_reviews
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)