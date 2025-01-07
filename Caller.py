import NHKNews
from NHKNews import main_titles, main_links

def call(news):
    titles,links = NHKNews.main(news)
    return titles,links

