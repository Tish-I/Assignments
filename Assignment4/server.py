# pip install Flask
from flask import Flask, jsonify, request, Response
import json
from datetime import datetime
from db_utils import member_borrow, books_by_availability, check_member_exists, borrow_by_book_id, \
    wait_list_reserve, view_borrowed_books, return_borrowed_book, cancel_waitlist_res, new_member_signup, \
    get_all_books, update_available_books, check_email_exists

# Initialising the app Flask object
app = Flask(__name__)


# Home page
# Terminal interaction
# curl http://127.0.0.1:5000/
@app.route('/')
def welcome():
    return {'hello': 'welcome to the library'}


# This API endpoint uses 'POST' to check if an email exists in the DB
# Terminal interaction
# curl -X POST -H "Content-Type: application/json" -d '{"email": "john.doe@gmail.com"}' http://127.0.0.1:5000/email
@app.route('/email', methods=['POST'])
def email_exists():
    inputs = request.get_json()
    if 'email' not in inputs.keys():
        return Response(json.dumps({'error': 'Invalid input - email missing'}),
                        content_type='application/json',
                        status=400)
    elif len(inputs['email']) == 0:
        return Response(json.dumps({'error': 'Invalid input - email can\'t be empty'}),
                        content_type='application/json',
                        status=400)
    res = check_email_exists(inputs['email'])
    return jsonify({'status': res})


# This API endpoint uses 'GET' to check member borrow status
# Terminal interaction
# curl http://127.0.0.1:5000/borrow/3006 - can't borrow
# curl http://127.0.0.1:5000/borrow/3001 - can borrow
@app.route('/borrow/<int:member_id>', methods=['GET'])
def borrow_status(member_id):
    member_exists = check_member_exists(member_id)
    if not member_exists:
        response_data = {
            'error': "This member_id does not exist on file"
        }
        return Response(json.dumps(response_data), content_type='application/json', status=404)

    borrow_result = member_borrow(member_id)
    message = borrow_result[0]['message']

    response_data = {
        'member_id': member_id,
        'status': message
    }

    if "You are allowed to borrow new books." in message:
        response_data['available_books'] = books_by_availability()

    json_response = json.dumps(response_data)

    return Response(json_response, content_type='application/json')


# This API endpoint uses 'GET' to view all books in the 'Library_db'
# Terminal interaction
# curl http://127.0.0.1:5000/books
@app.route('/books', methods=['GET'])
def view_all_books():
    records = get_all_books()
    return Response(json.dumps(records, default=str), content_type='application/json')


# This API endpoint uses 'GET' to view current loans
# Terminal interaction
# curl http://127.0.0.1:5000/loan/3001 - no loans, will return empty in the terminal
# curl http://127.0.0.1:5000/loan/3006
@app.route('/loan/<int:member_id>', methods=['GET'])
def view_loans(member_id):
    records = view_borrowed_books(member_id)
    # Dates can return as date objects, so default to strings instead
    return Response(json.dumps(records, default=str), content_type='application/json')


# This API endpoint uses 'POST' in order to allow users to borrow books
# Terminal interaction
# curl -X POST -H "Content-Type: application/json" -d '{"book_id": 2001, "member_id": 3001, "loan_date": "2023-06-01"}' http://127.0.0.1:5000/loan
@app.route('/loan', methods=['POST'])
def loan_book():
    loans = request.get_json()
    if not loans:
        return Response(json.dumps({'error': 'Invalid input'}), content_type='application/json', status=400)
    # Make sure the user can't put in an empty value
    if 'book_id' not in loans.keys():
        return Response(json.dumps({'error': 'Invalid input - book_id missing'}),
                        content_type='application/json',
                        status=400)
    elif len(loans['book_id']) == 0:
        return Response(json.dumps({'error': 'Invalid input - book_id can\'t be empty'}),
                        content_type='application/json',
                        status=400)

    loan_date = datetime.strptime(loans['loan_date'], '%Y-%m-%d').date()

    # Mark the book as loaned out
    res = borrow_by_book_id(
        book_id=loans['book_id'],
        member_id=loans['member_id'],
        loan_date=loan_date
    )
    if 'error' in res.keys():
        return Response(json.dumps(res),
                        content_type='application/json',
                        status=400)

    # Update availability of the book
    update_available_books(loans['book_id'])
    return Response(json.dumps({'message': "Book borrowed successfully"}))


# This API endpoint uses 'POST' in order to allow users to return books
# Terminal interaction
# curl -X POST -H "Content-Type: application/json" -d '{"book_id": 2001, "member_id": 3001}' http://127.0.0.1:5000/return
@app.route('/return', methods=['POST'])
def return_book_by_id():
    return_data = request.get_json()
    if not return_data:
        return Response(json.dumps({'error': 'Invalid input'}), content_type='application/json', status=400)

    # Make sure the user can't put in an empty value
    if 'book_id' not in return_data.keys():
        return Response(json.dumps({'error': 'Invalid input - book_id missing'}),
                        content_type='application/json',
                        status=400)
    elif len(return_data['book_id']) == 0:
        return Response(json.dumps({'error': 'Invalid input - book_id can\'t be empty'}),
                        content_type='application/json',
                        status=400)

    # Should check if book is actually borrowed
    return_book = return_borrowed_book(
        book_id=return_data['book_id'],
        member_id=return_data['member_id'],
    )
    return_book['status'] = 'success'

    return Response(json.dumps(return_book))


# This API endpoint uses 'POST' in order to allow users to reserve books
# Terminal interaction
# curl -X POST -H "Content-Type: application/json" -d '{"book_id": 2004, "member_id": 3001}' http://127.0.0.1:5000/reserve

@app.route('/reserve', methods=['POST'])
def reserve_book():
    reserve = request.get_json()
    if not reserve:
        return Response(json.dumps({'error': 'Invalid input'}), content_type='application/json', status=400)

    # Make sure the user can't put in an empty value
    if 'book_id' not in reserve.keys():
        return Response(json.dumps({'error': 'Invalid input - book_id missing'}),
                        content_type='application/json',
                        status=400)
    elif len(reserve['book_id']) == 0:
        return Response(json.dumps({'error': 'Invalid input - book_id can\'t be empty'}),
                        content_type='application/json',
                        status=400)

    reservation_response = wait_list_reserve(
        book_id=reserve['book_id'],
        member_id=reserve['member_id']
    )
    reservation_response['status'] = 'success'

    # Return the response with the message
    return Response(json.dumps(reservation_response), content_type='application/json')


# This API endpoint uses 'POST' in order to allow users to cancel a book reservation
# Terminal interaction
# curl -X POST -H "Content-Type: application/json" -d '{"book_id": 2004, "member_id": 3001}' http://127.0.0.1:5000/reserve/cancel
@app.route('/reserve/cancel', methods=['POST'])
def cancel_wait_list():
    cancel_reserve = request.get_json()
    if not cancel_reserve:
        return Response(json.dumps({'error': 'Invalid input'}), content_type='application/json', status=400)

    # Make sure the user can't put in an empty value
    if 'book_id' not in cancel_reserve.keys():
        return Response(json.dumps({'error': 'Invalid input - book_id missing'}),
                        content_type='application/json',
                        status=400)
    elif len(cancel_reserve['book_id']) == 0:
        return Response(json.dumps({'error': 'Invalid input - book_id can\'t be empty'}),
                        content_type='application/json',
                        status=400)

    reservation_response = cancel_waitlist_res(
        book_id=cancel_reserve['book_id'],
        member_id=cancel_reserve['member_id']
    )

    return jsonify(reservation_response)


# This API endpoint uses 'POST' in order to allow new users to sign-up
# Terminal interaction
# curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@gmail.com", "phone_number": "12345678901", "membership_date": "2023-06-01"}' http://127.0.0.1:5000/signup
@app.route('/signup', methods=['POST'])
def new_signup():
    member_data = request.get_json()
    if not member_data:
        return Response(json.dumps({'error': 'Invalid input'}), content_type='application/json', status=400)

    required_data = ['first_name', 'last_name', 'email', 'phone_number', 'membership_date']
    for data in required_data:
        if data not in member_data:
            return Response(json.dumps({'error': f'Missing field: {data}'}), content_type='application/json',
                            status=400)

    phone_number = member_data['phone_number']
    if len(phone_number) != 11 or not phone_number.isdigit():
        return Response(json.dumps({'error': 'Phone number must be exactly 11 digits long.'}),
                        content_type='application/json', status=400)

    membership_date = datetime.strptime(member_data['membership_date'], '%Y-%m-%d').date()

    response = new_member_signup(
        first_name=member_data['first_name'],
        last_name=member_data['last_name'],
        email=member_data['email'],
        phone_number=member_data['phone_number'],
        membership_date=membership_date
    )
    if response['status'] == 'success':
        new_member_id = response['message'].split("Your ID is ")[-1].strip(".")
        return Response(json.dumps({
            'status': 'success',
            'member_id': new_member_id,
            'first_name': member_data['first_name'],
            'last_name': member_data['last_name'],
            'message': f"{member_data['first_name']} {member_data['last_name']}, "
                       f"you have successfully been added to the Library database. "
                       f"Your ID is {response['member_id']}."
        }), content_type='application/json', status=201)
    else:
        return Response(json.dumps({'error': response['message']}), content_type='application/json', status=400)


if __name__ == '__main__':
    app.run(debug=True)
