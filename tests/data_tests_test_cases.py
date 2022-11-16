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

