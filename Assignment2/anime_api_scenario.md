# Assignment 2 - Python

## Summary
For my Assignment 2 project, I decided to utilise the [Jikan API](https://jikan.moe/).
I wanted to use it to pull data which the user could then access in a few ways to retrieve information about Anime.

This API does not require an API key.

## Scenario
Create a program that allows users to browse anime by genre or by top-rated.
The users should be able to read a synopsis of the anime when they find something interesting.
Allow the user to save the anime to a "watchlist" if they want.
Allow the user to review their watchlist at any point.
Allow the user to update the current watch status of any anime in their watchlist.

## Outcome
I have created an app called 'Kawaii_Haven'.
The app allows users to save their selected Anime IDs, names and current watch status in a watchlist stored as a CSV file.
On start-up the app asks the user for their name.
This is stored in a variable call 'app_user' and is used throughout the app.
Its main purpose is to map users to their watchlist.

Next, the user is shown a menu allowing them to navigate the app:
```text
1: 'Search by Anime',
2: 'Access your Watch-list'
```

Depending on their choice, this would then take them into a different section of the app.

For example, 'Search by Anime' will take them to another menu in the app where they are presented with more choices:
```text
1: 'Search by genre',
2: 'Search by Top-rated Anime'
```

Based on the users choices, the app will display a summary of the relevant anime.
The user will also be able to inspect an anime in more detail such as their IDs, English names, Scores, Ratings etc.

The user is then prompted to save an anime to their watch list by inputting the anime ID.
This saves their chosen anime ID, Title and defaults the current status to unwatched.

| Id    | Title                         | Status              | Updated           |
|-------|-------------------------------|---------------------|-------------------|
| 15417 | Gintama: Enchousen            | Unwatched           | 02-06-2024 14:52  | 
| 3958  | Kannagi: Crazy Shrine Maidens | Currently Watching  | 02-06-2024 14:52  |

The user is also able to access their watchlist.
Here they can change the current status of any anime in their watchlist by inputting their IDs.
If the ID matches an anime, they then have the option to update the watch status to any of the following:
```text
1: 'Watched',
2: 'Currently Watching',
3: 'To Be Watched'
```

Anime saved to the readers watchlist is stored in a CSV file.
When a user requests the data, it is read in as a list of dictionaries and displayed in a readable format for the user. 
The user can also access the watchlist directly through the CSV file if needed.

## Flow diagram
This diagram shows the flow of the 'Kawaii_Haven' app
```text
              ┌────────┐                    
              │ Enter  │                    
              │Username│                    
              └───┬────┘                    
                  │                         
                ┌─▼──┐                      
         ┌──────►Main◄───────────────────┐  
         │      │Menu│                   │  
         │      └─┬─┬┘                   │  
         │        │ │                    │  
      ┌──┴──┐     │ │    ┌──────┐        │  
  ┌───►Print◄─────┘ └────►Search│        │  
  │   │ CSV │            │Anime │        │  
  │   └──┬──┘            └─┬───┬┘        │  
  │      │          ┌───┐  │   │ ┌─────┐ │  
  │   ┌──▼───┐      │TOP◄──┘   └─►Genre│ │  
  └───┤Update│      └─┬─┘        └──┬──┘ │  
      │ CSV  │        │             │    │  
      └──────┘        └──────┬──────┘    │  
                             │           │  
                        ┌────▼───┐       │  
                        │Display ├───────┤  
                        │Detailed│       │  
                        └────┬───┘       │  
                             │           │  
                         ┌───▼──┐        │  
                         │Add TO├────────┘  
                         │ CSV  │           
                         └──────┘           
```

## Requirements:
In order to use the Kawaii_Haven app, you should ensure these modules are installed through your terminal;
```shell
pip install pandas
pip install textwrap3
pip install tabulate
```
