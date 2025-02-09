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

