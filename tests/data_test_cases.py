test_cases = [
    ([3, 9, 3, 4, 6], {'less(4)': 2, 'between(3,6)': 4, 'greater(4)': 2}),
    ([3, 9, 3, 4, 6, 5, 6, 2], {'less(4)': 3, 'between(4,6)': 4, 'greater(4)': 4}),
    ([3, 9, 3, 4, 6, 5, 6, 2], {'greater(-1)': 'Input value error: value out of range or different integer type.'}),
    ([3, 9, 3, 4, 6, 5, 6, 2], {'greater(1001)': 'Input value error: value out of range or different integer type.'})
    ]