from binance.exceptions import BinanceAPIException

from bot.client import client
from bot.logging_config import logger


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

        logger.info("Market Order placed successfully.")
        logger.info(
            f"Order ID={response['orderId']} | "
            f"Status={response['status']} | "
            f"ExecutedQty={response['executedQty']}"
        )

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

        logger.info("Limit Order placed successfully.")
        logger.info(
            f"Order ID={response['orderId']} | "
            f"Status={response['status']} | "
            f"ExecutedQty={response['executedQty']}"
        )

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise