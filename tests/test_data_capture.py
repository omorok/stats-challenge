import pytest
from tests.data_tests_test_cases import test_cases

from app.data_capture import DataCapture

@pytest.mark.parametrize('number, expected', test_cases)
def test_add(number, expected):
    capture = DataCapture()    
    assert capture.add(number) == expected   
        
