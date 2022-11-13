import pytest

from tests.data_capture_test_cases import test_cases

from app.data_capture import DataCapture

@pytest.mark.parametrize('numbers,methods', test_cases)
def test_less(numbers, methods):
    
    capture = DataCapture()
    for n in numbers:
        capture.add(n)
    stats = capture.build_stats()
    for method, expected in methods.items():
        if 'less'in method:
            assert eval('stats.' + method) == expected

@pytest.mark.parametrize('numbers,methods', test_cases)
def test_greater(numbers, methods):    
    capture = DataCapture()
    for n in numbers:
        capture.add(n)
    stats = capture.build_stats()
    for method, expected in methods.items():
        if 'greater'in method:
            assert eval('stats.' + method) == expected

@pytest.mark.parametrize('numbers,methods', test_cases)
def test_between(numbers, methods):    
    capture = DataCapture()
    for n in numbers:
        capture.add(n)
    stats = capture.build_stats()
    for method, expected in methods.items():
        if 'between'in method:
            assert eval('stats.' + method) == expected