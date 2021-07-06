# encoding: utf-8
from flask import render_template


class FeatureImageFunctions():

    def config():
        return render_template('config.html')
    
    
    def save_config():
        pass