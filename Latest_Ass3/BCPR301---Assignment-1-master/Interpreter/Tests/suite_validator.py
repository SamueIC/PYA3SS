from unittest import TestSuite, TextTestRunner, makeSuite
from Interpreter.Tests.test_validator import TestValidator


def test_suite_validator():

    my_suite = TestSuite()
    my_suite.addTest(makeSuite(TestValidator))
    return my_suite


if __name__ == '__main__':  # pragma: no cover
    runner = TextTestRunner(verbosity=2)
    runner.run(test_suite_validator())

