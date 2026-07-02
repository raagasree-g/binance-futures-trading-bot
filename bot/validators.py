def validate_side(side):
    side = side.upper().strip()

    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):
    order_type = order_type.upper().strip()

    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price):
    if price is None:
        raise ValueError("Price is required for LIMIT orders")

    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number")

    if price <= 0:
        raise ValueError("Price must be greater than 0")

    return price