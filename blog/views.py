from flask import render_template, url_for, flash, redirect, request
from blog import app, db, bc
from blog.forms import LoginForm, RegistrationForm
from blog.models import User, Post, Comments

@app.route('/')
def home():
 return render_template('home.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
 form = RegistrationForm()
 if form.validate_on_submit():
    hashed_password = bc.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash(f'Account created for {form.username.data}! You can Log in any time', 'secondary')
    return redirect(url_for('login'))
 return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
 form = LoginForm()
 if form.validate_on_submit():
  print(form.email.data)
  user = User.query.filter_by(email=form.email.data).first()
  if user and bc.check_password_hash(user.password, form.password.data):
      flash(f'{user.username}, You have been logged in!', 'primary')
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home'))
  else:
      flash('Login Unsuccessful. Please check email and password', 'danger')
 return render_template('login.html', title='Login', form=form)