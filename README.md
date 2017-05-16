# MovieDBTests
MovieDB automated tests

Developed using:
- Python 2.7.10
- nose 1.3.7
- nose-testconfig 0.10
- requests 2.14.2

To run tests
1. Open the file config/default.ini and update with a valid API key
2. From the root directory of the project run:  nosetests -c config/default.ini tests/person_tests.py