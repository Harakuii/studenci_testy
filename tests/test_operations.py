import unittest
from student import Student
from presence import Attendance
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

class TestOperations(unittest.TestCase):
    def setUp(self):
        Student.list_of_students.clear()
        Student.add("Jan", "Kowalski")
        Student.add("Anna", "Nowak")

    def test_update_attendance(self):
        attendance = Attendance("2024-11-25", [{'id': 0, 'status': 1}, {'id': 1, 'status': 0}])

        attendance.students_attendance[1]['status'] = 1
        self.assertEqual(attendance.students_attendance[1]['status'], 1)

    def test_check_students(self):
        self.assertEqual(len(Student.list_of_students), 2)
        self.assertEqual(Student.list_of_students[0].first_name, "Jan")

if __name__ == "__main__":
    unittest.main()
    