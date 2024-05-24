import requests
from pprint import pprint


# Welcoming the user
def welcome_user():
    app_user = input("Please enter your name: ").title()
    welcome_message = f"Hello {app_user}, welcome to Kawaii_Haven. Your one stop shop for all things Anime and Manga."

    return welcome_message


print(welcome_user())

# Ask the user if they would like to search anime by genre
def search_by_genre

search_by_genre = input("Would You like to search Anime by Genre? (yes/no): ").strip().lower()

# If Yes get a list of genres
if search_by_genre() == 'yes':
    url = 'https://api.jikan.moe/v4/genres/anime'
    response = requests.get(url)
    genres_data = response.json()
    genres = genres_data['data']

    print("Available genres:")
    for genre in genres:
        print(f"{genre['mal_id']}: {genre['name']}")


# If No


# Filtering anime


# Filtering Manga
