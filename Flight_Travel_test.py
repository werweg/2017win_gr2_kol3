import unittest
from Flight import Flight 
from Travel import Travel 
from contextlib import contextmanager
from StringIO import StringIO
import sys
import mock
import __builtin__

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
        self.angle = 0
        self.flag = 'n'
        self.flag1 = 'y'

    def test_to_string_method_should_return_empty_string(self):
        self.assertEqual(str(self.flight), '')
        print self.flight

    def test_should_print_welcome_message(self):
        with captured_output() as (out, err):
            Flight()

        output = out.getvalue().strip()
        self.assertEqual(output, "Start!")

    def test_should_print_given_arguments(self):
        argument1 = 1
        argument2 = ['z', 2]
        with captured_output() as (out, err):
            Travel.simulator_reply(argument1, argument2)

        output = out.getvalue().strip()
        self.assertEqual(output, str(argument1) + '\n' + str(argument2))

    def test_should_have_proper_field_values_set(self):
        self.assertEqual(Travel.angle, self.angle)
        self.assertEqual(Travel.flag, self.flag)
        self.assertEqual(Travel.flag1, self.flag1)


    def test_should_not_print_info_when_flag_is_yes_and_flag1_is_yes(self):
        self.flight.flag = 'y'
        self.flight.flag1 = 'y'
        self.verify_flight_go_empty_output()

    def test_should_not_print_info_when_flag_is_no_flag1_is_no(self):
        self.flight.flag = 'n'
        self.flight.flag1 = 'n'
        self.verify_flight_go_empty_output()

    def test_should_not_print_info_when_flag_is_no_flag1_is_yes(self):
        self.flight.flag = 'n'
        self.flight.flag1 = 'yes'
        self.verify_flight_go_empty_output()

    def verify_flight_go_empty_output(self):
        with captured_output() as (out, err):
            self.flight.go()

        output = out.getvalue().strip()
        self.assertEqual(output, '')

    @mock.patch.object(__builtin__, 'raw_input')
    def test_should_return_users_input(self, mock_raw_input):
        mock_raw_input.return_value = 'n'
        self.assertEqual(self.flight.user_action(''), 'n')

    @mock.patch.object(__builtin__, 'raw_input')
    def test_should_print_init_angle(self, mock_raw_input):
        mock_raw_input.return_value = 'n'
        with captured_output() as (out, err):
            self.flight.go()

        output = out.getvalue().strip()
        self.assertTrue(output.startswith('The angle is:'))
        self.assertTrue(output.endswith('We crashed!'))


if __name__=="__main__":
        unittest.main()
