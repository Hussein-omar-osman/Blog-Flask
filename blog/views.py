from flask import Flask, render_template, url_for, flash, redirect, request
from blog import app

@app.route('/')
def home():
 return render_template('home.html', title='Home')