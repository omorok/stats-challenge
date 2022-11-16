import pytest

from tests.data_capture_test_cases import add_cases, build_test_cases

from app.data_capture import DataCapture

@pytest.mark.parametrize('number, expected', add_cases)
def test_add(number: int, expected: int):
    capture = DataCapture()
    assert capture.add(number) == expected

@pytest.mark.parametrize('numbers,methods', build_test_cases)
def test_build_stats(numbers, methods):
    capture = DataCapture()
    for n in numbers:
        capture.add(n)
    stats = capture.build_stats()
    for method,expected in methods.items():
        assert eval('stats.' + method) == expected

