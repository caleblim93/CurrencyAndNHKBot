import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from seleniumbase import Driver

url = 'https://www3.nhk.or.jp/news/'
domain = 'https://www3.nhk.or.jp'
# Initialize translator
translator = Translator()
main_titles = []
main_links = []
top_featured = []
top_links = []
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'


def main(news):
    # header variable
    headers = {'User-Agent': user_agent}
    driver = Driver(uc=True, headless=True)
    driver.get(url)
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.sleep(3)
    #response = requests.get(url, headers)
    #soup = BeautifulSoup(response.content, 'html.parser')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #translated = translator.translate(f'{main_header[0].find("em").text}', src="ja", dest="en")
    #print(f'Translated Title: {translated.text}')

    if news.lower() == 'main':
        main_news(soup)
        # Get secondary news and extend links
        secondary_titles, secondary_links = secondary_news(soup)
        main_titles.extend(secondary_titles)
        main_links.extend(secondary_links)

        # Get tertiary news and extend links
        tertiary_titles, tertiary_links = tertiary_news(soup)
        main_titles.extend(tertiary_titles)
        main_links.extend(tertiary_links)
        return main_titles,main_links
    elif news.lower() == 'featured':
        # Get featured news and extend links
        featured_titles, featured_links = featured_news(soup)
        top_featured.extend(featured_titles)
        top_links.extend(featured_links)
        return top_featured,top_links
    elif news.lower() == 'society':
        #Get society news
        return society_news(soup)
    elif news.lower() == 'disaster':
        #Get disaster news
        return disaster_news(soup)
    elif news.lower() == 'politics':
        #Get political news
        return political_news(soup)
    elif news.lower() == 'business':
        #Get business news
        return business_news(soup)
    elif news.lower() == 'international':
        #Get international news
        return international_news(soup)
    elif news.lower() == 'science':
        #Get science news
        return science_culture_news(soup)
    elif news.lower() == 'sports':
        #Get sports news
        return sports_news(soup)
    elif news.lower() == 'life':
        #Get life news
        return medic_life_news(soup)

def main_news(soup):
    main_header = soup.find_all('h1', {'class': 'content--header-title'})
    main_title = f'{main_header[0].find("em").text}'
    main_link = f'{domain}{main_header[0].find("a").get("href")}'
    main_titles.append(main_title)
    main_links.append(main_link)

def secondary_news(soup):
    sub_headers = soup.find_all('ul', {'class': 'content--list grid--col -column2-md'})
    titles = []
    links = []
    for sub_header in sub_headers:
        listings = sub_header.find_all('li')
        for item in listings:
            title = item.find('em', {'class':'title'}).text
            link = f'{domain}{item.find("a").get("href")}'
            titles.append(title)
            links.append(link)
    return titles,links

def tertiary_news(soup):
    sub_headers = soup.find_all('ul', {'class': 'content--list grid--col -column4-md -column2-sm'})
    titles = []
    links = []
    for sub_header in sub_headers:
        listings = sub_header.find_all('li')
        for item in listings:
            title = item.find('em', {'class': 'title'}).text
            link = f'{domain}{item.find("a").get("href")}'
            titles.append(title)
            links.append(link)
    return titles,links

def featured_news(soup):
    featured = soup.find_all('div',id='featured-contents-tabpanel-001')
    featured_titles = []
    featured_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            featured_titles.append(title)
            featured_links.append(link)
    return featured_titles,featured_links

def society_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-002')
    society_titles = []
    society_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            society_titles.append(title)
            society_links.append(link)
    return society_titles, society_links

def disaster_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-003')
    disaster_titles = []
    disaster_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            disaster_titles.append(title)
            disaster_links.append(link)
    return disaster_titles, disaster_links

def political_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-004')
    politic_titles = []
    politic_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            politic_titles.append(title)
            politic_links.append(link)
    return politic_titles, politic_links

def business_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-005')
    business_titles = []
    business_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            business_titles.append(title)
            business_links.append(link)
    return business_titles, business_links

def international_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-006')
    international_titles = []
    international_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            international_titles.append(title)
            international_links.append(link)
    return international_titles, international_links

def science_culture_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-007')
    snc_titles = []
    snc_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            snc_titles.append(title)
            snc_links.append(link)
    return snc_titles, snc_links

def sports_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-008')
    sports_titles = []
    sports_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            sports_titles.append(title)
            sports_links.append(link)
    return sports_titles, sports_links

def medic_life_news(soup):
    featured = soup.find_all('div', id='featured-contents-tabpanel-009')
    medic_life_titles = []
    medic_life_links = []
    for items in featured:
        listings = items.find_all('li')
        for listing in listings:
            title = listing.find('em', {'class': 'title'}).text
            link = f'{listing.find("a").get("href")}'
            medic_life_titles.append(title)
            medic_life_links.append(link)
    return medic_life_titles, medic_life_links
