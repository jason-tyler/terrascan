import unittest
import os
import terraform_validate

class TestGroup(unittest.TestCase):
    terraform_directory = None

    def setUp(self):
        # Tell the module where to find your terraform configuration folder
        self.path = os.path.join(
            os.path.dirname(
                os.path.realpath(__file__)), self.terraform_directory)
        self.v = terraform_validate.Validator(self.path)