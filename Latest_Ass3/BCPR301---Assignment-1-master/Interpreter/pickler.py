from pickle import dumps, Unpickler as Unpick
from io import BytesIO


class Pickler:
    @staticmethod
    def pickle_unpickle(input_value):
        this_dict = dict()
        input_type = type(input_value)
        if input_type == dict:
            for key, value in input_value.items():
                this_dict[key] = dumps(value)
            return this_dict
        elif input_type == list:
            for record in input_value:
                # Create object that will be treated as a file for unpickling
                file = BytesIO(record[1])
                this_dict[record[0]] = Unpick(file).load()
            return this_dict
        else:
            print("Invalid input value, expected 'list' or 'dict' but received {0}".format(input_type))
            # May not be necessary v
            return False
