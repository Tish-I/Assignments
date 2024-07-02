# Assignment 4 - Library Interface API

## Scenario
This API will allow new members to sign up to the Library and current members will be able to sign in.
From there the API will allow users to:

- View a list of books that are available to borrow
- Borrow and reserve books
- Return books
- Amend their book reservations by setting it as 'Cancelled'
- Each book that gets borrowed or reserved will be inserted/updated in the appropriate tables in the `Library-db`
- Additionally, the API will keep track of the `available_copies` numbers against the books members borrow.

### Prerequisites
Before you begin, ensure you have the following installed:

```text
 Python
 Pip
 MySQL and MySQL Workbench
```

### Setup Instructions

#### Step 1:
Ensure you have MySQL Workbench installed and running. 
 - The SQL file, `Library.sql`,  should be run to ensure data is inserted and the stored procedures are initialised and saved.

#### Step 2:
Update the 'config.py' file with your database credentials
 - The `host`, `user` and `password` in the config file should be replaced with your own SQL details.

#### Step 3:
Please make sure that the following are run through the terminal in python.

```shell
pip install mysql-connector-python
pip install flask
pip install requests
pip install pandas
pip install tabulate
```

### Run the User application

Before running the `main.py` file, make sure that the Flask `server.py` file is running

#### Expected Outcomes

#### Sign-in or Sign-up:
- `POST '/signup'`
- Sign-in or Sign-up: Upon initialisation Users are met with an "Are you a new member (yes/no) choice"
- Sign-up a new member: This will confirm or deny successful sign-up along with a Library ID.
- The new user will also be inserted into the `Members` table in the SQL file.

#### Check for duplicate email: 
- `POST '/email'`
- If the DB finds a duplicate email in the DB it will print an appropriate message.

#### Borrow Status:
- `GET '/borrow/<int:member_id>'`
- Sign-in an existing member: This will sign the member in and display their borrow status.
- Based on this members will either have full or limited Library interaction options.

#### Browse all Books:
- `GET '/books'`
- Browse All Books: This will list all books currently in the library 
(Pulls this information from both the `Books` and `Authors` tables in DB).

#### Borrow a Book:
- `POST '/loan'`
- Borrow a book: This will confirm or deny successful borrowing and update the `available_copies` column by -1.
- It will also add the members details into the DB and issue a return date 14 days in the future.

#### View borrowed Books:
- `GET '/loan/<int:member_id>'`
- View current Books on Loan: Allows users to see a list of books they currently have borrowed as well as 
the due date for each book.

#### Return a Book:
- `POST '/return'`
- Return a book: This allows members to return a book only if it finds their memberID and the 
correlating bookID in the `Loans` table. 
- It will then confirm successful return and update the `available_copies` column +1. 
- If it does not find them in the DB an appropriate message gets returned.

#### Reserve a Book:
- `POST '/reserve'`
- Reserve a book: This will use a stored procedure in the SQL file to check if the member is reserving 
the chosen book for the first time. 
- It checks if others have reserved that same book. 
- The dates that each person reserved the book will add the member into a queue as well as into the `Reservations` table.
- It will return a message denying or confirming successful insertion. 
- If successful it will return the members queue position for the book.

#### Cancel a Reservation:
- `POST '/reserve/cancel'`
- Cancel a reservation: Members will be allowed to amend their reserved book to 'Cancelled' in the DB.
- If successful it will not delete them from the Reservations table but will change their default 'Pending'
status to 'Cancelled'.

#### Error Handling:
- I have put in a few checks and error handling to catch if a user tries to input empty data.
- I've also simulated checks to ensure members can't borrow books that are not available for borrowing.
- I have made sure members can't cancel a reservation if they don't have one on file
