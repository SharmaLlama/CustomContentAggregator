import requests


def articles_requester(category, pageSize):
    headers = {'Authorization': '853520a6146b476aa5a9d574a98a83f7'}
    everything_news_url = 'https://newsapi.org/v2/top-headlines'

    everything_payload = {'category': category, 'country': 'au', 'pageSize': pageSize}
    articles = requests.get(url=everything_news_url, headers=headers, params=everything_payload)
    print(articles.json())
    articledataframe = get_articles(articles.json()['articles'])

    return articledataframe


def get_articles(file):
    article_results = []

    for i in range(len(file)):
        article_dict = {'title': "".join(str(file[i]['title']).split("-")[0:-1]).strip(),
                        'author': file[i]['author'],
                        'source': file[i]['source'],
                        'description': file[i]['description'],
                        'content': file[i]['content'],
                        'pub_date': file[i]['publishedAt'],
                        'url': file[i]['url'],
                        'photo_url': file[i]['urlToImage']
                        }

        article_results.append(article_dict)

    return article_results


if __name__ == "__main__":
    df1 = articles_requester('business', 3)
    df2 = articles_requester('sports', 3)
    print(df1)
    print(df2)
