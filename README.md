## Python Stats Challenge

The challenge is to create a program that computes some basic statistics on a collection of small positive integers. You can assume all values will be less than 1,000.

The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.

Conditions:

The methods add(), less(), greater(), and between() should have
constant time O(1).
The method build_stats() can be at most linear O(n).

## For usage example

Install [Python3+](https://www.python.org/) before run.

```sh
git clone https://github.com/omorok/stats-challenge.git
cd stats-challenge
python main.py
```
or
```sh
python3 main.py
```

## For testing purposes
Install Pytest

```sh
pip install pytest==7.1.2
```
run test

```sh
cd tests
pytest
```