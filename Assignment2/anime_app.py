# The 'csv' module is used for reading and writing comma, separated, values.
# Writing - allows you to write data to it, from lists or dictionaries.
# Reading - allows you to access the csv files as well as convert the rows,
# to python lists or dictionaries
import csv

# This is used for making HTTP requests, like sending requests and handling responses.
# Sending requests - it simplifies HTTP/1.1 by using (GET, POST, PUT, DELETE),
# to interact with web services and APIs.
# Handling responses - It allows the user access to response content, headers
# and status codes
import requests

# This module allows us to format and wrap plain text.
# Wrapping Text - wraps text into a specified width for easier readability
# Indenting Text - allows us to add indentation to each line of text.
import textwrap

# This is a data manipulation and analysis library in python.
# It provides data structures like DataFrames for handling structured data.
# Data Manipulation - reads data from various file formats like CSV's
#                   - manipulates data using; filtering, grouping and merging
# Data Analysis - provides functions and methods used for data analysis and visualisation.
import pandas as pd

# The 'datetime' module provides classes for working with dates and times,
# in a simple way.
# Date and Time Manipulation - allows you to create, change and format dates and times.
import datetime

# This module is used to import the path functionality from the library
# It is used to check if the file exits
from os import path


# Ask the user their name using an input prompt.
# .title() titles the first character in the users name
# This then gets stored in the variable 'app_user'
# 'app_user' can now be used throughout the app
def name_prompt():
    app_user = input("Please enter your name: ").title()
    return app_user


# This function calls the 'name_prompt' to get the users name in title case
# then stores it in the variable 'app_user'
# # 'app_user' can now be used throughout the app
# This function also welcomes the user using the 'app_user' variable to make
# the welcome message be personalised
# It then takes the user into the 'kawaii_haven_nav(app_user)' part of the app
def welcome_user():
    app_user = name_prompt()
    print(f"Hello {app_user}, welcome to Kawaii_Haven. Your one stop shop for all things Anime.")
    kawaii_haven_nav(app_user)


# This function defines 'yes' and 'no' input from the user and can be used throughout the code.
# It takes in the argument 'prompt message', which is a message displayed to the user.
# The user's input is collected 'input(prompt_message)'.
# Its then stripped of leading or trailing whitespaces, and converted to lowercase
# A 'while' loop checks if the input is not 'yes' or 'no'
# If the input is invalid, it prints and error message and prompts the user again.
def prompt_yes_or_no_user_input(prompt_message):
    yes_or_no_user_input = input(prompt_message).strip().lower()
    while yes_or_no_user_input != "yes" and yes_or_no_user_input != "no":
        print("Invalid response, please type yes or no")
        yes_or_no_user_input = input(prompt_message).strip().lower()
    return yes_or_no_user_input


# The 'kawaii_haven_nav' guides the user through the app options based on their input.
# The function takes in 'app_user', which is the user's name
# The function then enters a loop where it repeatedly asks the user to choose an option,
# or 'exit' to quit.
# Depending on the user's input it will switch them to a different section of the app
def kawaii_haven_nav(app_user):
    nav_search_dict = {
        1: 'Search by Anime',
        2: 'Access your Watch-list'
    }
    navigation_choice = None
    while navigation_choice != 'exit':
        print(
            "\nPlease select the number that represents the navigation field "
            "you would like to use to peruse from the following list;")
        for key, value in nav_search_dict.items():
            print(f'{key}: {value}')
        navigation_choice = input("Type the number related to your choice here [type 'exit' to quit]: ")
        if navigation_choice == '1':
            print("\nSwitching you to the Anime side of Kawaii_Haven")
            anime_filtering(app_user)
        elif navigation_choice == '2':
            # Accessing this choice during the initial run-through of the app will
            # tell the user that their watch list is currently empty.
            print("\nTrying to retrieve your Watch-list!")
            anime_csv_options(app_user)
        elif navigation_choice == 'exit':
            print(f"\nGoodbye {app_user}, and thank you for visiting Kawaii_Haven!")
        else:
            print("Invalid option. Please choose either '1' or '2' ")


# This function formats and displays a watchlist as a table.
# It takes 'watch_list' which is a 'csv' and converts into a Pandas Dataframe
# It the converts the DataFrame into a Markdown table with the 'to_markdown' method
# 'index=False' - This removes the Dataframe index from the table, doing this can make the
# table cleaner.
# As well as more focused on the actual data in the Dataframe and not on the numerical
# index column that Pandas adds.
# 'tablefmt="grid"' - Formats the table with grid lines
# 'colalign=("center", "center", "center", "center")' - Centers the text in all columns
def display_watch_list(watch_list):
    df = pd.DataFrame(watch_list)
    watch_list_table = df.to_markdown(index=False, tablefmt="grid", colalign=("center", "center", "center", "center"))
    return watch_list_table


# This function reads the user's anime watch list
# It prints the user's anime watch list using the 'display_watch_list' function
# It then enters a loop where the user is  asked if they would like to update their watchlist.
# If the user chooses 'no', the loop breaks and the function ends
# If the user inputs anything other than 'yes' or 'no', it prints 'Invalid option'.
def anime_csv_options(app_user):
    watch_list = read_anime_csv(app_user)
    if len(watch_list) == 0:
        print("Watch list is empty")
        return
    else:
        print(display_watch_list(watch_list))

    choice = None
    while choice != 'no':
        choice = prompt_yes_or_no_user_input("Would you like to update the status of an Anime? [yes/no]: ")
        if choice == 'yes':
            watch_list = update_anime_csv(app_user, watch_list)
            print(display_watch_list(watch_list))
        elif choice == 'no':
            break
        else:
            print('Invalid option')


# This function constructs the CSV file name
def file_name(app_user):
    return f"{app_user}_watchlist.csv"


# This function has a single parameter 'app_user'.
# 'path.isfile()' checks if the file exists
# 'csv.DictReader(csvfile, skipinitialspace=True)' Uses 'csv.DictReader' to read each row as a dictionary where the keys
# are the column headers, and the values are the corresponding cell values in each row.
# 'skipinitialspace=True' allows for spaces after the delimiter to be ignored
# '[{k: v for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]' This iterates over each
# row produced by 'csv.DictReader' and makes a dictionary for each row. Which are then added to the 'watch_list'
def read_anime_csv(app_user):
    if not path.isfile(file_name(app_user)):
        return []

    with open(file_name(app_user), newline='') as csvfile:
        watch_list = [{k: v for k, v in row.items()} for row in csv.DictReader(csvfile, skipinitialspace=True)]
    return watch_list


# This function updates the status of an anime in the user's watch list
# It prompts the user to input the ID of the anime they want to update
# Then provides a dictionary of mapped status choices and their descriptions.
# If the anime ID is found, it updates the status and records the current
# timestamp as an updated time.
# It prints a confirmation message if the status is successfully updated,
# otherwise, it informs the user that the anime ID was not found.
# Finally, it returns the updated watch list by calling the 'read_the_anime_csv'
# function with the 'app_user'.
def update_anime_csv(app_user, watch_list):
    anime_id = input("Enter ID to update: ")
    # Mapping status choices to their descriptions
    anime_status_mapping = {
        '1': 'Watched',
        '2': 'Currently Watching',
        '3': 'To Be Watched'
    }
    print("Please select the number to set the status of this Anime from the following list: ")
    for key, value in anime_status_mapping.items():
        print(f'{key}: {value}')

    update_status = input("Type the number related to your choice here: ")
    if update_status in anime_status_mapping:
        new_status = anime_status_mapping[update_status]
    else:
        print("Invalid choice. Status not updated")
        return

    updated = False
    with open(f"{app_user}_watchlist.csv", 'w') as csv_file_name:
        anime_dict = ['Id', 'Title', 'Status', 'Updated']
        writer = csv.DictWriter(csv_file_name, fieldnames=anime_dict)
        writer.writeheader()
        for row in watch_list:
            if anime_id == row['Id']:
                row['Status'] = new_status
                # 'datetime.datetime.now()' calls a 'datetime' object representing the current date and time.
                # '.strftime("%d-%m-%Y %H:%M")' this method formats the 'datetime' object into a string format,
                # 'DD-MM-YYYY HH:MM';
                # '%d' - Day of the month as a zero-padded decimal number (01 to 31)
                # '%m' - Month as a zero-padded decimal number (01 to 12)
                # '%Y' - Year with century as a decimal number
                # '%H' - Hour (24-hour clock) as a zero-padded decimal number (00 to 23)
                # '%M' - Minute as a zero-padded decimal number (00 to 59)
                row['Updated'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                updated = True
            writer.writerow(row)

    if updated:
        print("Status updated successfully.")
    else:
        print("Anime ID not found.")
    return read_anime_csv(app_user)


# This function allows user to filter and search for anime based on a search field.
# If the user chooses 'yes', it prompts the user to select a search field by typing in the corresponding number.
# Based on the user's choice, it calls a specific functions to perform the search.
# If the user inputs an invalided choice, it prompts them to choose a valid option.
# Alternatively if the User chooses 'no', it prints a message indicating that they
# will be redirected back to the main menu.
def anime_filtering(app_user):
    output = ("Please select the number that represents your search field from the following list\n"
              "1: Search by genre\n"
              "2: Search by Top-rated Anime")
    print(output)

    choice = None
    while choice != '1' and choice != '2':
        choice = input("Type the number related to your choice here: ")
        if choice == '1':
            search_anime_by_genre()
        elif choice == '2':
            anime_by_rank()
        else:
            print("Invalid choice, Please choose either '1'or '2'")

    display_anime_by_id(app_user)


# This function allows the user to search for anime by genre by;
# API Request: sends a request to the Jikan API to retrieve a list of anime genres
# Process Response: extracts the genre data from API response
# List Genres: lists the available genre along with their IDs
# User Input: prompts the user to input genre ID from the list
# Validate Input: checks if the input genre ID is valid by comparing it with the available genre IDs
# Search Anime: if the input genre is valid, it sends another request to the Jikan API to retrieve
# anime of that genre.
# Display Results: displays the anime found in selected genre, including their ID, title, score, rating,
# and a shortened synopsis.
# Handle No Results: if no anime are found for selected genre, it notifies the user accordingly.
# Handle Invalid Input: if the user inputs an invalid genre ID, it prompts them to try again.
def search_anime_by_genre():
    url = 'https://api.jikan.moe/v4/genres/anime'
    response = requests.get(url)
    genres_data = response.json()
    genres = genres_data['data']

    # Sorts the genres by their ID in ascending order
    genres.sort(key=lambda x: x['mal_id'])

    # List the genres and their IDs
    print("Available genres:")
    for genre in genres:
        print(f"{genre['mal_id']}: {genre['name']}")

    # Prompt user to input a genre ID
    genre_id = input("Enter the Genre ID from the list above: ").strip()

    # Validate the input genre ID
    if any(genre['mal_id'] == int(genre_id) for genre in genres):
        # Use the genre ID to get anime of that genre
        genre_anime_url = f'https://api.jikan.moe/v4/anime?genres={genre_id}'
        genre_response = requests.get(genre_anime_url)
        anime_list = genre_response.json()

        # Display the anime list
        if 'data' in anime_list and anime_list['data']:
            print("Anime found in this genre: ")

            for anime in anime_list['data']:
                # This retrieves the 'synopsis' attribute in the anime 'data'
                # It sets 'synopsis' to a maximum length of 150 characters and checks
                # if the length exceeds the maximum limit. If it does it slices the synopsis to use only the first
                # 150 characters and adds ellipses (...). If it doesn't exceed the limit, it keeps the original length.
                synopsis = anime.get('synopsis', 'No synopsis available')
                s = 150
                sliced_synopsis = synopsis[:s] + "..." if len(synopsis) > s else synopsis
                print(f"""
                            ID: {anime['mal_id']}
                            Title: {anime['title_english'] if anime['title_english'] else anime['title']}
                            Score: {anime['score'] if anime['score'] is not None else 'N/A'}
                            Rating: {anime['rating'] if anime['rating'] is not None else 'N/A'}
                            Synopsis: 
                                {sliced_synopsis}
                            """)
        else:
            print("No anime found for the selected genre.")
    else:
        print("Invalid genre ID. Please try again.")


# This function fetches and displays the top-ranked anime from the Jikan API
# It requests information from the API by sending a 'GET' request
# The response is then processed and the anime data extracted.
# The anime is then stored in a list by their rank in ascending order. The list is also limited to the top 10 anime
# It then prints the 10 anime along with their rank, ID, score, rating, URL and a shortened synopsis (up to 150
# characters, followed by an ellipsis if the synopsis is longer).
def anime_by_rank():
    url = 'https://api.jikan.moe/v4/top/anime'
    response = requests.get(url)
    anime_data = response.json()
    anime_list = anime_data['data']

    # Sorts the top anime by their rank in ascending order
    anime_list.sort(key=lambda x: x['rank'])
    # Capping the list to 10
    # ':10' - this means that we are slicing from the beginning of the list (index 0) up to,
    # but not including, index 10. This selects the first 10 elements in the list.
    anime_list = anime_list[:10]

    # Lists the anime's and their ranks
    print("Top Anime by Popularity:")
    for anime in anime_list:
        synopsis = anime.get('synopsis', 'No synopsis available')
        s = 150
        sliced_synopsis = synopsis[:s] + "..." if len(synopsis) > s else synopsis
        title = anime.get('title_english') or anime['title']
        print(f"""
                    Rank {anime['rank']}: {title}
                    ID: {anime['mal_id']}
                    Score: {anime['score'] if anime['score'] is not None else 'N/A'}
                    Rating: {anime['rating'] if anime['rating'] is not None else 'N/A'}
                    Url: {anime['url']}
                    Synopsis: 
                              {sliced_synopsis}
""")


# This function fetches detailed information about an anime using the ID from the Jikan API.
# This stores a URL specific to the anime ids and send a 'GET' request to the Jikan API to retrieve detailed information
# about that aime.
# If 'the status_code' is 200 (OK), indicating that the request was sucessful. It returns the JSON data containing
# detailed information about the anime.
# If the 'status_code' is different from 200, it returns an empty dictionary. This would indicate that no data
# was retrieved, or an error occurred during the request.
def fetch_anime_by_id(anime_id):
    anime_url = f'https://api.jikan.moe/v4/anime/{anime_id}/full'
    response = requests.get(anime_url)

    if response.status_code == 200:
        return response.json()['data']
    else:
        return {}


# This function prompts the user to input an Anime ID and then displays detailed information by;
# User Input - prompts the user to input an anime ID
# Fetch Anime Data - calls the 'fetch_anime_by_id' function to retrieve detailed information about the anime
# corresponding to the provided ID.
# Handle Data - if the retrieved anime data is not empty, it formats the synopsis of the anime the 'textwrap.fill()'
# function to wrap the text and ensures the proper indentation.
# The function then gets the English title of the anime or the original title if the English title is not available.
# It also prints various details about the anime, including its title, score, number of episodes, synopsis and URL to
# access the anime.
# Handle Errors - if there is an issue fetching the anime data (resulting in an empty dictionary), it prints an error
# message instructing the user to try again.
# The user is then presented with a 'save to file' prompt, this allows them to save the anime,
# and it's ID to their watchlist
def display_anime_by_id(app_user):
    anime_id = None

    while anime_id != 'exit':
        anime_id = input("Please input an Anime ID for more information [type 'exit' to quit]: ").strip()

        if anime_id == 'exit':
            print("Returning you to the main menu.")
            break

        anime_data = fetch_anime_by_id(anime_id)

        if len(anime_data) > 0:

            # Stores the synopsis extracted from 'anime_data' into a variable, which we then pass in to be wrapped.
            synopsis = anime_data['synopsis']
            anime_title = anime_data['title_english'] if anime_data['title_english'] else anime_data['title']

        # The 'textwrap.fill' function is used to wrap the text into lines of a specific width and to add indentation.
        # 'synopsis' - synopsis extracted from 'anime_data'
        # 'width=150' - specifics the maximum line width (in characters).
        # Lines longer than this width will be wrapped to the next line.
        # 'initial_indent=' ' * 5' - this adds an initial indentation of 5 spaces at the beginning of the first line.
        # 'subsequent_indent=' ' * 25' - this adds an indentation of 25 spaces at the beginning of each subsequent line
        # after the first line.
            formatted_synopsis = textwrap.fill(synopsis, width=150, initial_indent=' ' * 5, subsequent_indent=' ' * 25)
            print(f"""
                        Title: {anime_title}
                        Score: {anime_data['score'] if anime_data['score'] is not None else 'N/A'}
                        Episodes: {anime_data['episodes']}
                        Synopsis: 
                        {formatted_synopsis}
                        URL: {anime_data['url']}
                        """)

            save_to_csv = prompt_yes_or_no_user_input(
                "Would you like to save this anime to your watch list? [yes/no]: ")
            if save_to_csv == 'yes':
                save_anime_to_csv(app_user, anime_id, anime_title)
        else:
            print("Error fetching manga data. Please try again.")


# This function prompts the user to save an anime to their watch list in a CSV file.
# It takes in three parameters 'app_user', 'anime_id' and 'anime_title'
# If a file does not yet exist for the user, it will construct a CSV file.
# Taking in the 'app_user' parameter it will name the file.
# Then prompts the user to input the ID of the anime they would like to save.
# It retrieves the anime details using the 'fetch_anime_by_id' function.
# It also checks whether the ID already exists in the users watch-list.
# If it does a message stating this will be printed.
# It opens the user's watch list CSV in append mode 'a+'
# The CSV columns are defined using 'Id', 'Title' and 'Status'
# It also creates a 'csv.DictWriter' object for writing dictionaries to the CSV file.
# It then writes a new row to the CSV file with the anime's ID and tiles and sets the
# 'Status' to unwatched as default.
#
def save_anime_to_csv(app_user, anime_id, anime_title):
    csv_file_name = file_name(app_user)

    # Ensure watchlist doesn't already contain the anime id
    watch_list = read_anime_csv(app_user)
    if any(row['Id'] == anime_id for row in watch_list):
        print(f"{app_user}, your watch list already contains that ID")
    else:
        with open(csv_file_name, 'a+') as csv_file_name:
            anime_dict = ['Id', 'Title', 'Status', 'Updated']
            writer = csv.DictWriter(csv_file_name, fieldnames=anime_dict)

            # Writes the header only if the file is new or empty
            csv_file_name.seek(0, 2)  # Moves the cursor to the end of the file
            if csv_file_name.tell() == 0:
                writer.writeheader()
            writer.writerow({'Id': anime_id,
                             'Title': anime_title,
                             'Status': 'Unwatched',
                             'Updated': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")})

        print(f"{app_user}, the ID has been added to your watch list\n")

    watch_list = read_anime_csv(app_user)
    print(display_watch_list(watch_list))


# Initialise App
welcome_user()
