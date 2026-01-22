import unittest
from src.library import Library
class TestLibrarySprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", lib.books)

    def test_duplicate_book_addition(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "Java", "James")

if __name__ == "__main__":
    unittest.main()

class TestLibrarySprint2(unittest.TestCase):

    def test_report_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("ID | Title | Author | Status", report)

    def test_report_contains_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        report = lib.generate_report()
        self.assertIn("B1", report)
