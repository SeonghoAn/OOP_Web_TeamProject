from flask_testing import TestCase
from app import create_app
import unittest


class TestClientUtils(TestCase):
    def create_app(self):
        return create_app()

    def test_assert_template_used_1(self):
        self.client.get("/list/")
        self.assert_template_used('article/article_list.html')

    def test_assert_template_used_2(self):
        self.client.get("/detail/1/")
        self.assert_template_used('article/article_detail.html')

    def test_assert_template_used_3(self):
        self.client.get("/category/politics/")
        self.assert_template_used('article/article_category.html')

    def test_assert_template_used_4(self):
        self.client.get("/category/economics/")
        self.assert_template_used('article/article_category.html')

    def test_assert_template_used_5(self):
        self.client.get("/category/international/")
        self.assert_template_used('article/article_category.html')

    def test_assert_template_used_6(self):
        self.client.get("/category/social/")
        self.assert_template_used('article/article_category.html')

    def test_assert_template_used_7(self):
        self.client.get("/category/culture/")
        self.assert_template_used('article/article_category.html')

    def test_assert_template_used_8(self):
        self.client.get("/category/sports/")
        self.assert_template_used('article/article_category.html')

    def test_assert_template_used_9(self):
        self.client.get("/press/")
        self.assert_template_used('article/article_press.html')

if __name__ == '__main__':
    unittest.main()