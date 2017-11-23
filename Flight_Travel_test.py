import unittest
import Flight
import Travel
import math
from contextlib import contextmanager
from StringIO import StringIO

@contextmanager
def captured_output():
	new_out, new_err = StringIO(), StringIO()
	old_out, old_err = sys.stdout, sys.stderr
	try:
		sys.stdout, sys.stderr = new_out, new_err
		yield sys.stdout, sys.stderr
	finally:
		sys.stdout, sys.stderr = old_out, old_err

class MyTest(unittest.TestCase):

	def setUp(self):
		self.flight=Flight()

	def to_string_method_should_return_empty_string(self):
		self.assertEqual(str(self.flight), '')

	def should_print_welcome_message(self):
		with captured_output() as (out, err):
			self.flight()

		output = out.getvalue().strip()
		self.assertEqual(output, "Start!")

	def should_print_given_arguments(self):
		x = 1
		with captured_output() as (out, err):
			self.flight()

		output = out.getvalue().strip()
		self.assertEqual(output, "1")


if __name__=="__main__":
        unittest.main()
