from sklearn.feature_extraction.text import CountVectorizer
import joblib
import pandas as pd

class Comments():

    def __init__(self, comment):
        self._comment = list(comment)
        self._cv = CountVectorizer()
        self._data1 = pd.read_csv('C:/Users/hohoa/PycharmProjects/oop_web/newtrain.csv', encoding='cp949')
        self._model = joblib.load('C:/Users/hohoa/PycharmProjects/oop_web/naive.pkl')
        self._filtered = []
        self._tf = None
        self._result = None
    def prediction(self):
        self._cv.fit(self._data1['comments'])
        self._tf = self._cv.transform(self._comment)
        self._result = self._model.predict(self._tf)
        for i in range(len(self._result)):
            if self._result[i]==0:
                self._filtered.append('필터링된 댓글입니다.')
            elif self._result[i]==1:
                self._filtered.append(self._comment[i])
        return self._filtered