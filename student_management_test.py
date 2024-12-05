from student_management import Student, StudentManager
import unittest
import json
from unittest.mock import patch


class TestStudentRegister(unittest.TestCase):
    def setUp(self):
        self.file_name = "student_data_test.json"
        self.student_manager = StudentManager(self.file_name)

    def test_add_students(self):
        self.student_manager.add_students(Student(2, "san", 25, "vg+", ["science", "history"]))
        self.assertEqual(self.student_manager.student_list[2].name, "san")

    @patch("student_management.test_print")
    def test_view_students(self, mock_print):
        self.student_manager.add_students(Student(10, "vimal", 22, "g+", ["chemistry", "english"]))
        self.student_manager.view_all_students()
        mock_print.assert_any_call(
            "ID: 10, Name: vimal, Age: 22, Grade: g+, Subjects: chemistry, english"
        )
        pass

    def test_update_name(self):
        self.student_manager.add_students(Student(3, "vimal", 22, "g+", ["chemistry", "english"]))
        self.student_manager.update_name(3, "sanjana")
        self.assertEqual(self.student_manager.student_list[3].name, "sanjana")

    def test_update_age(self):
        self.student_manager.add_students(Student(4, "vimal", 22, "g+", ["chemistry", "english"]))
        self.student_manager.update_age(4, 25)
        self.assertEqual(self.student_manager.student_list[4].age, 25)

    def test_update_grade(self):
        self.student_manager.add_students(Student(5, "vimal", 22, "g+", ["chemistry", "english"]))
        self.student_manager.update_grade(5, "vg")
        self.assertEqual(self.student_manager.student_list[5].grade, "vg")

    def test_update_subjects(self):
        self.student_manager.add_students(Student(6, "vimal", 22, "g+", ["chemistry", "english"]))
        self.student_manager.update_subjects(6, ["math"])
        self.assertEqual(self.student_manager.student_list[6].subjects, ["math"])

    def test_delete_student(self):
        self.student_manager.add_students(Student(7, "vim", 25, "vg+", ["science", "history"]))
        self.assertIn(7, self.student_manager.student_list)
        self.student_manager.delete_student(7)
        self.assertNotIn("7", self.student_manager.student_list)

    def test_save_to_file(self):
        self.student_manager.add_students(Student(8, "durga", 25, "vg+", ["telugu", "english"]))
        self.student_manager.save_students()
        with open(self.file_name, "r") as readfile:
            data = json.load(readfile)
            self.assertIn("8", data)
            self.assertEqual(data["8"]["Name"], "durga")

    def test_load_students_from_file(self):
        self.student_manager.load_students()
        self.assertEqual(self.student_manager.student_list[8].name, "durga")
