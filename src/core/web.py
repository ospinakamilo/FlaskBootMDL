"""Provides the Flask App object to be used in the project"""
from os.path import abspath 
from flask import Flask, Blueprint
app = Flask(__name__,
            static_folder=abspath("src/webapp/views/static"), 
            template_folder=abspath("src/webapp/views"),            
)

vendor_blueprint = Blueprint('vendor', __name__, static_url_path='/static/vendor', static_folder=abspath("src/core/html/vendor"))
app.register_blueprint(vendor_blueprint)
