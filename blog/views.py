from flask import Flask, render_template, url_for, flash, redirect, request
from blog import app
from blog.forms import LoginForm, RegistrationForm
@app.route('/')
def home():
 return render_template('home.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
 form = RegistrationForm()
 return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
 form = LoginForm()
 return render_template('login.html', title='Login', form=form)