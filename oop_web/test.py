from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models import Article, Comment
from app.keyword2 import Keyword
from app.rating import Rating
from app.comment_filter import Comments
import unittest

class UnitTestCase(unittest.TestCase):
    def setUp(self) -> None:
        Base = declarative_base()

        engine = create_engine("sqlite:///test.db", echo=False)

        Base.metadata.bind = engine

        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.article_list = self.session.query(Article).all()
        self.article = self.session.query(Article).get(1)
        self.com = []
        for i in self.article.comment_set:
            self.com.append(str(i.content))

    def tearDown(self) -> None:
        self.session.close()

    def test_runs(self):
        Rating(self.article_list).rating()
        Keyword(self.article).keyword_extract()
        Comments(self.com).prediction()

    def test_correct_value(self):
        per, lnd = Rating(self.article_list).rating()
        key = ", ".join(Keyword(self.article).keyword_extract())
        filter = Comments(self.com).prediction()
        self.assertEqual(per, 50)
        self.assertEqual(lnd, '그저그럼')
        self.assertEqual(key, '국민, 본회의, 의원, 국회, 통과')
        self.assertEqual(filter[0], '필터링된 댓글입니다.')



if __name__ == '__main__':
    unittest.main()