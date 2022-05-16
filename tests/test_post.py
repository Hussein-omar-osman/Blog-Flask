import unittest
from blog.models import Post
from blog import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_post = Post(description = 'content')
        db.session.add(self.new_post)
        db.session.commit()
        
    def tearDown(self):
        Post.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.description, 'content')

    def tearDown(self):
        Post.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.description, 'content')