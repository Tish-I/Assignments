import requests


# Function to print data types for a given anime
def print_anime_data_types(anime_id):
    url = f'https://api.jikan.moe/v4/anime/{anime_id}'
    response = requests.get(url)
    anime_data = response.json()

    # Print the available data and their types
    print("Available Data Types for Anime:")
    for key, value in anime_data['data'].items():
        print(f"{key}: {type(value).__name__}")


# Example usage
print_anime_data_types(1)  # Replace 1 with any anime ID you are interested in
