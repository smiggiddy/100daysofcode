from bs4 import BeautifulSoup
import csv 
import requests 

URL = 'https://fitmencook.com/recipes/'

def get_recipe_data(url):
    """returns soup for different recipes"""
    header_html = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
    "Accept-Language": 'en-US,en;q=0.5'
    }

    r = requests.get(url=url, headers=header_html)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    recipe_list = soup.find_all(name='h3', class_='fit-post-title')

    return recipe_list

def titles_links(soup):
    """Extract titles and URLS from scraping"""
    recipes = []

    for recipe in soup: 
        title = recipe.get_text()
        link = recipe.a['href']

        recipes.append({'name': title, 'url': link}) 

    return recipes


if __name__ == "__main__":
    recipe_list = get_recipe_data(URL)
    data = titles_links(recipe_list)

    titles = ['name', 'url']
    with open('./day-92/data.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=titles)
        writer.writeheader()
        writer.writerows(data)