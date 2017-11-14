import inspect
from sys import stdout
from sys import stderr

class TestRunner(dict):
    provider = None
    terraform_directory = None

    def get_test_groups(self):
        for filename in os.listdir('./tests/aws'):
            print(inspect.getmodulename(filename))

        return None

    def exec(self):
        print("Executing Terraform unit test(s).")
        exit(0)

    def add_test_group(self, provider, tgroup):
        # Dynamically import test class
        from src.tests import name
        # Add test class to test runner
        return None

    def add_test(self, provider, tgroup, test):
        return None

