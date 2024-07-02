import requests
from datetime import datetime
from tabulate import tabulate
import pandas as pd

# Reusable Base URL
BASE_URL = 'http://127.0.0.1:5000'

# Reusable headers
headers = {'Content-Type': 'application/json'}


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


# This function connects to the server in order to add new members to the database.
# It also checks if anything goes wrong during the sign-up and will display appropriate messages.
def new_member(member_data):
    url = f"{BASE_URL}/signup"
    response = requests.post(url, json=member_data, headers=headers)

    if response.status_code == 400:
        return {'status': 'error', 'message': response.json().get('error', 'Invalid server response')}

    if response.status_code != 201:
        return {'status': 'error', 'message': 'Unexpected server response'}

    return response.json()


# Queries the server to check if an email already exists
# Returns True if it does or if an error was encountered
def check_email(email):
    url = f"{BASE_URL}/email"
    response = requests.post(url, json={"email": email}, headers=headers).json()
    if 'error' in response.keys():
        print(response['error'])
        return True
    elif response['status']:
        print("Email already exists.")
        return True
    else:
        return False


# This function will give the user a new member choice of Yes and No.
# if yes it will take them to the sign-up process where it will check the database records against their email
# and phone numbers, if they're already in the database it will print an appropriate message.
# It will let them know if their details where successfully added to the database or not.
# If successful it will inform them of their Library ID.

def sign_in():
    new_user_choice = prompt_yes_or_no_user_input("Are you a new member? (yes/no): ")

    if new_user_choice == 'yes':
        email = input("Please enter your Email: ")
        if check_email(email):
            return None

        member_data = {
            "first_name": input("Please enter your First Name: "),
            "last_name": input("Please enter your Last Name: "),
            "email": email,
            "phone_number": input("Please enter your Phone number: "),
            "membership_date": datetime.now().strftime('%Y-%m-%d')  # Using the current date to autofill the date
        }

        signup_response = new_member(member_data)
        if signup_response.get('status') == 'success':
            member_id = signup_response.get('member_id')
            first_name = signup_response.get('first_name')
            last_name = signup_response.get('last_name')
            print(f"{first_name} {last_name}, you have successfully been added to the Library database. "
                  f"Your Library ID is {member_id}.")
            return member_id
        else:
            print(f"Signup failed: {signup_response.get('message')}")
            return None
    elif new_user_choice == 'no':
        member_id = input("Please input your Library Member ID (30**): ").strip()
        print(f"You have signed in with Member ID: {member_id}")
        return member_id


# This function uses the member id, connects to the web server and checks the members borrow status
# Using the users Borrow status, this function will display if the user is allowed to borrow or not.
# If they are allowed to borrow it will display the list of books that are currently at their disposal.
def display_borrow_status(member_id):
    response_data = requests.get(f"{BASE_URL}/borrow/{member_id}", headers=headers).json()

    if 'error' in response_data.keys():
        print(response_data['error'])
    else:
        member_id = response_data['member_id']
        status = response_data['status']
        print(f"{'MEMBER':<15} {'BORROW STATUS':<35}")
        print("_" * 50)
        print(f"{member_id:<15} {status:<15}")

        if "You are allowed to borrow new books" in status:
            print("\nAvailable books you can borrow:")

            if 'available_books' in response_data:

                # Convert to Dataframe
                df = pd.DataFrame.from_dict(response_data['available_books'])
                # Capitalise column names
                df.columns = [col.upper() for col in df.columns]
                # Left align data for tabulate
                table = tabulate(df, headers='keys', tablefmt='psql', showindex=False, stralign='left')
                print(table)
                print("\n")
            else:
                print("No Books available for you to borrow.")
        elif "Sorry, you cannot borrow any new nooks." in status:
            print(status)


# This function is used to display the full library of books to the user
def display_all_books():
    books = requests.get(f"{BASE_URL}/books", headers=headers).json()

    if not books:
        print("No Books available.")
        return

    # Convert to Dataframe
    df = pd.DataFrame.from_dict(books)
    # Capitalise column names
    df.columns = [col.upper() for col in df.columns]
    # Left align data for tabulate
    print("Total list of Books currently in the Library Database: ")
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, stralign='left'))
    print("\n")


# This function connects to the server to check if the user currently has any borrowed books
# It will display different messages depending on this. If they do have books they're currently
# borrowing, it will display them using tabulate.
def display_loaned_books(member_id):
    loaned_books = requests.get(f"{BASE_URL}/loan/{member_id}", headers=headers).json()

    if not loaned_books:
        print("No Books currently on loan.")
        return

    # Convert to Dataframe
    df = pd.DataFrame.from_dict(loaned_books)
    # Capitalise column names
    df.columns = [col.upper() for col in df.columns]
    # Left align data for tabulate
    print("You currently have the following on loan:")
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, stralign='left'))
    print("\n")


# This function allows the user to borrow books from the list of books available to borrow.
# Doing so will update the available_copies of the book by - 1 or remove the book from showing up
# if there are no more available copies.
def borrow_book(member_id):
    book_id = input("Please enter the book ID in order to borrow: ").strip()

    url = f"{BASE_URL}/loan"
    data = {
        'book_id': book_id,
        'member_id': member_id,
        'loan_date': datetime.now().strftime('%Y-%m-%d')  # Using the current date to autofill the date
    }
    response = requests.post(url, json=data, headers=headers).json()

    if response.get('message') == "Book borrowed successfully":
        print(f"\nSuccessfully borrowed the book with ID: {book_id}\n")
    else:
        print(f"\nFailed to borrow book: {response.get('error')}\n")


# This function allows the user to return a book. Doing so will update the available_copies of the returned book by + 1
def return_book(member_id):
    book_id = input("Please enter the ID of the book you would like to return: ").strip()

    url = f"{BASE_URL}/return"
    data = {
        'book_id': book_id,
        'member_id': member_id,
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    response_json = response.json()
    if response_json.get('status') == 'success':
        print(response_json.get('message'))  # Print the message from the stored procedure
    else:
        print(f"Failed to return book: {response_json.get('message')}")


# These two functions allow the user to reserve a book and enter into the wait-list if there are others ahead of them.
# It also allows them to cancel their reservation if they wish. This won't remove them from the database but will change
# the status on the book from 'Pending' to 'Cancelled' and remove them from the book wait-list.
def member_reserve_book(member_id):
    book_id = input("Please enter the Book ID to reserve: ").strip()

    url = "http://127.0.0.1:5000/reserve"
    data = {
        'book_id': book_id,
        'member_id': member_id,
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    response_json = response.json()
    if response_json.get('status') == 'success':
        print(response_json.get('message'))  # Print the message from the stored procedure
    else:
        print(f"Failed to reserve book: {response_json.get('message')}")


def cancel_res(member_id):
    book_id = input("Enter the Book ID to cancel the reservation: ").strip()

    url = f"{BASE_URL}/reserve/cancel"
    data = {
        'book_id': book_id,
        'member_id': member_id,
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None

    response = response.json()
    if response.get('message') == "Reservation status updated to 'Cancelled'.":
        print(f"\nSuccessfully Cancelled your reservation for book with ID: {book_id}\n")
    else:
        print(f"\nFailed to cancel your reservation: {response.get('message')}\n")


# This function will simulate calling the API and allow users to browse the library
def run():
    # Welcome them to the library
    print('###################################')
    print('## Hello, welcome to the Library ##')
    print('###################################')
    print()

    # ask them to sign-in or sign-up
    # stores their ID for all functions that require it
    member_id = None
    while member_id is None:
        member_id = sign_in()
        print()

    # show their borrow status as soon as their member ID is collected
    display_borrow_status(member_id)
    if member_id:
        # reusing this endpoint to determine the library selection we show the user
        response_data = requests.get(f"{BASE_URL}/borrow/{member_id}", headers=headers).json()

        if 'error' in response_data.keys():
            print(response_data['error'])
            return

        # storing their borrow status response to determine how they can interact with the library
        status = response_data['status']
        print()
        if "You are allowed to borrow new books." in status:
            while True:
                output = ("Please select the number that relates to your choice from the following list.\n"
                          "1: Browse All Books\n"
                          "2: Borrow a Book\n"
                          "3: Return a Book\n"
                          "4: Reserve a Book\n"
                          "5: Cancel a Reservation\n"
                          "6: View current Books on Loan\n"
                          "7: Exit"
                          )
                print(output)  # Show the full library interactions

                choice = input("\nEnter your choice (1-7): ").strip()
                if choice == '1':
                    # viewing all books in the database
                    display_all_books()
                    print()
                elif choice == '2':
                    # borrowing books
                    borrow_book(member_id)
                    print()
                elif choice == '3':
                    # returning books
                    return_book(member_id)
                    print()
                elif choice == '4':
                    # reserving books
                    member_reserve_book(member_id)
                    print()
                elif choice == '5':
                    # cancelling reservations
                    cancel_res(member_id)
                    print()
                elif choice == '6':
                    # fetching members borrowed books
                    display_loaned_books(member_id)
                    print()
                elif choice == '7':
                    print("Thank you for visiting the Library. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a number between 1 and 7.")
                    print()
        else:
            # showing a limited range of options for users with overdue books
            while True:
                output = ("Please select the number that relates to your choice from the following list.\n"
                          "1: View current Books on Loan\n"
                          "2: Return a Book\n"
                          "3: Exit"
                          )
                print(output)  # Show the limited library interactions

                choice = input("Enter your choice (1-3): ").strip()
                if choice == '1':
                    # fetching members borrowed books
                    display_loaned_books(member_id)
                    print()
                elif choice == '2':
                    # returning books
                    return_book(member_id)
                    print()
                elif choice == '3':
                    print("Thank you for visiting the Library. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a number between 1 and 3.")
                    print()


if __name__ == '__main__':
    run()
