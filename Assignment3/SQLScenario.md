# Assignment 3 - SQL


## Scenario
"I want to help my employer to better manage how internal staff interact with our online learning platform. 
I want to make the systems more efficient to use. To achieve this, I'll design a database
system to manage courses, student enrollments, assessments, results and payments seamlessly."

## Database Design and Implementation:

### Instructors:
I will create an 'Instructors' table, which will include instructor_id, first_name, last_name, a short bio, email and phone_number. I will associate `PRIMARY KEY` to instructor_id
to be able to link it to other tables. I will make use of `VARCHAR` and `TEXT` where appropriate. I will also use `UNIQUE` on the email column to ensure all emails are unique to instructors.
I will also make use of `NOT NULL` in the first_name and last_name columns.

### Courses Management: 
I will create a comprehensive 'Courses' table that includes details such as course_id, title of each course, as well as a short description of said course. 
Other columns included will be  price(`DECIMAL(6,2)` and `NOT NULL`), duration, and the instructor responsible (This will be a `FOREIGN KEY` in this table and reference the Instructors table). 

### Student Tracking: 
I will implement a 'Students' table to track student demographics. This will include student_id(`INT` and `PRIMARY KEY`) first_name (`VARCHAR()` and `NOT NULL`), last_name(`VARCHAR()` and `NOT NULL`).
As well as email addresses(`UNIQUE`), phone numbers, and dob(`DATE`). 
To maintain data integrity, triggers will be set up to validate date of birth entries, preventing future dates from being entered.

### Enrollment Management: 
I will set up an 'Enrollments' table to manage student enrollment in courses. 
This will include enrollment_id (`AUTO_INCREMENT`), student_id, course_id, instructor_id, and enrollment date. 
Each enrollment will be linked to the respective student, course and instructor through (`FOREIGN KEY`) for easy tracking.

### Assessments and Results: 
I will design an 'Assessments' table to schedule exams and assignments for each course. 
It will store assessment_id (`AUTO_INCREMENT`), course_id, title of the course, description of the course, total_marks students could obtain, and the assessment date. 
Results will be tracked in a 'Results' table with result_id (`AUTO_INCREMENT`), assessment_id, student_id, marks obtained, date of being marked, and feedback gained.

### Payments Tracking: 
I will create a 'Payments' table to handle student payments for courses. 
This table will include payment_id, student_id, enrollment date, course_id, 'title' of the course, price.
payment type will be `ENUM` to only take in a predefined set of values.
('pay in full', '2 month plan', '3 month plan') payment status will also be `ENUM`('paid in full', '1st installment paid', '2nd installment paid', 'final installment paid', 'awaiting payment'). 
This ensures transparency and accurate financial tracking.

## Retrieval Queries:

I will write queries to compile a list of courses, retrieve students enrolled in bootcamps, get details on specific courses as well as their results. 


I will use `AGGREGATE` functions like `COUNT()` and `AVG()` to show statistics such as course popularity based on enrollment counts. 
As well as summaries showing the average marks received from the learning platform.

JOINS will be used to generate reports on instructor information for all courses as well as assessment results for all students. 

I will make use of `TIMESTAMPDIFF()` and `CURDATE()`.
This will be used to get student ages ordered from oldest to youngest.
I will also use `CONCAT()` and `FORMAT()` in order to format course prices for easier reading.

I will simulate making a mistake within the course duration table and use UPDATE to correct it.
I will also generate reports on outstanding course payments, in order to do this I will have to ALTER the payments table.
Then `MODIFY` the payment_status column which is set as ENUM to take in a 'late on payment' status. 

I will simulate a situation where a course is added to the database without an appropriate instructor to teach said course.
I will then give the option to delete the entry using either the course_id or where the instructor_id IS NULL.

## Stored Procedure:

My stored procedure will be used to issue certificates to students who have completed their courses. 
In order to do this I will need to create a new table to store certificates. 
It generates certificates using data from other tables like student_id and course_id.
Then saves the newly generated certificates into the Certificate table.
I will provide some data entries that demonstrate successful results of this stored procedure.


I will generate a report that will make it easier to check student certificate statuses.
This will use `IF`, `INTERVAL`, and `WEEK` to check the `CURDATE` against the duration the course and students enrollment dates.
It will then mark the course_status as 'Ongoing' or 'Completed'.
Using `CASE`, `WHEN` and `WHEN EXISTS` I will check in the Certificates table to see if a certificate has been issued to all students.
If not I will make use of THEN and ELSE to set the certificate_status to 'Certificate Issued' or 'Certificate Pending'
This report will be `ORDER BY` students.last_names.

