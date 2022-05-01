from konlpy.tag import Komoran
from collections import Counter
import re

class Keyword():
    def __init__(self, article):
        self._text = str(article.title) + ' ' + str(article.maintext)
        self._keyword = []

    def keyword_extract(self):
        self._text = re.sub('[&]+[a-z]+', ' ', self._text)
        self._text = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', ' ', self._text)
        komoran = Komoran()
        noun = komoran.nouns(self._text)
        cnt = Counter(noun)
        for t, c in cnt.most_common():
            if len(t) >= 2 and len(self._keyword) <= 4:
                self._keyword.append(t)
            if len(self._keyword) > 4:
                break
        return self._keyword