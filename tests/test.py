from tutorialpackaging import mypackages

def test_generate_fibonacci():
    # Test case 1: n = 0
    assert mypackages.generate_fibonacci(0) == [], 'Incorrect'

    # Test case 2: n = 1
    assert mypackages.generate_fibonacci(1) == [0], 'Incorrect'

    # Test case 3: n = 5
    assert mypackages.generate_fibonacci(5) == [0, 1, 1, 2, 3], 'Incorrect'

    # Test case 4: n = 10
    assert mypackages.generate_fibonacci(0) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Incorrect'

