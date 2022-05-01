class Rating():
    def __init__(self, article_list):
        self._article_list = article_list
        self._cnt = 0
        self._length = 0
        self._percent = 0
        self._LnD = ''
    def rating(self):
        for article in self._article_list:
            if article.likes >= article.dislikes:
                self._cnt+=1
            self._length+=1
        self._percent = int(self._cnt * 100 / self._length)
        if self._percent >= 60:
            self._LnD = '호감'
        elif (self._percent < 60) and (self._percent >=40):
            self._LnD = '그저그럼'
        elif self._percent < 40:
            self._LnD = '비호감'
        return self._percent, self._LnD