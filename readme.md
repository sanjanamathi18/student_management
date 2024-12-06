# Student Management System

An interactive Student Management System.
Student Management is a Python - based system, where users can perform CRUD (Create, Read, Update, Delete) operations on student data. This system is capable of saving and loading data from a text file, and a Database, use functions for operations, and employ classes for data management.

## Description

The purpose of this project is to create a robust and user-friendly system that simplifies student information management. 

It is designed to:

Streamline Operations: Provide easy-to-use functions for creating, reading, updating, and deleting student records.

Ensure Data Persistence: Support data saving and loading, enabling users to store records in a text file or a database.

Demonstrate Programming Concepts: Showcase practical implementation of Python programming, including:
Object-Oriented Programming (OOP) for managing data using classes.File handling for saving and retrieving records.
Database integration for scalable and secure data storage.

This system is ideal for learning purposes, small-scale implementations in schools or tuition centers, or as a foundational component for larger projects.

## Getting Started

### Dependencies

Python requirements are mentioned [here](requirements.txt)

### Executing program
1. Clone or download the repository.
2. Ensure Python is installed on your system.
3. Install necessary dependencies (e.g., SQLite library, if using SQLite).
4. Run the "student_management.py" file to start the application.
Follow the interactive prompts to manage student records.

 - Run following command
 ```  
 python3 student_management.py
```
Note:
- recommendation is to use virtual environment and install the dependencies

### Design

Follow the flow of operations as described below:

1. **Start**
1. Display Menu¨
1. Input User Choice
1. Validate Input
    - if input is valid, proceed
    - if invalid,show an error and loop back to input.
1. Based on the choice:
    - **Choice 1**: Add Student
    - **Choice 2**: View All Students
    - **Choice 3**: Update Student
        - Check if ID exists.
            - If yes, update student details.
            - If no, display "ID doesn't exist."
    - **Choice 4**: Delete Student
    - Check if ID exists.
        - If yes, delete the student.
        - If no, display "ID doesn't exist."
    - **Choice 5**: Save and Exit




## Help

Any advise for common problems or issues.

For package installing issue
```
python3 -m venv .venv

source .ven/bin/activate

pip install flask

```


## Authors

Sanjana Mathiyalagan
 
@Sanjana Mathi [https://github.com/sanjanamathi18]

## Version History
* 1.0 
    * Introduction of web based input

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() 
* 0.1
    * Initial Release - Working prototype


