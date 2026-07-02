import argparse

from bot.orders import (
    place_limit_order,
    place_market_order,
    place_stop_limit_order,
)
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_stop_price,
)


def print_order_summary(response):
    """Display a formatted order summary."""

    print("\n" + "=" * 55)
    print("              BINANCE ORDER SUMMARY")
    print("=" * 55)

    print(f"Symbol          : {response.get('symbol', 'N/A')}")
    print(f"Side            : {response.get('side', 'N/A')}")
    print(f"Order Type      : {response.get('type', 'N/A')}")
    print(f"Order ID        : {response.get('orderId', 'N/A')}")
    print(f"Status          : {response.get('status', 'N/A')}")
    print(f"Executed Qty    : {response.get('executedQty', 'N/A')}")
    print(f"Order Price     : {response.get('price', 'Market Price')}")
    print(f"Stop Price      : {response.get('stopPrice', 'N/A')}")
    print(f"Average Price   : {response.get('avgPrice', 'N/A')}")
    print(f"Client Order ID : {response.get('clientOrderId', 'N/A')}")
    print(f"Time In Force   : {response.get('timeInForce', 'N/A')}")

    print("=" * 55)
    print("Order placed successfully.\n")


def confirm_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    """Ask the user to confirm before placing the order."""

    print("\nOrder Details")
    print("-" * 40)
    print(f"Symbol     : {symbol}")
    print(f"Side       : {side}")
    print(f"Type       : {order_type}")
    print(f"Quantity   : {quantity}")

    if price is not None:
        print(f"Price      : {price}")

    if stop_price is not None:
        print(f"Stop Price : {stop_price}")

    print("-" * 40)

    confirmation = input("Place this order? (y/n): ").strip().lower()

    return confirmation == "y"


def run():
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET, LIMIT, or STOP_LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        help="Price (required for LIMIT and STOP_LIMIT orders)"
    )

    parser.add_argument(
        "--stop-price",
        help="Trigger price (required only for STOP_LIMIT orders)"
    )

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper().strip()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = None
        stop_price = None

        if order_type in ("LIMIT", "STOP_LIMIT"):
            price = validate_price(args.price)

        if order_type == "STOP_LIMIT":
            stop_price = validate_stop_price(args.stop_price)

        # Bonus Feature: Confirmation Prompt
        if not confirm_order(
            symbol,
            side,
            order_type,
            quantity,
            price,
            stop_price,
        ):
            print("\nOrder cancelled by user.")
            return

        if order_type == "MARKET":
            response = place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
            )
        elif order_type == "LIMIT":
            response = place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )
        else:
            response = place_stop_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
                stop_price=stop_price,
            )

        print_order_summary(response)

    except ValueError as e:
        print("\nInput Validation Error")
        print(f"Reason: {e}")

    except Exception as e:
        print("\nOrder Failed")
        print(f"Reason: {e}")
