import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
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
    print(f"Average Price   : {response.get('avgPrice', 'N/A')}")
    print(f"Client Order ID : {response.get('clientOrderId', 'N/A')}")
    print(f"Time In Force   : {response.get('timeInForce', 'N/A')}")

    print("=" * 55)
    print("✅ Order placed successfully.\n")


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
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        help="Price (required only for LIMIT orders)"
    )

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper().strip()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        if order_type == "MARKET":
            response = place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
            )

        else:
            price = validate_price(args.price)

            response = place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )

        print_order_summary(response)

    except ValueError as e:
        print("\n❌ Input Validation Error")
        print(f"Reason: {e}")

    except Exception as e:
        print("\n❌ Order Failed")
        print(f"Reason: {e}")