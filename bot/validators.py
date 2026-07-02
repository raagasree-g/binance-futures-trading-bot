def validate_side(side):
    """Validate and normalize the order side."""
    side = side.upper().strip()

    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):
    """Validate and normalize the supported order type."""
    order_type = order_type.upper().strip()

    if order_type not in ("MARKET", "LIMIT", "STOP_LIMIT"):
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

    return order_type


def validate_quantity(quantity):
    """Validate that quantity is a positive number."""
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price):
    """Validate that price is present and greater than zero."""
    if price is None:
        raise ValueError("Price is required for LIMIT orders")

    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number")

    if price <= 0:
        raise ValueError("Price must be greater than 0")

    return price


def validate_stop_price(stop_price):
    """Validate that stop price is present and greater than zero."""
    if stop_price is None:
        raise ValueError("Stop price is required for STOP_LIMIT orders")

    try:
        stop_price = float(stop_price)
    except ValueError:
        raise ValueError("Stop price must be a number")

    if stop_price <= 0:
        raise ValueError("Stop price must be greater than 0")

    return stop_price
