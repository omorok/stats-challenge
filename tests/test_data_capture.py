import pytest
from tests.data_test_cases import test_cases

from app.data_capture import DataCapture

@pytest.mark.parametrize('numbers,methods', test_cases)
def test_build_stats(numbers, methods):
    capture = DataCapture()
    for n in numbers:
        capture.add(n)
    stats = capture.build_stats()
    for method,expected in methods.items():        
        assert eval('stats.' + method) == expected
