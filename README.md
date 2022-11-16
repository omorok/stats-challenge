# Python Stats Challenge

The challenge is to create a program that computes some basic statistics on a collection of small positive integers. You can assume all values will be less than 1,000.

Implement this challenge in whatever programming language
best highlights your skills. Also, please supply a README with
details on how to setup and run your application.

### Requirements

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.
Here’s the program skeleton in Python to explain the structure:
```sh
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
```


### Challenge Conditions
* You cannot import a library that solves it instantly
* The methods add(), less(), greater(), and between() should have
constant time O(1)
* The method build_stats() can be at most linear O(n)
* Apply the best practices you know
* Share a public repo with your project



## For usage example

Install [Python3+](https://www.python.org/) before run and get the source from:


```sh
git clone https://github.com/omorok/stats-challenge.git
```

to run the challenge run the code below
```sh
python3 main.py
```

## For testing purposes
If you need to add some test cases, be free to edit the files *data_capture_test_cases.py* and *data_tests_test_cases.py* within **/tests** folder.
The file estructure shuld look like this:

**data_capture_test_cases.py**
```sh
test_numbers = [3, 9, 3, 4, 6, 5, 6, 2]

test_numbers = [3, 9, 3, 4, 6, 5, 6, 2]

add_cases = [
    (test_numbers, {
        'add(3)': None,
        'add(9)': None,
        'add(3)': None,
        'add(4)': None,
        'add(6)': None,
        'add(4.5)': 'Input value error: value out of range or different integer type.',
        'add(-1)': 'Input value error: value out of range or different integer type.'
        }),
    ]

build_test_cases = [
    (test_numbers, {'less(4)': 3, 'between(3,6)': 6, 'greater(4)': 4}),
    (test_numbers, {'less(3)': 1, 'between(6,3)': 6, 'greater(6)': 1}),
    (test_numbers, {'greater(-1)': 'Input value error: value out of range or different integer type.'}),
    (test_numbers, {'greater(1001)': 'Input value error: value out of range or different integer type.'})
    ]
```

Above: the first list array (test_numbers) should contains the numbers you want to add to the test cases (all of them at once), then you could edit the add_cases (input value, expected output) list array or the build_test_cases list array second dictionary argument where the keys are the are method names, and the values expected by each test case.

and
**data_tests_test_cases.py**
```sh
test_numbers = [3, 9, 3, 4, 6, 5, 6, 2]

less_cases = [
    (test_numbers, {'less(3)': 1, 'less(4)': 3, 'less(5)': 4}),
    (test_numbers, {'less(-1)': 'Input value error: value out of range or different integer type.'}),
    (test_numbers, {'less(1001)': 'Input value error: value out of range or different integer type.'})
    ]

between_cases = [
    (test_numbers, {'between(3,6)': 6, 'between(4,6)': 4, 'between(6,4)': 4}),
    (test_numbers, {'between(-1, 10)': 'Input value error: value out of range or different integer type.'}),
    (test_numbers, {'between(1001, 4)': 'Input value error: value out of range or different integer type.'})
    ]

greater_cases = [
    (test_numbers, {'greater(3)': 5, 'greater(4)': 4, 'greater(5)': 3}),
    (test_numbers, {'greater(-1)': 'Input value error: value out of range or different integer type.'}),
    (test_numbers, {'greater(1001)': 'Input value error: value out of range or different integer type.'})
    ]
```
Above: in the same way as the first file, you are allowed to edit test_numbers array list with all input numbers, then array list for less_cases, between_cases and greater_cases.

### Install Pytest before any testing run. 
```sh
pip install pytest==7.1.2
```
to run test execute the lines below

```sh
cd tests
pytest
```
