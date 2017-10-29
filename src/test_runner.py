from sys import stdout
from sys import stderr

class TestRunner(dict):
    def exec(self):
        print("Executing Terraform unit test(s).")
        exit(0)

    def add_test_class(self, name):
        # Dynamically import test class
        from src.tests import name
        # Add test class to test runner

