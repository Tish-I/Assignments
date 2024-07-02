-- Create a Database for an online learning provider
CREATE DATABASE online_learning_platform;
USE online_learning_platform;

-- Creating tables and populating them with relevant data

-- Create the Instructors table
CREATE TABLE Instructors (
instructor_id INT PRIMARY KEY,
first_name VARCHAR(25) NOT NULL,
last_name VARCHAR(25) NOT NULL,
bio TEXT,
email VARCHAR(100) UNIQUE,
phone_number VARCHAR(11)
);

-- Insert into the instructors table
INSERT INTO Instructors (instructor_id, first_name, last_name, bio, email, phone_number) VALUES
(9001, 'Jane', 'Plumbob', 'Expert in Computer Sciences', 'JaniePlumb@gmail.com', '04157714833'),
(9010, 'Shana', 'Roach', 'Digital Marketing expert', 'S.Roach@live.ie', '04715442648'),
(9002, 'Norman', 'Bates', 'Professional Graphic Designer', 'normanbates@gmail.com', '02982944275'),
(9008, 'Luther', 'McAvoy', 'Expert in Computer Sciences', 'LMcAvoy@gmail.co.uk', '09593698907'),
(9003, 'Carlene', 'Webb', 'Cerified public Accountant', 'leneWebb@gmail.com', '04941876501'),
(9004, 'Noah', 'Buckley', 'Web Development Specialist', 'Buckley_noah@gmail.ie', '06519841812'),
(9006, 'Allyson', 'Durham', 'Professional Graphic Designer', 'Ally_Durham@gmail.co.uk', '09953354405'),
(9009, 'Leah', 'Lamb', 'Expert in Cyber Security', 'LL_lamb@gmail.com', '04374119528'),
(9005, 'Mike', 'Bishops', 'Project Mangement Professional', 'Mike.Bishops@gmail.com', '02733645944'),
(9007, 'Madeleiene', 'Bishops', 'Financial Analyst Expert', 'Made_lei.bishops@gmail.com', '03228786322');

-- Create the Courses table
CREATE TABLE Courses (
course_id INT PRIMARY KEY,
title VARCHAR(100) NOT NULL,
description TEXT,
price DECIMAL(6,2) NOT NULL,
duration VARCHAR(15) NOT NULL,
instructor_id INT,
FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

-- Insert into the courses table
INSERT INTO Courses (course_id, title, description, price, duration, instructor_id) VALUES
(8002, 'Data Science and Machine Learning', 'Advanced course', 1200.00, '12 week course', 9001),
(8004, 'Graphic Design for Beginners', 'Intro course to Graphic Designing', 300.00, '6 weeks', 9002),
(8006, 'Financial Accounting Basics', 'Basic concepts of Financial Accounting', 400.00, '8 weeks', 9003),
(8008, 'Digital Marketing Fundamentals', 'Refreasher course on Digital Marketing', 500.00, '8 weeks', 9010),
(8010, 'Web Development Bootcamp', 'Bootcamp covering you\ll need to be a Web Developer', 1500.00, '16 weeks', 9004),
(8012, 'Intro to Cybersecurity', 'Basic concepts of Cybersecurity', 500.00, '8 weeks', 9009),
(8014, 'Graphic Design Bootcamp', 'Learn Graphic Design from scratch', 1000.00, '12 weeks', 9006),
(8016, 'Project Mangagement Bootcamp', 'Bootcamp covering everything you\'ll need to be a Project Manager', 1500.00, '10 weeks', 9005),
(8018, '(PMP) Certification Prep', 'Prepare for the PMP exam with this course', 400.00, '2 weeks', 9005),
(8020, 'Intro to Graphic Design', 'Basic concepts of Graphic Design', 500.00, '8 weeks', 9002);

-- Simulating a scenario where course is entered without an appropriate instructor being hired, then deleting the course
-- Inserting a course without an instrustor
INSERT INTO Courses (course_id, title, description, price, duration) Values
(8022, 'SQL Fundamentals', 'Basic fundamentals of SQL', 300.00, '2 weeks');
-- Checking it exits in the table
 SELECT * FROM Courses ORDER BY title;
-- Deleting the SQL course
-- Delete by course_id
-- DELETE FROM Courses WHERE course_id = 8022;
-- Delete using NULL
-- DELETE FROM Courses WHERE instructor_id IS NULL;

-- Create a Students table
CREATE TABLE Students (
student_id INT PRIMARY KEY,
first_name VARCHAR(25) NOT NULL,
last_name VARCHAR(25) NOT NULL,
email VARCHAR(100) UNIQUE,
phone_number VARCHAR(11),
dob DATE
);

-- Adding  triggers
-- Before populating the students table, adding a trigger to ensure that dob's are all after the current date
-- This ensures that only valid dob dates will be entered.

-- Step 1: Change the delimiter
DELIMITER //

-- Step 2: Create a BEFORE INSERT trigger
CREATE TRIGGER before_insert_students
BEFORE INSERT ON Students
FOR EACH ROW
BEGIN
	IF NEW.dob >= CURDATE() THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'dob must be before the current date';
	END IF;
END;
//

-- Step 3: Create a BEFORE UPDATE trigger
CREATE TRIGGER before_update_students
BEFORE UPDATE ON Students
FOR EACH ROW
BEGIN
	IF NEW.dob >= CURDATE() THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'dob must be before the current date';
	END IF;
END;
//

-- Step 4: Reset the delimiter
DELIMITER ;

-- Populate the students table
INSERT INTO Students (student_id, first_name, last_name, email, phone_number, dob) VALUES
(1005, 'Allison', 'Polin', 'Polin_Allie@gmail.com', '07820163045', '1994-08-23'),
(1001, 'Charlize', 'Stewart', 'Charlize.Ste@yahoo.com', '07073437986', '1997-01-19'),
(1004, 'James', 'Mason', 'Mason106@hotmail.com', '07448672067', '1953-11-20'),
(1002, 'Charles', 'Adams', 'Adam.Adams@gmail.co.uk', '07663937152', '1986-04-25'),
(1020, 'Betsy', 'Hauck', 'HukleBets_berry@gmail.com', '07007858287', '1961-01-02'),
(1003, 'James', 'Feild', 'Feildday01.James@yahoo.com', '07920036172', '1972-01-14'),
(1018, 'Edwin', 'Wolf', 'Ed_Wolf@yahoo.com', '07163701056', '1960-02-02'),
(1014, 'Jamie', 'Williamson', 'Jay_Jamie@yahoo.com', '07838556408', '1994-04-02'),
(1006, 'Amiya', 'Gupta', 'AmiyaGupta@yahoo.com', '07458630230', '1947-05-21'),
(1007, 'Lee', 'Stokes', 'stokes.lee@hotmail.com', '07196978251', '1970-09-10'),
(1008, 'Amar', 'Gupta', 'AmGu.Amar@gmail.co.uk', '07440465286', '2004-10-20'),
(1009, 'Amar', 'Singh', 'amar_sing@hotmail.com', '07499663528', '1989-09-06'),
(1011, 'Thomas', 'Carr', 'tommie.Carr@hotmail.com', '07734696785', '2006-07-15'),
(1010, 'Alfie', 'Carr', 'Car_Alp99@hotmail.com', '07944411677', '1982-07-17'),
(1012, 'Georgina', 'Coombes', 'GeorgiNaCoo@gmail.com', '07419624740', '1999-09-21'),
(1013, 'Amelia', 'Trent', 'ami.Amelia_T@gmail.co.uk', '07211400122', '1976-07-16'),
(1015, 'Jack', 'Carr', 'Jack_jack27@gmail.com', '07795644202', '1969-04-14'),
(1016, 'Mia', 'Coombes', 'Mia.Coombes@gmail.co.uk', '07896659155', '1981-03-02'),
(1017, 'Indi', 'Singh', 'indi_Singheray@yahoo.com', '07856617883', '1991-09-24'),
(1019, 'Freya', 'Polin', 'Frey_bells66@gmail.com', '07822273718', '1980-11-15');

-- Back to creating Tables

-- Create an Enrollments table
CREATE TABLE Enrollments (
enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
course_id INT,
instructor_id INT,
enrollment_date DATE,
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id),
FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

-- Populate Enrollments table
INSERT INTO Enrollments (student_id, course_id, instructor_id, enrollment_date) VALUES
(1005, 8002, 9001, '2024-04-01'), 
(1001, 8004, 9002, '2024-01-02'),
(1004, 8006, 9003, '2024-02-03'),
(1002, 8008, 9010, '2024-01-04'),
(1020, 8010, 9004, '2024-05-05'),
(1003, 8012, 9009, '2024-01-06'),
(1018, 8014, 9006, '2024-04-07'),
(1014, 8016, 9005, '2024-01-08'),
(1006, 8018, 9005, '2024-05-09'), 
(1007, 8020, 9002, '2024-01-10'),
(1008, 8002, 9001, '2024-01-11'),
(1009, 8004, 9002, '2024-01-12'),
(1011, 8006, 9003, '2024-01-13'),
(1010, 8008, 9010, '2024-01-14'),
(1012, 8010, 9004, '2024-01-15'),
(1013, 8012, 9009, '2024-01-16'),
(1015, 8014, 9006, '2024-01-17'),
(1016, 8016, 9005, '2024-01-18'),
(1017, 8018, 9005, '2024-01-19'),
(1019, 8020, 9002, '2024-01-20'),
(1005, 8004, 9002, '2024-03-02'),
(1001, 8010, 9004, '2024-04-01'),
(1004, 8002, 9001, '2024-01-01'),
(1020, 8012, 9009, '2024-05-10'), 
(1003, 8014, 9006, '2024-04-15');


-- Create an Assessments table
CREATE TABLE Assessments (
assessment_id INT AUTO_INCREMENT PRIMARY KEY,
course_id INT,
title VARCHAR(100) NOT NULL,
description TEXT,
total_marks INT NOT NULL,
assessment_date DATE,
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Insert into the assessments table
INSERT INTO Assessments (course_id, title, description, total_marks, assessment_date) VALUES
(8002, 'Final Exam', 'Assessment on key topics covered in Data Science and Machine Learning', 100, '2024-05-15'),
(8004, 'Final Design Project', 'Create a graphic design portfolio', 100, '2024-03-20'),
(8006, 'Financial Accounting Test', 'Test on basic concepts of Financial Accounting', 100, '2024-03-18'),
(8008, 'Marketing Strategy Presentation', 'Present a comprehensive digital marketing strategy', 100, '2024-03-22'),
(8010, 'Final Web Project', 'Develop a full-stack web application', 200, '2024-06-25'),
(8012, 'Cybersecurity Practical Exam', 'Practical assessment on cybersecurity concepts', 100, '2024-02-19'),
(8014, 'Design Showcase', 'Showcase your graphic design work', 150, '2024-06-21'),
(8016, 'Project Management Simulation', 'Simulate a project management scenario', 100, '2024-04-24'),
(8018, 'PMP Mock Exam', 'Mock exam to prepare for PMP certification', 100, '2024-05-23'),
(8020, 'Graphic Design Assignment', 'Basic assignment on graphic design principles', 50, '2024-01-17');

-- Create a Results table
CREATE TABLE Results (
result_id INT AUTO_INCREMENT PRIMARY KEY,
assessment_id INT,
student_id INT,
marks_obtained INT,
mark_date DATE,
feedback TEXT,
FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id),
FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Inserting into Results 
INSERT INTO Results (assessment_id, student_id, marks_obtained, mark_date, feedback) VALUES
(8, 1016, 99, '2024-04-25', 'Very good simulation results'),
(6, 1003, 80, '2024-02-20', 'Good practical skills'), 
(3, 1011, 79, '2024-03-19', 'Decent accounting knowledge'),
(1, 1008, 82, '2024-05-16', 'Good effort on the exam'), 
(9, 1006, 99, '2024-05-24', 'Well-prepared for PMP exam'), 
(4, 1002, 88, '2024-03-23', 'Very comprehensive strategy'),  
(10, 1007, 40, '2024-01-18', 'Basic understanding of design principles'), 
(3, 1004, 98, '2024-03-19', 'Solid grasp of accounting basics'), 
(9, 1017, 88, '2024-05-24', 'Well-prepared and confident'), 
(2, 1009, 87, '2024-03-21', 'Creative portfolio design'), 
(4, 1010, 84, '2024-03-23', 'Strategic and detailed presentation'), 
(1, 1005, 85, '2024-05-16', 'Good understanding of concepts'), 
(8, 1014, 100, '2024-04-25', 'Excellent project management simulation'), 
(2, 1001, 90, '2024-03-21', 'Excellent design skills'), 
(10, 1019, 45, '2024-01-18', 'Needs improvement in basic design principles'), 
(6, 1013, 77, '2024-02-20', 'Good practical understanding');

-- Create a payment table
CREATE TABLE Payments(
payment_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
enrollment_date DATE,
course_id INT,
title VARCHAR(100) NOT NULL,
price DECIMAL(6,2) NOT NULL,
payment_type ENUM('pay in full', '2 month plan', '3 month plan') NOT NULL,
payment_status ENUM('paid in full', '1st installment paid', '2nd installment paid', 'final installment paid', 'awaiting payment') NOT NULL,
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Populate the payments table with data
INSERT INTO Payments (student_id, enrollment_date, course_id, title, price, payment_type, payment_status) VALUES
(1005, '2024-04-01', 8002, 'Advanced Mathematics', 300.00, 'pay in full', 'paid in full'),
(1001, '2024-01-02', 8004, 'History 101', 150.00, 'pay in full', 'paid in full'),
(1004, '2024-02-03', 8006, 'Physics Basics', 200.00, '2 month plan', '1st installment paid'),
(1002, '2024-01-04', 8008, 'Chemistry Intro', 250.00, '3 month plan', '2nd installment paid'),
(1020, '2024-05-05', 8010, 'Biology Fundamentals', 180.00, 'pay in full', 'awaiting payment'),
(1003, '2024-01-06', 8012, 'English Literature', 150.00, 'pay in full', 'paid in full'),
(1018, '2024-04-07', 8014, 'Computer Science', 300.00, 'pay in full', 'paid in full'),
(1014, '2024-01-08', 8016, 'Art History', 100.00, '2 month plan', 'awaiting payment'),
(1006, '2024-05-09', 8018, 'Music Theory', 120.00, '3 month plan', '1st installment paid'),
(1007, '2024-01-10', 8020, 'Philosophy 101', 150.00, 'pay in full', 'paid in full'),
(1008, '2024-01-11', 8002, 'Advanced Mathematics', 300.00, 'pay in full', 'paid in full'),
(1009, '2024-01-12', 8004, 'History 101', 150.00, 'pay in full', 'paid in full'),
(1011, '2024-01-13', 8006, 'Physics Basics', 200.00, '2 month plan', '1st installment paid'),
(1010, '2024-01-14', 8008, 'Chemistry Intro', 250.00, '3 month plan', '2nd installment paid'),
(1012, '2024-01-15', 8010, 'Biology Fundamentals', 180.00, 'pay in full', 'paid in full'),
(1013, '2024-01-16', 8012, 'English Literature', 150.00, 'pay in full', 'paid in full'),
(1015, '2024-01-17', 8014, 'Computer Science', 300.00, 'pay in full', 'awaiting payment'),
(1016, '2024-01-18', 8016, 'Art History', 100.00, '2 month plan', 'awaiting payment'),
(1017, '2024-01-19', 8018, 'Music Theory', 120.00, '3 month plan', '2nd installment paid'),
(1019, '2024-01-20', 8020, 'Philosophy 101', 150.00, 'pay in full', 'paid in full'),
(1005, '2024-03-02', 8004, 'History 101', 150.00, 'pay in full', 'paid in full'),
(1001, '2024-04-01', 8010, 'Biology Fundamentals', 180.00, 'pay in full', 'awaiting payment'),
(1004, '2024-01-01', 8002, 'Advanced Mathematics', 300.00, 'pay in full', 'paid in full'),
(1020, '2024-05-10', 8012, 'English Literature', 150.00, '2 month plan', 'awaiting payment'),
(1003, '2024-04-15', 8014, 'Computer Science', 300.00, 'pay in full', 'paid in full');

-- Retrievals 
-- retrieve all courses ordered by duration of the course using CAST to ensure that duration is sorted numerically
SELECT * FROM Courses ORDER BY CAST(duration AS UNSIGNED);

-- retrieve students enrolled in bootcamps using LIKE '%' and ordered by student_id
SELECT DISTINCT s.student_id, s.first_name, s.last_name, c.title AS course_title
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.title LIKE '%Bootcamp%'
ORDER BY s.student_id;

-- retrieve assessment details for 'Intro to Cybersecurity'
SELECT a.assessment_id, a.title, a.description, a.total_marks, a.assessment_date
FROM Assessments a
JOIN Courses c ON a.course_id = c.course_id
WHERE c.title = 'Intro to Cybersecurity';

-- retrieve student results for 'Data Science and Machine Learning' ordered by marks in descending order
SELECT r.result_id, s.first_name, s.last_name, c.title AS course_title, a.title AS assessment_title, r.marks_obtained, r.mark_date, r.feedback
FROM Results r
JOIN Assessments a ON r.assessment_id = a.assessment_id
JOIN Courses c ON a.course_id = c.course_id
JOIN Students s ON r.student_id = s.student_id
WHERE c.title = 'Data Science and Machine Learning'
ORDER BY r.marks_obtained DESC;

-- retrieve contact info for all instructors ordered by last_name
SELECT last_name, email, phone_number
FROM Instructors
ORDER BY last_name;

-- Aggregate functions
-- using COUNT() to retrieve the total number of students enrolled in each course
SELECT c.course_id, c.title AS course_title, COUNT(e.student_id) AS total_students_enrolled
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.title
ORDER BY c.course_id;

-- using AVG() to calculate average marks obtained in all assessments
SELECT AVG(r.marks_obtained) AS average_marks_obtained
FROM Results r;

-- Joins
-- retrieve instructor infomation for each course
SELECT 
	c.course_id,
    c.title AS course_title,
    CONCAT(i.first_name, ' ', i.last_name) AS instructor_name,
    i.email AS instructor_email,
    i.phone_number AS instructor_phone
FROM
	Courses c
JOIN
	Instructors i ON c.instructor_id = i.instructor_id
ORDER BY
	c.course_id;

-- retrieve assessment results, courses and student details
SELECT 
    r.result_id,
    c.title AS course_title,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    a.title AS assessment_title,
    r.marks_obtained,
    r.mark_date,
    r.feedback
FROM
    Results r
JOIN
    Assessments a ON r.assessment_id = a.assessment_id
JOIN
    Courses c ON a.course_id = c.course_id
JOIN
    Students s ON r.student_id = s.student_id
ORDER BY
    r.result_id;

-- Additional functions
-- Using TIMESTAMPDIFF and CURDATE() to retrieve student ages
SELECT
	student_id,
    first_name,
    last_name,
    dob,
    TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age
FROM
	Students
ORDER BY
	age DESC;
    
-- Using CONCAT() and FORMAT() to format the prices in the course table
SELECT
	course_id,
    title,
    description,
    CONCAT('£', FORMAT(price, 2)) AS formatted_price,
    duration,
    instructor_id
FROM
	Courses
ORDER BY 
	price;
 
-- Comment the following in order to update entries

-- Updating data science to say '12 weeks' instead of '12 week course'
-- UPDATE Courses SET duration = '12 weeks' WHERE title = 'Data Science and Machine Learning'


-- Update late payments
-- First alter Payments table to take in another ENUM statement
--  ALTER TABLE Payments
--  MODIFY COLUMN payment_status ENUM('paid in full', '1st installment paid', '2nd installment paid', 'final installment paid', 'awaiting payment', 'late on payment') NOT NULL;

-- Update late payments where enrollment_date is 30 days or more in the past
--  UPDATE Payments
--  SET payment_status = 'late on payment'
--  WHERE DATEDIFF(CURDATE(), enrollment_date) >= 30
--    AND payment_status <> 'paid in full'
--    LIMIT 4; -- limits the changed data to 4 entries

-- retrieve all payment information ordered by their payment status
SELECT * FROM Payments ORDER BY payment_status;
 
-- STORED Procedure to issue certificates
-- First create a Certicates table
CREATE TABLE Certificates (
certificate_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
course_id INT,
cert_text TEXT,
issue_date DATE,
UNIQUE KEY unique_certs (student_id, course_id),
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE GenerateCourseCompletionCert (
IN p_student_id INT,
IN p_course_id INT,
IN p_completion_date DATE
)
BEGIN
	DECLARE v_student_name VARCHAR(25);
    DECLARE v_course_title VARCHAR(100);
    DECLARE v_cert_text TEXT;
    
-- Retrieve student name and check if it exists
	SELECT CONCAT(first_name, ' ', last_name) INTO v_student_name
	FROM Students
	WHERE student_id = p_student_id;
    
    IF v_student_name IS NULL THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid student_id provided.';
	END IF;

-- Retrieve course title and check it exists
	SELECT title INTO v_course_title
	FROM Courses
	WHERE course_id = p_course_id;
    
    IF v_course_title IS NULL THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid course_id provided.';
	END IF;

-- Prep certificate text
	SET v_cert_text = CONCAT(
		'Certificate of Completion\n\n',
		'This certifies that ', v_student_name, ' has successfully completed the course:\n',
		v_course_title, '\n\n',
		'Completion Date: ', DATE_FORMAT(p_completion_date, '%M-%d-%Y'), '\n\n',
		'Issued on: ', DATE_FORMAT(NOW(), '%M-%d-%Y')
	);

-- Insert the certificates into a table
	INSERT INTO Certificates (student_id, course_id, cert_text, issue_date) VAlUES
    (p_student_id, p_course_id, v_cert_text, NOW());

-- Return and display the certificate text
	SELECT v_cert_text AS course_completion_certificate;
END //

DELIMITER ;

-- Uncomment to run calling the procedure with parameters
-- CALL GenerateCourseCompletionCert();
-- call the procedure using any of these provided values
-- 1010, 8008, '2024-06-11'
-- 1015, 8014, '2024-05-29'
-- 1016, 8016, '2024-06-01'
-- 1008, 8002, '2024-05-20'

-- Populating the Certificates table with 8 rows of data
-- Insert data into Certificates table
INSERT INTO Certificates (student_id, course_id, cert_text, issue_date) VALUES
(1005, 8002, 'Certificate of Completion\n\nThis certifies that Allison Polin has successfully completed the course: Data Science and Machine Learning\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13'),
(1001, 8004, 'Certificate of Completion\n\nThis certifies that Charlize Stewart has successfully completed the course: Graphic Design for Beginners\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13'),
(1004, 8006, 'Certificate of Completion\n\nThis certifies that James Mason has successfully completed the course: Financial Accounting Basics\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13'),
(1002, 8008, 'Certificate of Completion\n\nThis certifies that Charles Adams has successfully completed the course: Digital Marketing Fundamentals\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13'),
(1020, 8010, 'Certificate of Completion\n\nThis certifies that Betsy Hauck has successfully completed the course: Web Development Bootcamp\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13'),
(1003, 8012, 'Certificate of Completion\n\nThis certifies that James Feild has successfully completed the course: Intro to Cybersecurity\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13'),
(1018, 8014, 'Certificate of Completion\n\nThis certifies that Edwin Wolf has successfully completed the course: Graphic Design Bootcamp\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13'),
(1014, 8016, 'Certificate of Completion\n\nThis certifies that Jamie Williamson has successfully completed the course: Project Management Bootcamp\n\nCompletion Date: May-29-2024\n\nIssued on: June-13-2024', '2024-06-13');

-- Retrieval query to check certifate status' ordered by students last_name
SELECT
	s.student_id,
    s.last_name,
    s.first_name,
    c.course_id,
    c.title AS course_title,
    e.enrollment_date,
    c.duration,
    IF(e.enrollment_date + INTERVAL c.duration WEEK >= CURDATE(), 'Ongoing', 'Completed') AS course_status,
    CASE
        WHEN e.enrollment_date + INTERVAL c.duration WEEK >= CURDATE() THEN NULL
        WHEN EXISTS (
            SELECT 1
            FROM Certificates cert
            WHERE cert.student_id = e.student_id
            AND cert.course_id = e.course_id
        ) THEN 'Certificate Issued'
        ELSE 'Certificate Pending'
    END AS certificate_status
FROM
    Courses c
JOIN
    Enrollments e ON c.course_id = e.course_id
JOIN
    Students s ON e.student_id = s.student_id
ORDER BY
    s.last_name;

