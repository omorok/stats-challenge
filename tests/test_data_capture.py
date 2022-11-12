import pytest

from app.data_capture import DataCapture

test_cases = [
    ([3, 9, 3, 4, 6], {'less(4)': 2, 'between(3,6)': 4, 'greater(4)': 2}),
    ([3, 9, 3, 4, 6, 5, 6, 2], {'less(4)': 3, 'between(4,6)': 4, 'greater(4)': 4}),
    ([3, 9, 3, 4, 6, 5, 6, 2], {'greater(-1)': 'Input value error: value out of range or different integer type.'}),
    ([3, 9, 3, 4, 6, 5, 6, 2], {'greater(1001)': 'Input value error: value out of range or different integer type.'})
    ]

@pytest.mark.parametrize('numbers,methods', test_cases)
def test_build_stats(numbers, methods):
    capture = DataCapture()
    for n in numbers:
        capture.add(n)
    stats = capture.build_stats()
    for method,expected in methods.items():
        assert eval('stats.' + method) == expected
