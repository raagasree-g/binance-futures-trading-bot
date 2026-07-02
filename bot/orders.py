from binance.exceptions import BinanceAPIException

from bot.client import client
from bot.logging_config import logger


def _log_order_response(order_label, response):
    """Log the common response fields returned after an order request."""
    logger.info(f"{order_label} placed successfully.")
    logger.info(
        f"Order ID={response['orderId']} | "
        f"Status={response['status']} | "
        f"ExecutedQty={response['executedQty']}"
    )


def _submit_order(order_label, request_message, **order_params):
    """Submit an order to Binance Futures with consistent logging."""
    try:
        logger.info(request_message)

        response = client.futures_create_order(**order_params)
        _log_order_response(order_label, response)

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order on Binance Futures.
    """
    return _submit_order(
        "Market Order",
        f"Market Order Request | Symbol={symbol} | Side={side} | Quantity={quantity}",
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
    )


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order on Binance Futures.
    """
    return _submit_order(
        "Limit Order",
        f"Limit Order Request | Symbol={symbol} | Side={side} | "
        f"Quantity={quantity} | Price={price}",
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC",
    )


def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    """
    Place a STOP_LIMIT order on Binance Futures.

    Binance Futures uses the API type "STOP" for stop-limit orders.
    """
    return _submit_order(
        "Stop Limit Order",
        f"Stop Limit Order Request | Symbol={symbol} | Side={side} | "
        f"Quantity={quantity} | Price={price} | StopPrice={stop_price}",
        symbol=symbol,
        side=side,
        type="STOP",
        quantity=quantity,
        price=price,
        stopPrice=stop_price,
        timeInForce="GTC",
    )
