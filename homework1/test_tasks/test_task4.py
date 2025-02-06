import pytest

# Test valid cases for discount function
def test_valid_discount():
    # Test discount function on floats
    assert calculate_discount(69.95, 25) == 52.46
    assert calculate_discount(11000, 23.45) == 8420.5
    
    # Test discount function on integers
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(700, 6) == 658

# Test invalid cases for discount function
def test_invalid_discount():
    # Test that function does not accept non-numeric variables
    # In all cases below
    with pytest.raises(TypeError) as excinfo:
        calculate_discount("Extra", "Silly")
    assert str(excinfo.value) == "Error, user_price and user_discount must be of type int or float"

    with pytest.raises(TypeError) as excinfo:
        calculate_discount("Extra", 20)
    assert str(excinfo.value) == "Error, user_price and user_discount must be of type int or float"
    
    with pytest.raises(TypeError) as excinfo:
        calculate_discount(20, "Silly")
    assert str(excinfo.value) == "Error, user_price and user_discount must be of type int or float"

    # Check that negative numbers are not accepted below
    # In all cases below
    with pytest.raises(ValueError) as excinfo:
        calculate_discount(-20, -2)
    assert str(excinfo.value) == "Error, user_price and user_discount must be non-negative"

    with pytest.raises(ValueError) as excinfo:
        calculate_discount(-100, 20)
    assert str(excinfo.value) == "Error, user_price and user_discount must be non-negative"

    with pytest.raises(ValueError) as excinfo:
        calculate_discount(20, -2)
    assert str(excinfo.value) == "Error, user_price and user_discount must be non-negative"
    
    # Check that discount cannot be greater than 100
    with pytest.raises(ValueError) as excinfo:
        calculate_discount(100, 101)
    assert str(excinfo.value) == "Error, user_discount must be between 0 and 100"