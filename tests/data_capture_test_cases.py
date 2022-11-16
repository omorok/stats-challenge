test_numbers = [3, 9, 3, 4, 6, 5, 6, 2]

add_cases = [
    (3, None),
    (9, None),
    (3, None),
    (4, None),
    (6, None),
    (4.5, 'Input value error: value out of range or different integer type.'),
    (-1, 'Input value error: value out of range or different integer type.')
    ]

build_test_cases = [
    (test_numbers, {'less(4)': 3, 'between(3,6)': 6, 'greater(4)': 4}),
    (test_numbers, {'less(3)': 1, 'between(6,3)': 6, 'greater(6)': 1}),
    (test_numbers, {'greater(-1)': 'Input value error: value out of range or different integer type.'}),
    (test_numbers, {'greater(1001)': 'Input value error: value out of range or different integer type.'})
    ]