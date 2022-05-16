from flask import render_template, url_for, flash, redirect, request, abort
from blog import app, db, bc
from blog.forms import LoginForm, RegistrationForm, UpdateProfileForm, BlogForm, CommentForm
from blog.models import User, Post, Comments
from flask_login import login_user, current_user, logout_user, login_required
import requests
from blog.utility_func import save_profile_pic, save_blog_pic


@app.route('/')
def home():
 res = requests.get(f'http://quotes.stormconsultancy.co.uk/random.json').json()
 most_like = Post.query.order_by(Post.likes.desc()).all()
 latest = Post.query.order_by(Post.date_posted.desc()).all()
 latest_post = []
 liked_post = []
 for i in range(0, len(most_like)):
   if i == 3:
     break
   else:
     liked_post.append(most_like[i])
     
 for i in range(0, len(latest)):
   if i == 6:
     break
   else:
     latest_post.append(latest[i])
 return render_template('home.html', title='Home', res=res, liked_post=liked_post, latest_post=latest_post)

@app.route("/register", methods=['GET', 'POST'])
def register():
 if current_user.is_authenticated:
   return redirect(url_for('home'))
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
 if current_user.is_authenticated:
   return redirect(url_for('home'))
 form = LoginForm()
 
 if form.validate_on_submit():
  user = User.query.filter_by(email=form.email.data).first()
  if user and bc.check_password_hash(user.password, form.password.data):
      login_user(user)
      flash(f'{user.username}, You have been logged in!', 'secondary')
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home'))
  else:
      flash('Login Unsuccessful. Please check email and password', 'danger')
 return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('You have successfully logged out', 'secondary')
    return redirect(url_for('home'))
  
  
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
  profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
  posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.date_posted.desc()).all()
  return render_template('account.html', title='Account', profile_image=profile_image, posts=posts)

@app.route("/update_profile", methods=['GET', 'POST'])
@login_required
def update_profile():
  form = UpdateProfileForm()
  if form.validate_on_submit():
    print(form.username.data, form.email.data, form.bio.data)
    if form.profile_pic.data:
      print(form.profile_pic.data)
      p_name = save_profile_pic(form.profile_pic.data)
      current_user.profile_image = p_name
    current_user.username = form.username.data
    current_user.email = form.email.data
    current_user.description = form.bio.data
    db.session.commit()
    flash('Your account has been updated', 'secondary')
    return redirect(url_for('account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
    form.bio.data = current_user.description
    
  return render_template('update_profile.html', title='Update Profile', form=form)


@app.route("/blogs", methods=['GET', 'POST'])
def blogs():
  posts = Post.query.order_by(Post.date_posted.desc()).all() 
  return render_template('blogs.html', title='Blogs', posts=posts)


@app.route("/create_pitch", methods=['GET', 'POST'])
@login_required
def create_blog():
  form = BlogForm()
  if form.validate_on_submit():
    if form.blog_pic.data:
      print(form.blog_pic.data)
      p_name = save_blog_pic(form.blog_pic.data)
      post = Post(title=form.title.data, content=form.content.data, author=current_user, blog_image=p_name)
    else:
      post = Post(title=form.title.data, content=form.content.data, author=current_user)
    db.session.add(post)
    db.session.commit()
      
    flash('You have posted', 'secondary')
    return redirect(url_for('blogs'))
    
  return render_template('create_blog.html', title='Create Blog', form=form, leg='Create A Blog Post')

@app.route("/post/<post_id>" , methods=['GET', 'POST'])
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comments.query.order_by(Comments.date_posted.desc()).filter_by(post_id=post_id)
    form = CommentForm()
    total_comments = len(post.comments)
    if form.validate_on_submit():
      comment = Comments(content=form.content.data, user_comments=current_user, post_id=post_id)
      db.session.add(comment)
      db.session.commit()
      flash('You have commented', 'secondary')
      return redirect(url_for('post', post_id=post_id))
    return render_template('post.html', post=post, form=form, comments=comments, total_comments=total_comments, title='Post')
  
  

@app.route("/post/<post_id>/update" , methods=['GET', 'POST'])
@login_required
def update_post(post_id):
  post = Post.query.get_or_404(post_id)
  if post.author != current_user:
    abort(403)

  form = BlogForm()
  if form.validate_on_submit():
    post.title = form.title.data
    post.content = form.content.data
    if form.blog_pic.data:
      p_name = save_blog_pic(form.blog_pic.data)
      post.blog_image = p_name
    db.session.commit()
    flash('Your Blog Post Has Been Updated', 'secondary')
    return redirect(url_for('post', post_id=post.id))
  elif request.method == "GET":
    form.title.data = post.title
    form.content.data = post.content
  return render_template('create_blog.html', title='Update Blog', form=form, leg='Update Blog Post')
