import unittest
import os
from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        Student.list_of_students.clear()
        self.test_file = "students_test.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            try:
                os.remove(self.test_file)
            except Exception as e:
                print(f"Error removing file {self.test_file}: {e}")

    def test_add_student(self):
        try:
            Student.add("Jan", "Kowalski")
            self.assertEqual(len(Student.list_of_students), 1)
            self.assertEqual(Student.list_of_students[0].first_name, "Jan")
        except Exception as e:
            self.fail(f"Test failed due to unexpected exception: {e}")

    def test_save_and_load_students(self):
        try:
            Student.add("Anna", "Nowak")
            Student.add("Piotr", "Zielinski")
            Student.save_to_file(self.test_file)

            self.assertTrue(os.path.exists(self.test_file))

            Student.list_of_students.clear()
            Student.load_from_file(self.test_file)
            self.assertEqual(len(Student.list_of_students), 2)
            self.assertEqual(Student.list_of_students[1].surname, "Zielinski")
        except Exception as e:
            self.fail(f"Test failed due to unexpected exception: {e}")

if __name__ == "__main__":
    unittest.main()