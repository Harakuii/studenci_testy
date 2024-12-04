import unittest
import os
from presence import Attendance

class TestAttendance(unittest.TestCase):
    def setUp(self):
        self.test_file = "attendance_test.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            try:
                os.remove(self.test_file)
            except Exception as e:
                print(f"Error removing file {self.test_file}: {e}")

    def test_save_and_load_attendance(self):
        try:
            
            data = [{'id': 1, 'status': 1}, {'id': 2, 'status': 0}]
            attendance = Attendance("2024-11-25", data)
            attendance.save_to_file(self.test_file)

            self.assertTrue(os.path.exists(self.test_file))

            loaded_attendance = Attendance.load_attendance_from_file(self.test_file)
            self.assertEqual(loaded_attendance.date, "attendance_test")
            self.assertEqual(len(loaded_attendance.students_attendance), 2)
            self.assertEqual(loaded_attendance.students_attendance[0]['status'], 1)
            
        except Exception as e:
            self.fail(f"Test failed due to unexpected exception: {e}")

if __name__ == "__main__":
    unittest.main()
