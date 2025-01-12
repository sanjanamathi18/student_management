# Student Management System

An interactive Student Management System.
Student Management is a Python - based system, where users can perform CRUD (Create, Read, Update, Delete) operations on student data. This system is capable of saving and loading data from a text file, use functions for operations, and employ classes for data management.

## Description

The purpose of this project is to create a robust and user-friendly system that simplifies student information management. 

It is designed to:

Streamline Operations: Provide easy-to-use functions for creating, reading, updating, and deleting student records.

Ensure Data Persistence: Support data saving and loading, enabling users to store records in a text file.

Demonstrate Programming Concepts: Showcase practical implementation of Python programming, including:
Object-Oriented Programming (OOP) for managing data using classes.File handling for saving and retrieving records.

This system is ideal for learning purposes, small-scale implementations in schools or tuition centers, or as a foundational component for larger projects.

## Getting Started


### Executing program
1. Clone or download the repository:
   ```bash
   git clone https://github.com/sanjanamathi18/student_management.git
   ```
2. Ensure Python is installed on your system.

3. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
  
   ```

4. Run the "student_management.py" file to start the application.
Follow the interactive prompts to manage student records.

 - Run following command
 ```  
 python3 student_management.py
```

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

```
python3 -m venv .venv

source .ven/bin/activate

```

## Authors

Sanjana Mathiyalagan
 
@Sanjana Mathi [https://github.com/sanjanamathi18]

## Version History
* 1.0 
    * Test cases for CRUD

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() 
* 0.1
    * Initial Release - Working prototype
