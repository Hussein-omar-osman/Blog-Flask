import secrets
import os
from blog import app
from PIL import Image


 
def save_profile_pic(form_pic):
    random_hex = secrets.token_hex(8)
    fn, f_ext = os.path.splitext(form_pic.filename)
    pic_name = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static/profile_pics', pic_name)
    
    desired_img_size = (130, 130)
    i = Image.open(form_pic)
    i.thumbnail(desired_img_size)
    i.save(pic_path)
    
    return pic_name
   
   
def save_blog_pic(form_pic):
    random_hex = secrets.token_hex(8)
    fn, f_ext = os.path.splitext(form_pic.filename)
    pic_name = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static/blog_images', pic_name)
    
    desired_img_size = (700, 700)
    i = Image.open(form_pic)
    i.thumbnail(desired_img_size)
    i.save(pic_path)
    
    return pic_name