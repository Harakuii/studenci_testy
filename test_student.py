import unittest
import os
from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        Student.list_of_students.clear()
        self.test_file = "students_test.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_student(self):
        Student.add("Jan", "Kowalski")
        self.assertEqual(len(Student.list_of_students), 1)
        self.assertEqual(Student.list_of_students[0].first_name, "Jan")

    def test_save_and_load_students(self):
        Student.add("Anna", "Nowak")
        Student.add("Piotr", "Zielinski")
        Student.save_to_file(self.test_file)

        self.assertTrue(os.path.exists(self.test_file))

        Student.list_of_students.clear()
        Student.load_from_file(self.test_file)
        self.assertEqual(len(Student.list_of_students), 2)
        self.assertEqual(Student.list_of_students[1].surname, "Zielinski")

if __name__ == "__main__":
    unittest.main()