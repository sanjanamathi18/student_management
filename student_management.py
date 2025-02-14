import json
from typing import List, Dict


def test_print(message: str):
    print(message)


def validate_string(message: str):
    if len(message) == 0:
        return False
    for n in message:
        if not ((65 <= ord(n) <= 90) or (97 <= ord(n) <= 122)):
            return False
    return True


class Student:
    def __init__(
        self, id: int = 0, name: str = "", age: int = 0, grade: str = "", subjects: List[str] = []
    ):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def to_dict(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Age": self.age,
            "Grade": self.grade,
            "Subjects": self.subjects,
        }

    def to_string(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Subjects: {', '.join(self.subjects)}"


class StudentManager:
    def __init__(self, file_name):
        self.student_list: Dict[int, Student] = {}
        self.file_name = file_name
        self.load_students()

    def add_students(self, student: Student):
        self.student_list[student.id] = student

    def view_all_students(self):
        for student in self.student_list.values():
            test_print(student.to_string())

    def update_name(self, id: int, name: str):
        self.student_list[id].name = name

    def update_age(self, id: int, age: int):
        self.student_list[id].age = age

    def update_grade(self, id: int, grade: str):
        self.student_list[id].grade = grade

    def update_subjects(self, id: int, subjects: List[str]):
        self.student_list[id].subjects = subjects

    def delete_student(self, id: int):
        self.student_list.pop(id)

    def save_students(self):
        with open(self.file_name, "w") as writefile:
            students = {}
            for id, student in self.student_list.items():
                students[id] = student.to_dict()
            json.dump(students, writefile, indent=4)

    def load_students(self):
        self.student_list = {}
        try:
            with open(self.file_name, "r") as outfile:
                students = json.load(outfile)
                for id, student in students.items():
                    student_obj = Student(
                        int(id),  # gives value of the key id
                        student["Name"],
                        student["Age"],
                        student["Grade"],
                        student["Subjects"],
                    )
                    self.add_students(student_obj)
        except json.decoder.JSONDecodeError:
            print("File is empty.")
        except FileNotFoundError:
            self.student_list = {}

    def field_to_update(self, id):
        print("""Which feild do want to update:
              -> Name 
              -> Age
              -> Grade
              -> Subjects
              or Type end to stop.
              """)
        while True:
            feild = input("Enter field to update: ")
            if not feild:
                print("Feild cannot be empty.")
                continue
            if feild == "end":
                return
            else:
                if feild == "id":
                    print("ID cannot be updated")
                elif feild == "name":
                    value = self.get_name()
                    self.update_name(id, value)
                elif feild == "age":
                    value = self.get_age()
                    self.update_age(id, value)
                elif feild == "grade":
                    value = self.get_grade()
                    self.update_grade(id, value)
                elif feild == "subjects":
                    value = self.get_subjects()
                    self.update_subjects(id, value)
                else:
                    print("Enter valid field.")

    def get_saved_student_data(self, id: int):
        if self.check_id_exists(id):
            return self.student_list[id]
        return Student()

    def check_id_exists(self, id: int) -> bool:
        return id in self.student_list

    def get_student_data(self) -> Student:
        id = self.get_id()
        name = self.get_name()
        age = self.get_age()
        grade = self.get_grade()
        subjects = self.get_subjects()
        return Student(id, name, age, grade, subjects)

    def get_id(self) -> int:
        while True:
            try:
                id = int(input("Enter student ID: "))
                if self.check_id_exists(id):
                    print("ID exists.")
                    continue
                else:
                    return id

            except ValueError as e:
                print(f"Enter valid value. Failed with error {e}.")

    def get_name(self) -> str:
        while True:
            try:
                name = input("Enter student name: ")
                if not validate_string(name):
                    print("Invalid Name.")
                    continue
                return name
            except ValueError as e:
                print(f"Enter valid value. Failed with error {e}.")

    def get_age(self) -> int:
        while True:
            try:
                age = int(input("Enter student age: "))
                if age <= 10:
                    print("Age should be greater than 10.")
                    continue
                return age

            except ValueError as e:
                print(f"Enter valid value. Failed with error {e}.")

    def get_grade(self) -> str:
        while True:
            try:
                grade = input("Enter student grade: ")
                if not validate_string(grade):
                    print("Invalid Grade.")
                    continue
                return grade
            except ValueError as e:
                print(f"Enter valid value. Failed with error {e}.")

    def get_subjects(self) -> List[str]:
        subjects = []
        while True:
            try:
                count = int(input("How number of subjects: "))
                if count > 0:
                    break
                else:
                    print("Count cannot be negative.")
            except ValueError as e:
                print(f"Enter valid value. Failed with error {e}.")
        n = 1
        while n <= count:
            sub = input(f"Enter subject {n} : ")
            if not validate_string(sub):
                print("Invalid Subject.")
                continue
            else:
                subjects.append(sub)
                n += 1
        return subjects


FILE_NAME = "student_data.json"


def main():
    student_manager = StudentManager(FILE_NAME)
    while True:
        print("""Which operation do you want to perform:
        1. Add Student
        2. View all students
        3. Update students information
        4. Delete Student
        5. Save and Exit""")

        try:
            choice = input("Enter your choice: ")
            choice = int(choice)
            if choice == 1:
                print("Enter student details.")
                student = student_manager.get_student_data()
                student_manager.add_students(student)
                print(f"Student {student.name} added successfully.")
            elif choice == 2:
                student_manager.view_all_students()

            elif choice == 3:
                try:
                    id = int(input("Enter ID of the student to update: "))
                    if student_manager.check_id_exists(id):
                        student_manager.field_to_update(id)
                    else:
                        print("ID doesn't exists.")

                except ValueError as e:
                    print(f"Enter only intergers. Failed with error {e}.")

            elif choice == 4:
                try:
                    id = int(input("Enter ID of the student to delete: "))
                    if student_manager.check_id_exists(id):
                        student_manager.delete_student(id)
                    else:
                        print("ID doesn't exists.")

                except ValueError as e:
                    print(f"Enter only intergers. Failed with error {e}.")

            elif choice == 5:
                student_manager.save_students()
                break

            else:
                print("Invalid option.")

        except ValueError as e:
            print(f"Enter only intergers. Failed with error {e}.")


if __name__ == "__main__":
    main()
