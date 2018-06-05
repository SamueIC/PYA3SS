from pickle import Unpickler as Unpick
from io import BytesIO


# Wesley
class Unpickler:
    # Wesley
    @staticmethod
    def unpickle_dictionary(list):
        """Input a dictionary with key value
            where value is pickled and return a dictionary
            with unpickled values"""
        # need the items function to iterate through dictionary
        unpickled_dict = dict()
        for record in list:
            # Create object that will be treated as a file for unpickling
            file = BytesIO(record[1])
            unpickled_dict[record[0]] = Unpick(file).load()
        return unpickled_dict

