"""Provide the Flask App object to be used in the project"""
from os.path import abspath 
from flask import Flask
app = Flask(__name__,
            static_folder=abspath("src/webapp/views/static"), 
            template_folder=abspath("src/webapp/views"),            
)
