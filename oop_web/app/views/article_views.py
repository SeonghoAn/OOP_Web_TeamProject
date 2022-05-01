from flask import Blueprint, render_template, request
from app.models import Article, Comment
from app import db
from app.keyword2 import Keyword
from app.comment_filter import Comments
from app.rating import Rating
import pandas as pd
from datetime import datetime

bp = Blueprint('article', __name__, url_prefix='/')

@bp.route('/list/')
def _list():
    # # 기사 데이터 db에 삽입하는 부분
    # df = pd.read_csv('C:/Users/hohoa/PycharmProjects/oop_web/MBCone.csv', encoding='utf-8')
    # for i in range(df.shape[0]):
    #     a = Article(title=str(df.loc[i]['제목']), maintext=str(df.loc[i]['기사내용']), type_of_press=str(df.loc[i]['언론사']),
    #                 type_of_event=str(df.loc[i]['카테고리']), likes=int(df.loc[i]['좋아요']), dislikes=int(df.loc[i]['싫어요']),
    #                 create_date=datetime.strptime(df.loc[i]['기사생성날짜'], '%Y-%m-%d'))
    #     db.session.add(a)
    #     if str(df.loc[i]['댓글']) != 'nan':
    #         comment = str(df.loc[i]['댓글']).split('/')
    #         com = []
    #         for i in comment:
    #             com.append(i.split(',')[0])
    #         for i in com:
    #             c = Comment(article=a, content=i, create_date=datetime.now())
    #             db.session.add(c)
    # db.session.commit()

    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    article_list = Article.query.order_by(Article.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        article_list = article_list.filter(Article.title.ilike(search) | Article.maintext.ilike(search) | Article.type_of_event.ilike(search) | Article.type_of_press.ilike(search)).distinct()
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_list.html', article_list=article_list, page=page, kw=kw)

@bp.route('/detail/<int:article_id>/')
def detail(article_id):
    article = Article.query.get_or_404(article_id)
    keyword = ", ".join(Keyword(article).keyword_extract())
    com = []
    for i in article.comment_set:
        com.append(str(i.content))
    filter_com = Comments(com).prediction()
    return render_template('article/article_detail.html', article=article, keyword=keyword, filter_com=filter_com)

@bp.route('/category/politics/')
def politics():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    url = 'article.politics'
    cate = '정치'
    category = '%%{}%%'.format(cate)
    article_list = Article.query.order_by(Article.create_date.desc()).filter(Article.type_of_event.ilike(category))
    percent, LnD = Rating(article_list).rating()
    if kw:
        search = '%%{}%%'.format(kw)
        article_list = article_list.filter(
            Article.title.ilike(search) | Article.maintext.ilike(search) | Article.type_of_press.ilike(search)).distinct()
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_category.html', article_list=article_list, page=page, kw=kw, cate=cate,url=url, percent=percent, LnD=LnD)

@bp.route('/category/economics/')
def economics():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    url = 'article.economics'
    cate = '경제'
    category = '%%{}%%'.format(cate)
    article_list = Article.query.order_by(Article.create_date.desc()).filter(Article.type_of_event.ilike(category))
    percent, LnD = Rating(article_list).rating()
    if kw:
        search = '%%{}%%'.format(kw)
        article_list = article_list.filter(
            Article.title.ilike(search) | Article.maintext.ilike(search) | Article.type_of_press.ilike(search)).distinct()
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_category.html', article_list=article_list, page=page, kw=kw, cate=cate,url=url, percent=percent, LnD=LnD)

@bp.route('/category/international/')
def international():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    url = 'article.international'
    cate = '국제'
    category = '%%{}%%'.format(cate)
    article_list = Article.query.order_by(Article.create_date.desc()).filter(Article.type_of_event.ilike(category))
    percent, LnD = Rating(article_list).rating()
    if kw:
        search = '%%{}%%'.format(kw)
        article_list = article_list.filter(
            Article.title.ilike(search) | Article.maintext.ilike(search) | Article.type_of_press.ilike(search)).distinct()
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_category.html', article_list=article_list, page=page, kw=kw, cate=cate,url=url, percent=percent, LnD=LnD)

@bp.route('/category/social/')
def social():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    url = 'article.social'
    cate = '사회'
    category = '%%{}%%'.format(cate)
    article_list = Article.query.order_by(Article.create_date.desc()).filter(Article.type_of_event.ilike(category))
    percent, LnD = Rating(article_list).rating()
    if kw:
        search = '%%{}%%'.format(kw)
        article_list = article_list.filter(
            Article.title.ilike(search) | Article.maintext.ilike(search) | Article.type_of_press.ilike(search)).distinct()
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_category.html', article_list=article_list, page=page, kw=kw, cate=cate,url=url, percent=percent, LnD=LnD)

@bp.route('/category/culture/')
def culture():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    url = 'article.culture'
    cate = '문화'
    category = '%%{}%%'.format(cate)
    article_list = Article.query.order_by(Article.create_date.desc()).filter(Article.type_of_event.ilike(category))
    percent, LnD = Rating(article_list).rating()
    if kw:
        search = '%%{}%%'.format(kw)
        article_list = article_list.filter(
            Article.title.ilike(search) | Article.maintext.ilike(search) | Article.type_of_press.ilike(search)).distinct()
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_category.html', article_list=article_list, page=page, kw=kw, cate=cate,url=url, percent=percent, LnD=LnD)

@bp.route('/category/sports/')
def sports():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    url = 'article.sports'
    cate = '스포츠'
    category = '%%{}%%'.format(cate)
    article_list = Article.query.order_by(Article.create_date.desc()).filter(Article.type_of_event.ilike(category))
    percent, LnD = Rating(article_list).rating()
    if kw:
        search = '%%{}%%'.format(kw)
        article_list = article_list.filter(
            Article.title.ilike(search) | Article.maintext.ilike(search) | Article.type_of_press.ilike(search)).distinct()
    article_list = article_list.paginate(page, per_page=10)
    return render_template('article/article_category.html', article_list=article_list, page=page, kw=kw, cate=cate,url=url, percent=percent, LnD=LnD)

@bp.route('/press/')
def press():
    article_list = Article.query.order_by(Article.create_date.desc())
    press_list = ['한국일보', '중앙일보', 'MBC', '동아일보']
    dic = {}
    for press in press_list:
        press_type = '%%{}%%'.format(press)
        percent, LnD = Rating(article_list.filter(Article.type_of_press.ilike(press_type))).rating()
        dic[press] = [percent, LnD]
    return render_template('article/article_press.html',dic=dic)