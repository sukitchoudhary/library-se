# library-se
📚 Library Book Management System

Software Engineering Assignment – CS2042

📌 Project Overview

This project implements a Library Book Management System using Agile methodology, Git version control, and unit testing.
The system provides basic library operations such as registering books, borrowing books, returning books, and generating reports.

As per the assignment requirement, no database is used. All data is handled using in-memory data structures.

GitHub Repository Link:
https://github.com/sukitchoudhary/library-se

🛠️ Technologies Used

Python (Programming Language)

Git and GitHub (Version Control)

Python unittest framework (Testing)

Agile methodology (Sprint-based development)

🧠 Development Methodology (Agile Approach)

The project follows an Agile development approach, where the entire work was divided into multiple sprints.
Each sprint focused on a specific feature, followed by testing and version control updates.
This helped in developing the project incrementally and maintaining clarity at every stage.

🔁 Sprint-wise Execution Details
🟢 Sprint 1: Book Registration

Objective:
The goal of this sprint was to allow the librarian to register books in the system using a unique Book ID, book title, and author name.

Execution Details:

A Library class was created to manage all library operations.

A dictionary data structure was used to store book details.

Validation logic was added to ensure that no two books share the same Book ID.

Proper error handling was implemented for duplicate entries.

Testing:
Unit tests were written to verify:

Successful registration of a new book

Rejection of duplicate Book IDs

Version Control:
All Sprint-1 related changes were committed to a separate branch, merged into the main branch after testing, and tagged as the first version.

🟡 Sprint 2: Borrowing and Returning Books

Objective:
The purpose of this sprint was to manage the borrowing and returning of books while maintaining correct availability status.

Execution Details:

Borrow functionality was added to allow issuing books only if they are available.

Return functionality was implemented to mark borrowed books as available again.

Business rules were enforced to prevent invalid operations such as borrowing an already borrowed book.

Exception handling was used to handle incorrect actions gracefully.

Testing:
Unit tests validated:

Successful borrowing of available books

Prevention of borrowing unavailable books

Correct return of borrowed books

Version Control:
Sprint-2 changes were developed in a separate branch, merged after successful testing, and tagged as the second version.

🔵 Sprint 3: Library Report Generation

Objective:
The objective of this sprint was to generate a report displaying all books along with their availability status.

Execution Details:

A report generation feature was implemented.

The report displays Book ID, title, author, and current status.

The report provides a clear overview of the library inventory.

Testing:
Unit tests ensured:

Correct formatting of the report

Accurate display of all book records

Version Control:
Sprint-3 changes were committed, merged, and tagged as the final version of the project.

🧪 Testing Strategy

Testing was performed using Python’s built-in unit testing framework.
Test cases were written for every sprint to validate both normal functionality and error conditions.
All tests were executed successfully, ensuring the reliability of the system.

🔗 Requirement Traceability
Sprint	User Story	Implementation	Test Case	Version Tag
Sprint 1	Register books	Book registration logic	Add book test	v0.1
Sprint 2	Borrow book	Borrow functionality	Borrow book test	v0.2
Sprint 2	Return book	Return functionality	Return book test	v0.2
Sprint 3	Generate report	Report generation	Report test	v0.3
🔀 Git Version Control Strategy

Separate branches were used for each sprint

Changes were merged only after testing

Version tags were created for every sprint

Clear commit messages were maintained

This strategy ensured traceability, clean history, and safe development.

📌 Project Outcome

All required features were successfully implemented

Agile methodology was properly followed

Unit testing ensured correctness

Git provided complete traceability

🎓 Conclusion

This project demonstrates the practical application of software engineering principles such as Agile development, version control, testing, and traceability.
The assignment helped in understanding how structured processes improve software quality and maintainability.
