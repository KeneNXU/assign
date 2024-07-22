# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
import os
import sys
import dateutil.parser
import babel
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_wtf import FlaskForm
import logging
from flask_pymongo import PyMongo
from logging import Formatter, FileHandler
from datetime import datetime
# from forms import ArtistForm, ShowForm, VenueForm
# from models import app, db, City, Show, Venue, Artist
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
app = Flask(__name__)
app.secret_key = os.urandom(32)
mongo_pwd = os.environ.get('MONGO_PWD')
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
app.config["MONGO_URI"] = f"mongodb+srv://kgobianagha:{mongo_pwd}@cluster0.s0vyuej.mongodb.net/mydatabase?retryWrites=true&w=majority&appName=Cluster0"
# app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

# Initialize PyMongo
mongo = PyMongo(app)


@app.route('/add', methods=['POST'])
def add_user_data():
    data = request.get_json()
    if data is not None:
        try:
            user_id = mongo.db.users.insert_one(data).inserted_id
            return jsonify({"message": "User data added", "user_id": str(user_id)}), 201
        except:
            flash('An error occurred. Data could not be listed')
            print(sys.exc_info())

    return {}


@app.route('/')
def index():
    return render_template('pages/home.html')


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
