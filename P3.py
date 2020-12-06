#!/usr/bin/env python
# coding: utf-8

# # IST256 Project Deliverable 3 (P3)
# 
# ## Phase 3: Implementation (26 of 52 points)
# 
# **IMPORTANT:** PLEASE READ THIS ENTIRE NOTEBOOK BEFORE STARTING YOUR WORK!
# 
# It time to turn in the the finished product, 3 Steps:
# 
# 1. Restate your idea
# 2. Place all your project code in cells below, and make sure it runs correctly. 
# 3. Your Comments
# 
# Don't forget to record in your journal each time you work on the project.
# 

# ### Step 1: What is Your Idea, Again?
# 
# Remind us of your project again!
# 
# `--== Double-click and put the title or brief description of your project below  ==--`
# 
# 

# ### Step 2: Project Code
# 
# Include all project code below. Make sure to execute your code to ensure it runs properly before you turn it in. We will be grading this code based on the following criteria:
# 
# - Is there clear code evidence which helps your evaluator determine how you got from original idea to the final implementation?
# - It is expected that your code will execute as intended as solve the problem as stated.
# - It is expected your code will be well written in a modular fashion, use aptly named objects, user defined functions for modularity (breaking up the code into smaller parts), and handle user errors  / bad input as appropriate.
# - The programming style and idioms will match those you were taught in class. We should not see code outside of the style learned in IST256.
# - Does the code clearly demonstrate what you have learned in the course and that you are capable of acquiring new programming skills and techniques independently ?
# - Does your journal adequately reflect upon the work you’ve done?
# - Will your code execute for the evaluator? Does it have everything they need in this notebook? HINT: Go to the control panel, click **Stop My Server**, then start your notebook back up and run your P3 code again to make sure it works in a clean notebook.
# - Exceptional projects are awareded the highest number of points. Exceptional projects go above and beyond the expectations and normally incorporate several project references into the project.
# 
# Multiple cells are provided for your code below. Add more as appropriate.
# 

# In[1]:


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


# In[2]:


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


# In[ ]:





# ### Step 3: Your Comments
# 
# Any last words or comments about your code submission? Add anything here you feel will be helpful for us to make a proper evaluation of your code project submission. This should include, but not be limited to, any changes you made to your project between P2 and P3 which we would be unaware of and the reasons those changes we made.
# 
# `--== Double-click and place your comments below  ==--`
# 
# 
# 
# 

# In[ ]:


# SAVE YOUR WORK FIRST! CTRL+S
# RUN THIS CODE CELL TO TURN IN YOUR WORK!
from ist256.submission import Submission
Submission().submit()

