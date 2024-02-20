def function(x):
    if x == 1:
        print(True)
        return None
    elif x == 2:
        return 2
    elif x == 3:
        print(False)
        return False
    return x + 1

import pytest


# Define test cases using pytest
@pytest.mark.parametrize("input_value, expected_output", [
    (1, True),  
    (2, 3), 
    (3, False), 
    (100, 101) 
])
def test_func(input_value, expected_output):
    # Call the function with the input value
    result = function(input_value)

    # Check if the result matches the expected output
    assert result == expected_output
