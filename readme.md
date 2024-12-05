# Student Management System

An interactive Student Management System.
Student Management is a Python - based system, where users can perform CRUD (Create, Read, Update, Delete) operations on student data. This system is capable of saving and loading data from a text file, and a Database, use functions for operations, and employ classes for data management.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

python requirements are mrentioned [here](requirements.txt)


### Executing program
 - Install python and git
 - Clone repo
 - Navigate to repo
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


