import pytest
from typing import List, Dict
from app.data_capture import DataCapture
from app.stats import Stats

from tests.data_tests_test_cases import less_cases, greater_cases, between_cases


@pytest.fixture
def build_stats():
    def _factory(numbers: List[int]):
        capture = DataCapture()
        for n in numbers:
            capture.add(n)
        return capture.build_stats()
    return _factory


@pytest.mark.parametrize('numbers,methods', less_cases)
def test_less(numbers: List[int], methods: Dict[str,int], build_stats: Stats):    
    stats = build_stats(numbers)
    for method, expected in methods.items():
        if 'less'in method:
            assert eval('stats.' + method) == expected

@pytest.mark.parametrize('numbers,methods', greater_cases)
def test_greater(numbers: List[int], methods: Dict[str,int], build_stats: Stats):
    stats = build_stats(numbers)
    for method, expected in methods.items():
        if 'greater'in method:
            assert eval('stats.' + method) == expected

@pytest.mark.parametrize('numbers,methods', between_cases)
def test_between(numbers: List[int], methods: Dict[str,int], build_stats: Stats):
    stats = build_stats(numbers)
    for method, expected in methods.items():
        if 'between'in method:
            assert eval('stats.' + method) == expected