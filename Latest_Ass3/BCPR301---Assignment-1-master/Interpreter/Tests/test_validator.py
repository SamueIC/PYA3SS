from unittest import TestCase
from Interpreter.validator import Validator
from datetime import datetime


class TestValidator(TestCase):

    def setUp(self):
        self.validator = Validator()

    def tearDown(self):
        del self.validator

    def test_empid_invalid(self):
        """
        Tests validating graph_data
        """
        empid = "A12323123123"
        expected = False

        result = self.validator.check_all(empid, new_key='empid')
        self.assertEqual(expected, result)

    def test_empid_valid(self):
        """
        Tests validating graph_data
        """
        empid = "Q666"
        expected = "Q666"

        result = self.validator.check_all(empid, new_key='empid')
        self.assertEqual(expected, result)

    def test_gender_true_female_letter(self):
        """
        Tests validating graph_data
        """
        gender = "F"
        expected = "F"
        # fix this!!
        result = self.validator.check_all(gender, new_key='gender')
        self.assertEqual(expected, result)

    def test_gender_true_female_string(self):
        """
        Tests validating graph_data
        """
        gender = "Female"
        expected = "F"

        result = self.validator.check_all(gender, new_key='gender')
        self.assertEqual(expected, result)

    def test_gender_true_male_string(self):
        """
        Tests validating graph_data
        """
        gender = "male"
        expected = "M"

        result = self.validator.check_all(gender, new_key='gender')
        self.assertEqual(expected, result)

    def test_gender_false(self):
        """
        Tests validating graph_data
        """
        gender = "transgender"
        expected = False

        result = self.validator.check_all(gender, new_key='gender')
        self.assertEqual(expected, result)

    def test_age_true(self):
        """
        Tests validating graph_data
        """
        age = "23"
        expected = "23"

        result = self.validator.check_all(age, new_key='age')
        self.assertEqual(expected, result)

    def test_age_false(self):
        """
        Tests validating graph_data
        """
        age = "213"
        expected = False

        result = self.validator.check_all(age, new_key='age')
        self.assertEqual(expected, result)

    def test_sales_true(self):
        """
        Tests validating graph_data
        """
        sales = "123"
        expected = "123"

        result = self.validator.check_all(sales, new_key='sales')
        self.assertEqual(expected, result)

    def test_sales_false(self):
        """
        Tests validating graph_data
        """
        sales = "1233"
        expected = False

        result = self.validator.check_all(sales, new_key='sales')
        self.assertEqual(expected, result)

    def test_BMI_true(self):
        """
        Tests validating graph_data
        """
        BMI = "Normal"
        expected = "Normal"

        result = self.validator.check_all(BMI, new_key='bmi')
        self.assertEqual(expected, result)

    def test_BMI_lowercase(self):
        """
        Tests validating graph_data
        """
        BMI = "overweight"
        expected = "overweight"

        result = self.validator.check_all(BMI, new_key='bmi')
        self.assertEqual(expected, result)

    def test_BMI_false(self):
        """
        Tests validating graph_data
        """
        BMI = "Fatty"
        expected = False

        result = self.validator.check_all(BMI, new_key='bmi')
        self.assertEqual(expected, result)

    def test_salary_true(self):
        """
        Tests validating graph_data
        """
        salary = "456"
        expected = "456"

        result = self.validator.check_all(salary, new_key='salary')
        self.assertEqual(expected, result)

    def test_salary_false(self):
        """
        Tests validating graph_data
        """
        salary = "456million"
        expected = False

        result = self.validator.check_all(salary, new_key='salary')
        self.assertEqual(expected, result)

    def test_birthday_true(self):
        """
        Tests validating graph_data
        """
        birthday = "13/12/1994"
        expected = "13/12/1994"

        result = self.validator.check_all(birthday, new_key='birthday')
        self.assertEqual(expected, result)

    def test_birthday_false_delim_fix(self):
        """
        Tests validating graph_data
        """
        birthday = "13-12-1994"
        result = self.validator.check_all(birthday, new_key='Birthday')
        expected = "13/12/1994"
        self.assertEqual(expected, result)

    def test_xlxs_date(self):
        """"
        Tests static return function, test coverage purposes
        """
        expected = "13-12-1994"
        test_date = datetime(1994, 12, 13)
        result = Validator.xlsx_date(test_date)
        self.assertEquals(expected, result)

    def test_birthday_day_length(self):
        """
        Tests validating graph_data
        """
        birthday = "1/12/1994"
        expected = "1/12/1994"

        result = self.validator.check_all(birthday, new_key='birthday')
        self.assertEqual(expected, result)

    def test_birthday_month_length(self):
        """
        Tests validating graph_data
        """
        birthday = "13/1/1994"
        expected = "13/1/1994"

        result = self.validator.check_all(birthday, new_key='birthday')
        self.assertEqual(expected, result)

    def test_birthday_both_length(self):
        """
        Tests validating graph_data
        """
        birthday = "1/1/1994"
        expected = "1/1/1994"

        result = self.validator.check_all(birthday, new_key='birthday')
        self.assertEqual(expected, result)

    def test_save_dict_valid(self):
        """
        Test static checker method
        """
        data2 = {0: {'ID': 'Q123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                     'Birthday': '01/01/1996'}}
        expected2 = {0: {'Empid': 'Q123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'Bmi': 'normal', 'Salary': '12', 'Birthday': '01/01/1996'}}
        result2 = self.validator.save_dict(data2)
        self.assertEqual(result2, expected2)
        print(result2)

    def test_z_save_dict_invalid(self):
        """
        Test static checker method
        """
        data1 = {0: {'ID': 'A123', 'Gender': 'F', 'Age': '212', 'Sales': '101', 'BMI': 'Normal', 'Salary': '12',
                     'Birthday': '01/01/1996'},
                 1: {'ID': 'Q999', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                     'Birthday': '01/01/1996'}
                 }
        expected1 = {1: {'Empid': 'Q999', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'Bmi': 'normal', 'Salary': '12',
                         'Birthday': '01/01/1996'}
                     }
        result1 = self.validator.save_dict(data1)
        self.assertEqual(result1, expected1)

    def test_check_checker_invalid_id(self):
        """
        Test static checker method
        """
        data = {0: {'ID': 'A123', 'Gender': 'F', 'Age': '201', 'Sales': '101', 'BMI': 'Normal', 'Salary': '12',
                    'Birthday': '01/01/1996'},
                1: {'ID': 'A123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                    'Birthday': '01/01/1996'}
                }

        expected = {1: {'Empid': 'A123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'Bmi': 'normal', 'Salary': '12',
                        'Birthday': '01/01/1996'}
                    }
        result = self.validator.save_dict(data)
        self.assertEqual(result, expected)

    def test_check_invalid_key(self):
        """
        Tests validating graph_data
        """
        data = {'ASDSADASD': 'A123', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',
                        'Birthday': '01/01/1996'}
        result = self.validator.checker(data)
        expected = False
        self.assertEqual(expected, result)
