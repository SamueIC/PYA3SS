import re
from copy import deepcopy


class Validator:
    def __init__(self):
        self.temp_dict = dict()
        self.valid_dict = dict()
        self.empid = "^[A-Z][\d]{3}$"
        self.gender = "^(M|F)$"
        self.age = "^[\d]{2}$"
        self.sales = "^[\d]{3}$"
        self.bmi = "^((n|N)ormal)|((o|O)verweight)|((o|O)besity)|((u|U)nderweight)$"
        self.salary = "^([\d]{2}|[\d]{3})$"
        self.birthday = "^(((0[1-9])|([1-31]))|[1-2][0-9]|3(0|1))(/)(((0[1-9])|([1-12]))|1[0-2])(/)(19|20)[0-9]{2}$"

    def check_all(self, new_value, new_key):
        """
        :param new_value:
        :param new_key:
        :return:
        >>> v = Validator()
        >>> v.checker({'ID': 'Q999', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', 'Salary': '12',\
                     'Birthday': '01/01/1996'})
        True
        """
        new_key = getattr(self, new_key.lower())
        check_value = str(new_value)
        check_value = self.fix_bday_delims(check_value)
        check_value = self.fix_gender(check_value)
        match = re.match(new_key, check_value)
        if match:
            a = check_value
            return a
        elif match is None:
            return False

    @staticmethod
    def fix_gender(new_gender):
            match = re.match("^(m|M)ale$", new_gender)
            fmatch = re.match("^(f|F)emale$", new_gender)
            if match:
                new_gender = "M"
            elif fmatch:
                new_gender = "F"
            return new_gender

    @staticmethod
    def fix_bday_delims(new_birthday):
        invalid_delims = "^(|/\\.:;,_-)$"
        for i in invalid_delims:
            new_birthday = new_birthday.replace(i, "/")
        return new_birthday

    @staticmethod
    def xlsx_date(a_date):
        return a_date.date().strftime("%d-%m-%Y")

    def checker(self, row):
        for key, value in row.items():
            valid_keys = {"id", "empid", "gender", "age", "sales", "salary", "birthday", "bmi"}
            key2 = key.lower()
            if key2 in valid_keys:
                if key2 == "id":
                    key2 = "empid"
                elif key2 == "bmi":
                    value = value.lower()
                else:
                    key2 = key2.lower()
                if self.check_all(value, key2) is False:
                    return False
                else:
                    self.push_value(key2.capitalize(), self.check_all(value, key2))
            else:
                return False

    def save_dict(self, loaded_dict):
        for empno, row in loaded_dict.items():
            b = self.checker(row)
            if b is False:
                print("Error at entry: " + str(empno))
            else:
                self.push_row(empno)
        return self.return_dict()

    def push_value(self, key, val):
        self.temp_dict[key] = val

    def push_row(self, empno):
        print("Adding Row " + str(empno))
        temp = deepcopy(self.temp_dict)
        self.valid_dict[empno] = temp
        print(self.valid_dict[empno])

    def return_dict(self):
        return self.valid_dict
