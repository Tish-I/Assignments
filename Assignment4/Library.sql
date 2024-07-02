-- Create a library database
CREATE DATABASE Library_db;
USE Library_db;

-- Create the Authors table
CREATE TABLE Authors (
author_id INT PRIMARY KEY,
first_name VARCHAR(25),
last_name VARCHAR(25),
);

-- Create the Books table
CREATE TABLE Books(
book_id INT PRIMARY KEY,
title VARCHAR(75),
author_id INT,
genre VARCHAR(50),
publication_date DATE,
isbn VARCHAR(17) UNIQUE,
total_copies INT,
available_copies INT,
FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);


-- Create the Members table
CREATE TABLE Members(
member_id INT PRIMARY KEY,
first_name VARCHAR(25),
last_name VARCHAR(25),
email VARCHAR(100) UNIQUE,
phone_number VARCHAR(11),
membership_date DATE
);

-- Create the Loans table
CREATE TABLE Loans(
loan_id INT AUTO_INCREMENT PRIMARY KEY,
book_id INT,
member_id INT,
loan_date DATE,
due_date DATE,
return_date DATE,
is_returned BOOLEAN DEFAULT FALSE,
FOREIGN KEY (book_id) REFERENCES Books(book_id),
FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Create the Reservations table
CREATE TABLE Reservations(
reservation_id INT AUTO_INCREMENT PRIMARY KEY,
book_id INT,
member_id INT,
reservation_date DATE,
res_status VARCHAR(20),
FOREIGN KEY (book_id) REFERENCES Books(book_id),
FOREIGN KEY (member_id) REFERENCES Members(member_id)
);


-- Inserting data into the Authors table
INSERT INTO Authors (author_id, first_name, last_name) VALUES
(1001, 'Joanna', 'Wallace'),
(1002, 'Andrew', 'Shanahan'),
(1003, 'Freida', 'McFadden'),
(1004, 'Lucinda', 'Berry'),
(1005, 'Keven', 'Panetta'),
(1006, 'Ling', 'Ma'),
(1007, 'Julia', 'Quinn'),
(1008, 'Alice', 'Oseman'),
(1009, 'Marianne','Curley'),
(1010, 'Han','Kang'),
(1011, 'Sophie', 'Kinsella'),
(1012, 'Rupi', 'Kaur');

-- Inserting data into the Books table
INSERT INTO Books (book_id, title, author_id, genre, publication_date, isbn, total_copies, available_copies) VALUES
(2001, 'Milk and Honey', 1012, 'Poetry', '2014-11-04', '1502784270', 3, 1),
(2002, 'Human Acts', 1010, 'Literary Fiction', '2014-05-19', '9781101906729', 1, 1),
(2003, 'The Vegetarian', 1010, 'Literary Fiction', '2007-10-30', '9781101906118', 4, 2),
(2004, 'The Undomestic Goddess', 1011, 'Chick Lit', '2005-07-19', '9780552772747', 1, 0),
(2005, 'You\'d Look Better as a Ghost', 1001, 'Mystery Thriller', '2023-09-21', '9781800811300', 2, 0),
(2006, 'Before and After', 1002, 'Sci Fi', '2020-01-08', '978-1677612154', 5, 4),
(2007, 'The Perfect Child', 1004, 'Mystery Thriller', '2019-03-01', '9781503960114', 2, 1),
(2008, 'Old Magic', 1009, 'Young Adult', '2000-01-01', '9780743437691', 1, 1),
(2009, 'Heartstopper: Volume One', 1008, 'Young Adult', '2018-01-01', '152722533X', 3, 0),
(2010, 'Heartstopper: Volume Four', 1008, 'Young Adult', '2021-05-06', '1338617567', 1, 1),
(2011, 'An Offer From a Gentleman : Bridgertons, #3', 1007, 'Historical Romance', '2001-07-01', '9780749936594', 4, 2),
(2012, 'To Sir Phillip, With Love : Bridgertons, #5', 1007, 'Historical Romance', '2003-01-01', '9780380820856', 4, 1),
(2013, 'The Secrets of Sir Richard Kenworthy : Smythe-Smith #4', 1007, 'Historical Romance', '2015-01-27', '0062072943', 1, 1),
(2014, 'The Housemaid', 1003, 'Mystery Thriller', '2022-04-26', '9781538742570', 1, 0);

-- Inserting data into the Members table
INSERT INTO Members (member_id, first_name, last_name, email, phone_number, membership_date) VALUES
(3010, 'Alice','Gallagher','alice.galla@live.ie', '07728488732', '2023-01-15'),
(3012, 'Charles', 'Henderson', 'charlieh@gmail.com', '01150243306', '2022-05-20'),
(3001, 'Freyr', 'Rosenberg', 'F.Rosen-berg@gmail.com', '07035095233', '2016-12-09'),
(3002, 'Iryna', 'Serrato', 'Irynie-Se@live.co.uk', '06943395345', '2020-11-10'),
(3009, 'Mollie', 'Yen', 'molli.pops@gmail.co.uk', '07907117889', '2018-09-09'),
(3008, 'Agatha', 'Rogers', 'A.Rogers@gmail.com', '05712372452', '2023-01-27'),
(3006, 'Michael', 'Poulos', 'MichaelPoulos@gmail.com', '09700529691', '2023-04-03'),
(3003, 'Steven', 'Hoffman', 'steven.Hman@gmail.co.uk', '07851683804', '2016-03-11'),
(3011, 'Miyo', 'To', 'ToMiyo-Mayo@live.ie', '07107110242', '2017-09-11'),
(3014, 'Lin', 'Ch\'ang', 'Lin.Cha.Ling@gmail.com', '08955616774', '2019-07-25');

-- Inserting data into the Loans table
INSERT INTO Loans (loan_id, book_id, member_id, loan_date, due_date, return_date, is_returned) VALUES
(1, 2001, 3010, '2024-07-07', '2024-07-21', NULL, FALSE),
(2, 2013, 3009, '2024-04-03', '2024-04-17', '2024-04-17', TRUE),
(3, 2006, 3003, '2024-04-29', '2024-05-13', NULL, FALSE),
(4, 2012, 3011, '2024-05-01', '2024-05-15', '2024-05-13', TRUE),
(5, 2011, 3011, '2024-01-26', '2024-02-08', '2024-02-10', TRUE),
(6, 2007, 3014, '2024-05-22', '2024-06-05', NULL, FALSE),
(7, 2005, 3011, '2024-05-18', '2024-06-01', NULL, FALSE),
(8, 2005, 3006, '2024-05-18', '2024-06-01', NULL, FALSE),
(9, 2002, 3003, '2024-03-16', '2024-03-30', '2024-03-25', TRUE),
(10, 2003, 3009, '2024-05-31', '2024-06-14', NULL, FALSE);

-- Inserting data into the Reservations table
INSERT INTO Reservations (reservation_id, book_id, member_id, reservation_date, res_status) VALUES
(1, 2005, 3010, '2024-06-03', 'Pending'),
(2, 2009, 3014, '2024-06-04', 'Pending'),
(3, 2009, 3009, '2024-01-12', 'Completed'),
(4, 2014, 3009, '2024-06-04', 'Pending'),
(5, 2012, 3011, '2024-05-01', 'Completed'),
(6, 2004, 3009, '2024-06-06', 'Pending'),
(7, 2001, 3003, '2024-04-23', 'Cancelled'),
(8, 2002, 3003, '2024-03-12', 'Completed'),
(9, 2001, 3012, '2024-06-05', 'Pending'),
(10, 2007, 3006, '2024-05-27', 'Cancelled');


-- STORED PROCEDURES


-- Stored Procedure that checks if members have over due books.
-- Based on this it prints a message showing if members can borrow books or not.
-- If they do have over due books, it will show the title of the over due book
-- as well as how many days over due the book is.
DELIMITER //
CREATE PROCEDURE CanBorrow(IN memberID INT)
BEGIN
	DECLARE overdueCount INT;

    -- Check for overdue books
    SELECT COUNT(*) INTO overdueCount
    FROM Loans
    WHERE member_id = memberID AND due_date < CURDATE() AND return_date IS NULL;

    IF overdueCount > 0 THEN
		-- Retrieve the overdue book details
        SELECT CONCAT('Sorry, you can not borrow any new books as "', Books.title, '" is ', DATEDIFF(CURDATE(), Loans.due_date), ' days overdue!') AS message
        FROM Loans
		JOIN Books on Loans.book_id = Books.book_id
		WHERE Loans.member_id = memberID AND Loans.due_date < CURDATE() AND Loans.return_date IS NULL;
	ELSE
		-- Allow user to borrow books
        SELECT "You are allowed to borrow new books." AS message;
	END IF;
END //
DELIMITER ;

-- CALL CanBorrow(3009);
-- Call CanBorrow(3010); -- member who can borrow
-- memberID's with over due books (3009, 3011, 3003, 3006, 3014)


-- Stored procedure to check the books in the reservations table.
-- This then print a message informing the member if the book is currently reserved or not.
-- If it is reserved it will check against the reservation dates and alert the user of their queue position
-- It will also check if the user already has a reservation for the book in the table and let them know,
-- It will not add them again if they already exist in the table for that book.
DELIMITER //

CREATE PROCEDURE AddToWaitList(IN bookID INT, IN memberID INT)
BEGIN
    DECLARE queue_position INT DEFAULT 0;
    DECLARE book_title VARCHAR(75);
    DECLARE res_count INT;
    DECLARE existing_res_date DATE;

    -- Check if the book exists
    SELECT COUNT(*) INTO res_count
    FROM Books
    WHERE book_id = bookID;

    IF res_count = 0 THEN
        SELECT CONCAT("Book ID ", bookID, " does not exist.") AS message;
    END IF;

    -- Get the book title
    SELECT title INTO book_title
    FROM Books
    WHERE book_id = bookID;

    -- Check if the member already has a pending reservation for the book
    SELECT reservation_date INTO existing_res_date
    FROM Reservations
    WHERE book_id = bookID AND member_id = memberID AND res_status = 'Pending'
    ORDER BY reservation_date ASC
    LIMIT 1;

    IF existing_res_date IS NOT NULL THEN
        -- Member already has an existing pending reservation for the book
        SET queue_position = (SELECT COUNT(*)
                              FROM Reservations
                              WHERE book_id = bookID AND reservation_date <= existing_res_date AND res_status = 'Pending');
        SELECT CONCAT("'", book_title, "' has already been reserved on ", DATE_FORMAT(existing_res_date, '%Y-%m-%d'), ". You are number ",
                      queue_position, " in the queue.") AS message;
    ELSE
        -- Insert a new reservation for the member
        INSERT INTO Reservations (book_id, member_id, reservation_date, res_status)
        VALUES (bookID, memberID, CURDATE(), 'Pending');

        -- Determine the queue position
        SET queue_position = (SELECT COUNT(*)
                              FROM Reservations
                              WHERE book_id = bookID AND res_status = 'Pending');

        -- Return the queue position to the member
        SELECT CONCAT("Adding you to the waitlist for '", book_title, "', you are number ", queue_position, " in the queue.") AS message;
    END IF;

END //

DELIMITER ;


-- Calling the AddToWaitlist Procedure
-- (book_id, member_id)
-- CALL AddToWaitlist(2014, 3010);

-- Stored procedure to check if a member has a loan that is not yet returned.
-- If there are no loans it will print an appropriate message.
-- If they do have a loan it will update the Loans table to
-- return the book and let the user know if it was successful or not.
-- It will also update the Books table available_copies + 1
DELIMITER //

CREATE PROCEDURE ReturnBook(IN bookID INT, memberID INT)
BEGIN
	DECLARE loanID INT;
    -- Check if the book is currently loaned by the member and not yet returned
    SELECT loan_id INTO loanID
    FROM Loans
    WHERE book_id = bookID AND member_id = memberID AND is_returned = FALSE
    LIMIT 1;

    -- If no such loan exists, show an appropriate message
    IF loanID IS NULL THEN
		SELECT CONCAT("No active loan found for this book ID ", bookID, " and member ID ", memberID, ".") AS message;
	ELSE
		-- Update the Loans table to mark the book as returned
        UPDATE Loans
        SET return_date = CURDATE(), is_returned = True
        WHERE loan_id = loanID;

        -- Increment the available copies in the books table
        UPDATE Books
        SET available_copies = available_copies + 1
        WHERE book_id = bookID;

        -- Return a success message
        SELECT CONCAT("Book ID ", bookID, " has been successfully returned by Member ID ", memberID, ".") AS message;
	END IF;
END //

DELIMITER ;

-- Call ReturnBook
-- CALL ReturnBook(2007, 3001);