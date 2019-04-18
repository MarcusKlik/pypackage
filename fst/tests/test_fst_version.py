
from unittest import TestCase

import fst

class TestFstVersion(TestCase):
    def test_is_string(self):
        v = fst.fst_version()
        self.assertTrue(isinstance(v, str))
