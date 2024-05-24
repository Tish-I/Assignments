import requests

# Ask the user their name
def name_prompt():
    app_user = input("Please enter your name: ").title()
    return app_user


# Welcome message
def welcome_message(app_user):
    welcome = f"Hello {app_user}, welcome to Kawaii_Haven. Your one stop shop for all things Anime and Manga."
    return welcome


# Welcome the user with welcome message
def welcome_user():
    app_user = name_prompt()
    print(welcome_message(app_user))


# Calling the Api for Anime
def query_anime(url):
    response = requests.get(url)
    if response.status_code == 200:
        
        return response

def filtering_anime():
   query_anime('https://api.jikan.moe/v4/genres/anime')





#         data = response.json()
#          = data.get('data')



#
#     if response.status_code == 200:
#         data = response.json()
#         recipes = data.get('hits')
#         if recipes:
#             return recipes
#         else:
#             print('No recipes found for chosen ingredient.')
#             return []
#
#     else:
#         print(f'Error occurred during API request. Status code: {response.status_code}')
#         return []

# Calling the Api for Manga


welcome_user()

