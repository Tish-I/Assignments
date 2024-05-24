import requests
from pprint import pprint

# Search anime by name

# Ask the user if they would like to search anime by genre
search_by_genre = input("Would you like to search Anime by Genre? (yes/no): ").strip().lower()

# If Yes, get a list of genres
if search_by_genre == 'yes':
    url = 'https://api.jikan.moe/v4/genres/anime'
    response = requests.get(url)
    genres_data = response.json()
    genres = genres_data['data']

    genres.sort(key=lambda x: x['mal_id'])

    print("Available Genres:")
    for genre in genres:
        print(f"{genre['mal_id']}: {genre['name']}")

    # Get the genre code from the user
    genre_code = input("Enter the Genre Code from the list above: ").strip()

    # Fetch the list of anime for the selected genre
    genre_anime_url = f'https://api.jikan.moe/v4/anime?genres={genre_code}'
    genre_response = requests.get(genre_anime_url)
    genre_anime_data = genre_response.json()
    anime_list = genre_anime_data['data']

    # Display the list of anime
    print(f"Anime in Genre Code {genre_code}:")
    for anime in anime_list:
        print(f"""
        Title: {anime['title_english']}
        Id: {anime['mal_id']}
        Score: {anime['score'] if anime['score'] is not None else 'N/A'}
            """)

else:
    print("Okay, you chose not to search by genre.")
