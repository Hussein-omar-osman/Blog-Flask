import unittest
from blog.models import Comments
from blog import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comments(description = 'content')
        db.session.add(self.new_comment)
        db.session.commit()
        
    def tearDown(self):
        Comments.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.description, 'content')

    def tearDown(self):
        Comments.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.description, 'content')