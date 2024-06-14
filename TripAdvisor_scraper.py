"""
    This function finds the urls of all the restaurants in Thessaloniki.
    It receives a soup object and a list with the already collected urls.
    It returns a list with all the urls.
"""
def restaurants_urls(soup, urls_list):
    titles_restaurants = soup.find_all("div", class_="RfBGI")
    for title in titles_restaurants:
        title_url = 'https://www.tripadvisor.com' + title.a.get('href')
        urls_list.append(title_url)

    return urls_list


"""
    This function finds the url of the next page of a current page.
    It receives a soup object and the name of the class of the next page button.
    It returns the url of the next page.
"""
def next_page(soup, class_name):
    page = soup.find("a", class_=class_name)
    href = page.get('href')
    url = 'https://www.tripadvisor.com' + href

    return url


"""
    This function finds the name of the restaurant.
    It receives a soup object and returns the restaurant's name.
"""
def restaurant_name(soup):
    return soup.find("h1", class_="HjBfq").text


"""
    This function finds the usernames of all the reviewers in a page.
    It receives a soup object and returns the reviewer's username
"""
def username(soup):
    usernames = []
    usernames_list = soup.find_all("div", class_="info_text pointer_cursor")
    for name in usernames_list:
        usernames.append(name.text)

    return usernames


"""
    This function finds the dates of review of all the reviews in a page.
    It receives a soup object and returns the reviews' date
"""
def review_date(soup):
    review_dates = []
    dates_list = soup.find_all("span", class_="ratingDate")
    for date in dates_list:
        review_dates.append(date.get('title'))

    return review_dates


"""
    This function finds the dates of visit of all the reviews in a page.
    It receives a soup object and returns the visits date
"""
def visit_date(soup):
    visit_dates = []
    dates_list = soup.find_all("div", class_="prw_rup prw_reviews_stay_date_hsx")
    for date in dates_list:
        full_text = date.text
        split_word = ': '
        date = full_text.split(split_word)[1]
        visit_dates.append(date)

    return visit_dates


"""
    This function finds the title of all the reviews in a page.
    It receives a soup object and returns the titles.
"""
def title(soup):
    titles = []
    titles_list = soup.find_all("span", class_="noQuotes")
    for t in titles_list:
        titles.append(t.text)

    return titles


"""
    This function finds the text that appears immediately in all the reviews in a page.
    It receives a soup object and returns the texts.
"""
def partial_text(soup):
    texts = []
    texts_list = soup.find_all("p", class_="partial_entry")
    for text in texts_list:
        text = text.text
        split_word = '...'
        text = text.split(split_word)[0]
        texts.append(text)

    return texts


"""
    This function finds the text that appears inside the more button in all the reviews in a page.
    It receives a soup object and returns the texts.
"""
def more_text(soup):
    mores = []
    mores_list = soup.find_all("span", class_="postSnippet")
    for more in mores_list:
        mores.append(more.text)

    return mores


"""
    This function finds the rating of all the reviews in a page.
    It receives a soup object and returns the ratings.
"""
def rating(soup):
    ratings = []
    ratings_soup_list = soup.find_all("div", class_="ui_column is-9")
    for rating_soup in ratings_soup_list:
        rating = rating_soup.find("span", class_="ui_bubble_rating")
        if rating.get('class')[1] == "bubble_10":
            ratings.append(1.0)
        elif rating.get('class')[1] == "bubble_15":
            ratings.append(1.5)
        elif rating.get('class')[1] == "bubble_20":
            ratings.append(2.0)
        elif rating.get('class')[1] == "bubble_25":
            ratings.append(2.5)
        elif rating.get('class')[1] == "bubble_30":
            ratings.append(3.0)
        elif rating.get('class')[1] == "bubble_35":
            ratings.append(3.5)
        elif rating.get('class')[1] == "bubble_40":
            ratings.append(4.0)
        elif rating.get('class')[1] == "bubble_45":
            ratings.append(4.5)
        elif rating.get('class')[1] == "bubble_50":
            ratings.append(5.0)
        else:
            ratings.append(0.0)

    return ratings
