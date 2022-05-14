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
 if form.validate_on_submit():
  if form.email.data == 'ali@gmail.com' and form.password.data == '123':
   flash('login successful', 'secondary')
   return redirect(url_for('home'))
  else:
   flash('login unsuccessful', 'danger')
 return render_template('login.html', title='Login', form=form)