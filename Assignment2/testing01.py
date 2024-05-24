import requests
from pprint import pprint

# Ask the user if they would like to search anime by genre
search_by_genre = input("Would you like to search Anime by Genre? (yes/no): ").strip().lower()

if search_by_genre == 'yes':
    # Get the list of genres
    url = 'https://api.jikan.moe/v4/genres/anime'
    response = requests.get(url)
    genres_data = response.json()
    genres = genres_data['data']

    # List the genres and their IDs
    print("Available Genres:")
    for genre in genres:
        print(f"{genre['mal_id']}: {genre['name']}")

    # Prompt user to input a genre ID
    genre_id = input("Please enter the ID of the genre you are interested in: ").strip()

    # Validate the input genre ID
    if any(genre['mal_id'] == int(genre_id) for genre in genres):
        # Use the genre ID to get anime of that genre
        genre_anime_url = f'https://api.jikan.moe/v4/anime?genres={genre_id}'
        genre_response = requests.get(genre_anime_url)
        anime_list = genre_response.json()

        # Display the anime list
        if 'data' in anime_list and anime_list['data']:
            pprint(anime_list['data'])
        else:
            print("No anime found for the selected genre.")
    else:
        print("Invalid genre ID.")
else:
    # If the user does not want to search by genre
    anime_name = input("Input an Anime name: ").strip()
    search_url = f'https://api.jikan.moe/v4/anime?q={anime_name}'

    # Get the list of anime by name
    response = requests.get(search_url)
    anime_list = response.json()

    # Display the anime list
    if 'data' in anime_list and anime_list['data']:
        pprint(anime_list['data'])
    else:
        print("No anime found with the given name.")