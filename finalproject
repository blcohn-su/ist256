import requests
import json

zipcode = input("Enter your zip code: ")
url = f'https://api.documenu.com/v2/restaurants/zip_code/{zipcode}/?key=1a3d001e5f3faa286dc984c148d33771'

param = {"fullmenu" : True}
response = requests.get(url, params = param)

page_results = [response.json()]
initial_query = response.json()
total_restaurants = initial_query['totalResults']
total_pages = initial_query['total_pages']

for page in range(2, total_pages + 1):
    param = {"page" : page, "fullmenu" : True}
    response = requests.get(url, params = param)
    page_results.append(response.json()) 

from IPython.display import display, HTML 

search_term = input("Enter the menu item you would like to search for: ")
search_term = search_term.lower()

for page in page_results:
    for restaurant in page['data']:
        rest_info_printed = False
        for menu in restaurant['menus']:
            for section in menu['menu_sections']:
                for item in section['menu_items']:
                    successful_search = False
                    for word in item['name'].lower().split():
                        if word.startswith(search_term) or word.endswith(search_term): 
                            successful_search = True
                    for word in item['description'].lower().split():
                        if word.startswith(search_term) or word.endswith(search_term): 
                            successful_search = True
                    if successful_search:
                        if not rest_info_printed:
                            if restaurant['restaurant_website']:
                                display(HTML(f"<a href=\"{restaurant['restaurant_website']}\"><h2>{restaurant['restaurant_name']}</h2>{restaurant['restaurant_website']}</a>"))
                            else: 
                                display(HTML(f"<h2>{restaurant['restaurant_name']}</h2>"))
                            display(HTML(f"<em>{restaurant['restaurant_phone']}</em>"))
                            display(HTML(f"<em>{restaurant['address']['formatted']}</em>"))
                            display(HTML('<h3>Item(s) Found:</h3>'))
                            rest_info_printed = True
                        item_found = f"<strong>{item['name']}</strong>"
                        if item['description']:
                            item_found += f" -- {item['description']}"
                        display(HTML(item_found))
        if rest_info_printed: print()
