# Unit Testing

```bash
$ cd testing
$ python3 -m unittest  -v test.unittest_cloudcredit
$ python3 -m pip install coverage
$ python3 -m coverage run -m unittest -v test.unittest_cloudcredit
$ python3 -m coverage report
$ coverage run -m unittest -v test.unittest_cloudcredit && coverage 
report -m

$ python3 -m pip install pytest
$ pytest -v
$ coverage run -m pytest -v && coverage report -m

```
