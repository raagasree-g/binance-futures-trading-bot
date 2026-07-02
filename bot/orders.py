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


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order on Binance Futures.
    """
    try:
        logger.info(
            f"Market Order Request | Symbol={symbol} | Side={side} | Quantity={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        _log_order_response("Market Order", response)

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order on Binance Futures.
    """
    try:
        logger.info(
            f"Limit Order Request | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        _log_order_response("Limit Order", response)

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise


def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    """
    Place a STOP_LIMIT order on Binance Futures.

    Binance Futures uses the API type "STOP" for stop-limit orders.
    """
    try:
        logger.info(
            f"Stop Limit Order Request | Symbol={symbol} | Side={side} | "
            f"Quantity={quantity} | Price={price} | StopPrice={stop_price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce="GTC",
        )

        _log_order_response("Stop Limit Order", response)

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise
