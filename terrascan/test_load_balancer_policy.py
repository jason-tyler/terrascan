import unittest
import os
import terraform_validate
from . import settings

class TestEncryption(unittest.TestCase):

    def setUp(self):
        # Tell the module where to find your terraform configuration folder
        self.path = os.path.join(
            os.path.dirname(
                os.path.realpath(__file__)), settings.TERRAFORM_LOCATION)
        self.v = terraform_validate.Validator(self.path)