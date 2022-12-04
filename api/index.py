from flask import Flask
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
html = urlopen(baseUrl)
soup = BeautifulSoup(html.read(), 'lxml')
eczaneListesi = soup.find_all('li', class_='media')

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'