'''
Created on 20 Feb 2018

@author: Slaporter
'''
from flask import render_template
from app import app
from systeminfo.main import get_platform_info


@app.route('/')
def index():
    returnDict = {}
    returnDict['platform']=get_platform_info()
    returnDict['title']='Home'
    return render_template("index.html",**returnDict)