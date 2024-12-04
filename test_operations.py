import unittest
from student import Student
from presence import Attendance

class TestOperations(unittest.TestCase):
    def setUp(self):
        try:
            Student.list_of_students.clear()
            Student.add("Jan", "Kowalski")
            Student.add("Anna", "Nowak")
        except Exception as e:
            self.fail(f"Test failed due to unexpected exception: {e}")

    def test_update_attendance(self):
        try:
            attendance = Attendance("2024-11-25", [{'id': 0, 'status': 1}, {'id': 1, 'status': 0}])

            attendance.students_attendance[1]['status'] = 1
            self.assertEqual(attendance.students_attendance[1]['status'], 1)
        except Exception as e:
            self.fail(f"Test failed due to unexpected exception: {e}")

    def test_check_students(self):
        try:

            self.assertEqual(len(Student.list_of_students), 2)
            self.assertEqual(Student.list_of_students[0].first_name, "Jan")
        except Exception as e:
            self.fail(f"Test failed due to unexpected exception: {e}")

if __name__ == "__main__":
    unittest.main()