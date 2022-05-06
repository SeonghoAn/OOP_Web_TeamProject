from konlpy.tag import Komoran
from collections import Counter
import re

class Keyword():
    def __init__(self, article):
        self._text = str(article.title) + ' ' + str(article.maintext)
        self._keyword = []
        self._komoran = Komoran()
        self._noun = None
        self._cnt = None

    def keyword_extract(self):
        self._text = re.sub('[&]+[a-z]+', ' ', self._text)
        self._text = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', ' ', self._text)
        self._noun = self._komoran.nouns(self._text)
        self._cnt = Counter(self._noun)
        for t, c in self._cnt.most_common():
            if len(t) >= 2 and len(self._keyword) <= 4:
                self._keyword.append(t)
            if len(self._keyword) > 4:
                break
        return self._keyword