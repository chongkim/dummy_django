from django.test import TestCase

class MyTestCase(TestCase):
    def test_should_pass(self):
        x = 1
        self.assertEqual(x, 1)
