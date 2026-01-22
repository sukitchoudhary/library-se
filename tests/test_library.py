class TestLibrarySprint3(unittest.TestCase):

    def test_report_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("ID | Title | Author | Status", report)

    def test_report_contains_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        report = lib.generate_report()
        self.assertIn("B1", report)
