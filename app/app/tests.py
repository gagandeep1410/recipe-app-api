"""
Sample tests

"""

from django.test import SimpleTestCase

from app import calc

class calcTests(SimpleTestCase):
    def test_add_number(self):
        res = calc.add(5,6)

        self.assertEqual(res,11)
    def test_subtract_number(self):
        res = calc.sub(15,6)

        self.assertEqual(res,9)