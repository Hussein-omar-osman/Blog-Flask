from flask import Flask, render_template, url_for, flash, redirect, request
from blog import app

@app.route('/')
def home():
 return render_template('home.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
 return render_template('register.html', title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
 return render_template('login.html', title='Login')