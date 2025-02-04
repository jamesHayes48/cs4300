import pytest
def calculate_discount(price, discount):
    # Print error if int or float was not passed
    if (not isinstance(price, (int, float))) or (not isinstance(discount, (int, float))):
        raise TypeError("Error, user_price and user_discount must be of "
        "type int or float")
    
    # Print error if either was negative
    elif (discount < 0) or (price < 0):
        raise ValueError("Error, user_price and user_discount must be "
        "non-negative")

    # Print error is user_discount is above 100
    elif discount > 100:
        raise ValueError("Error, user_discount must be between 0 and 100")
    
    # Calculate new price after discount is applied
    else:
        discount_percent = discount / 100
        value_off = round(price * discount_percent, 2)
        new_price = round(price - value_off, 2)
        return new_price

def test_valid_discount():
    # Test discount function on floats
    assert calculate_discount(69.95, 25) == 52.46
    assert calculate_discount(11000, 23.45) == 8420.5
    
    # Test discount function onf integers
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(700, 6) == 658

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