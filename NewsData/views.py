import datetime
from django.shortcuts import render
from .webScraper import articles_requester
from .models import NewsData


# Create your views here.


def home_view(request, *args, **kwargs):
    NewsData.objects.filter(date=datetime.date.today()).filter(category='home').delete()

    df1 = articles_requester('sports', 3)
    df2 = articles_requester('business', 3)
    df3 = articles_requester('science', 3)
    df4 = articles_requester('technology', 3)
    df5 = articles_requester('general', 3)
    viewer = df1 + df2 + df3 + df4 + df5
    for article in viewer:
        NewsData.objects.create(url=article['url'], title=article['title'], author=article['author'],
                                description=article['description'], content=article['content'], pub_date=
                                article['pub_date'], urlImage=article['photo_url'], category='home',
                                date=datetime.date.today())

    return render(request, "home.html", {'articles': viewer})


def _view(category):
    # checker = NewsData.objects.filter(date=datetime.date.today()).filter(category=category).first()
    # if not checker:
    #     df1 = articles_requester('general', 25)
    #     for article in df1:
    #         NewsData.objects.create(url=article['url'], title=article['title'], author=article['author'],
    #                                 description=article['description'], content=article['content'], pub_date=
    #                                 article['pub_date'], urlImage=article['photo_url'], category=category,
    #                                 date=datetime.date.today())
    #
    # else:
    #     df1 = NewsData.objects.filter(date=datetime.date.today()).filter(category=category).values()

    NewsData.objects.filter(date=datetime.date.today()).filter(category=category).delete()
    df1 = articles_requester(category, 25)
    for article in df1:
        NewsData.objects.create(url=article['url'], title=article['title'], author=article['author'],
                                description=article['description'], content=article['content'], pub_date=
                                article['pub_date'], urlImage=article['photo_url'], category=category,
                                date=datetime.date.today())

    return df1


def general_view(request, *args, **kwargs):
    return render(request, "general.html", {'articles': _view('general')})


def business_view(request, *args, **kwargs):
    return render(request, "business.html", {'articles': _view('business')})


def sports_view(request, *args, **kwargs):
    return render(request, "sports.html", {'articles': _view('sports')})


def technology_view(request, *args, **kwargs):
    return render(request, "technology.html", {'articles': _view('technology')})


def science_view(request, *args, **kwargs):
    return render(request, "science.html", {'articles': _view('science')})
