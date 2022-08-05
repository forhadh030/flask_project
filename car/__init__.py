from flask import Flask, render_template
from .car_model import cars
from config import Config

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cars/<int:car_number>')
def car_list(car_number):
    return render_template('car_listing.html', cars_id = cars[car_number])