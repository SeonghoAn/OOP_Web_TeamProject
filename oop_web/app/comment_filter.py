
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import pandas as pd

class Comments():

    def __init__(self, comment):
         self.comment = list(comment)

    def prediction(self):
        cv = CountVectorizer()
        data1 = pd.read_csv('C:/Users/hohoa/PycharmProjects/oop_web/newtrain.csv', encoding='cp949')
        cv.fit(data1['comments'])
        model = joblib.load('C:/Users/hohoa/PycharmProjects/oop_web/naive.pkl')
        tf = cv.transform(self.comment)
        result = model.predict(tf)
        filtered = []
        for i in range(len(result)):
            if result[i]==0:
                filtered.append('필터링된 댓글입니다.')
            elif result[i]==1:
                filtered.append(self.comment[i])
        return filtered