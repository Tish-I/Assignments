# Before using this file we must first ensure these are installed

# pip install mysql-connector-python
import mysql.connector
from config import HOST, USER, PASSWORD
from datetime import timedelta


# Set up our custom class
class DbConnectionError(Exception):
    pass


# Connect to the database
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# Defining queries that fetch-all from DB structure
def query_db(query, args=None):
    db_connection = None
    try:
        db_name = 'Library_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)

        if args is None:
            cur.execute(query)
        else:
            cur.execute(query, args)

        result = cur.fetchall()
        cur.close()
        return result
    except Exception:
        raise DbConnectionError("DB query error")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Defining queries that use commits structure
def update_db(query, args=None):
    db_connection = None
    try:
        db_name = 'Library_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        if args is None:
            cur.execute(query)
        else:
            cur.execute(query, args)

        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to insert data into DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Allow members to borrow books based on their CanBorrow status message
# First we need to check if they currently exist in our database
# Using 'SELECT COUNT(*)' to check if their member_id exists in the database
def check_member_exists(member_id):
    result = query_db(f"""SELECT COUNT(*) FROM Members WHERE member_id = '{member_id}'""")
    print(result)
    return result[0]['COUNT(*)'] > 0


# Using a stored procedure to check members borrow status
def member_borrow(member_id):
    return query_db(f"""CALL CanBorrow('{member_id}')""")


# View all books in the database using 'SELECT', 'CONCAT' and 'JOIN'
def get_all_books():
    records = query_db("""SELECT Books.book_id, Books.title, CONCAT(Authors.first_name, ' ', Authors.last_name) AS 
                                author_name, Books.genre, Books.publication_date, Books.isbn 
                          FROM Books 
                          JOIN Authors ON Books.author_id = Authors.author_id
                          ORDER BY Books.book_id;
                       """)
    return records


# Allowing users to see the books they currently have on loan using 'SELECT' and 'JOIN'
def view_borrowed_books(member_id):
    records = query_db(f"""
        SELECT DISTINCT Books.book_id, Books.title, Loans.loan_date, Loans.due_date
        FROM Loans
        JOIN Books ON Loans.book_id = Books.book_id
        JOIN Members ON Loans.member_id = Members.member_id
        WHERE Members.member_id = '{member_id}' AND is_returned = FALSE;
        """)
    return records


# Showing the available books from the Library DB using 'SELECT', 'JOIN'.
# '>' gets used as comparison operator to show books 'WHERE' the available_copies are more than 0
def books_by_availability():
    records = query_db("""
        SELECT Books.book_id, Books.title, Authors.first_name, Authors.last_name, Books.available_copies
        FROM Books
        JOIN Authors ON Books.author_id = Authors.author_id
        WHERE Books.available_copies > 0
        """)
    return records


# Allowing members to borrow a book using the book ID.
# First we need to check if the book has available copies
def get_available_copies(book_id):
    result = query_db(f"""
        SELECT available_copies
        FROM Books
        WHERE book_id = %s
        """, (book_id,))
    return result[0]['available_copies'] if result else 0


# An 'INSERT' 'VALUES' gets used here with '%s' acting as a placeholder.
# Information from the user will then get collected, replace the placeholders and be inserted into the DB
def borrow_by_book_id(book_id, member_id, loan_date):
    available_copies = get_available_copies(book_id)
    print(available_copies)

    if available_copies > 0:
        due_date = loan_date + timedelta(days=14)
        update_db(f"""
            INSERT INTO Loans (book_id, member_id, loan_date, due_date)
            VALUES (%s, %s, %s, %s)
            """, (book_id, member_id, loan_date, due_date))
        return{'message': "Book borrowed successfully"}
    else:
        return {'error': "No copies of that Book available for borrowing."}


# Updating the available copies of a book against the borrowed book.
# 'UPDATE' and 'SET' are used here to update the available_copies of books
# to - 1 when a user borrows a book.
def update_available_books(book_id):
    return update_db(f"""
        UPDATE Books
        SET available_copies = available_copies - 1
        WHERE book_id = %s AND available_copies > 0
        """, (book_id,))


# Reserving and adding to wait-list through the use of a stored procedure
def wait_list_reserve(book_id, member_id):
    try:
        db_name = 'Library_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        print(f"Connected to DB: {db_name}")

        cur.callproc("AddToWaitlist", (book_id, member_id))

        for result in cur.stored_results():
            result_data = result.fetchall()
            if result_data:
                reservation_message = result_data[0]['message']

                db_connection.commit()
                cur.close()
                return {'message': reservation_message}

    except Exception:
        raise DbConnectionError(f"Failed to read from DB for Member: {member_id}")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Allowing users to return their books using a stored procedure
def return_borrowed_book(book_id, member_id):
    try:
        db_name = 'Library_db'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        print(f"Connected to DB: {db_name}")

        cur.callproc("ReturnBook", (book_id, member_id))

        for result in cur.stored_results():
            result_data = result.fetchall()
            if result_data:
                book_return_message = result_data[0]['message']

                db_connection.commit()
                cur.close()
                return {'message': book_return_message}

    except Exception:
        raise DbConnectionError(f"Failed to read from DB for Member: {member_id}")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Allow users to cancel their reservations using 'UPDATE', 'SET', 'WHERE' and '%' placeholders.
def cancel_waitlist_res(book_id, member_id):
    # Check if the reservation exists
    reservation = query_db(f"""
        SELECT res_status
        FROM Reservations
        WHERE book_id = %s AND member_id = %s
    """, (book_id, member_id))

    if reservation:
        # Reservation exists
        update_db(f"""
            UPDATE Reservations 
            SET res_status = 'Cancelled'
            WHERE book_id = %s AND member_id = %s
            """, (book_id, member_id))
        return {'message': "Reservation status updated to 'Cancelled'."}
    else:
        # Reservation dose not exist
        return {'message': "No reservation found for the provided BookID and MemberID"}


# check users email
def check_email_exists(email):
    result = query_db("SELECT COUNT(*) FROM Members WHERE email = %s", (email,))
    return result[0]['COUNT(*)'] > 0


# Allow new members to sign up using and 'INSERT' statement and '%' placeholders to collect information about the user.
def new_member_signup(first_name, last_name, email, phone_number, membership_date):
    if check_email_exists(email):
        return {'status': 'error', 'message': 'Email already exists.'}

    new_member_id = create_new_member_id()
    update_db("""
        INSERT INTO Members (member_id, first_name, last_name, email, phone_number, membership_date) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (new_member_id, first_name, last_name, email, phone_number, membership_date))

    return {'status': 'success',
            'member_id': new_member_id,
            'message': f"{first_name} {last_name}, "
                       f"you have successfully been added to the "
                       f"Library database."
                       f"Your ID is {new_member_id}."}


# Issuing new members a Member-ID using 'ORDER BY', 'DESC' to ensure that the Members table
# get ordered by descending order. The last created id is then used as a benchmark to determine the new users ID number.
def create_new_member_id():
    result = query_db("SELECT member_id FROM Members ORDER BY member_id DESC LIMIT 1")
    return (int(result[0]['member_id']) + 1) if result else 3001
