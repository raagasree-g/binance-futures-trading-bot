# Binance Futures Trading Bot

A Python CLI application for placing Binance Futures Testnet MARKET, LIMIT, and bonus STOP_LIMIT orders.

---

## Features

- Place MARKET Orders
- Place LIMIT Orders
- Place STOP_LIMIT Orders
- BUY / SELL Support
- Command Line Interface (CLI)
- Order Confirmation Prompt
- Input Validation
- Logging
- Exception Handling

---

## Project Structure

```text
binance-futures-trading-bot/
|
|-- bot/
|   |-- __init__.py
|   |-- client.py
|   |-- cli.py
|   |-- orders.py
|   |-- validators.py
|   |-- logging_config.py
|
|-- logs/
|   |-- trading.log
|
|-- .env
|-- .gitignore
|-- README.md
|-- requirements.txt
|-- main.py
```

---

## Installation

```bash
git clone https://github.com/raagasree-g/binance-futures-trading-bot.git
cd binance-futures-trading-bot
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Usage

### Market Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000
```

### Stop-Limit Order

```bash
python main.py --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.001 --price 109500 --stop-price 110000
```

A confirmation prompt is displayed before any order is submitted.

---

## Validation

The application validates:

- BUY / SELL order side
- MARKET / LIMIT / STOP_LIMIT order type
- Quantity greater than 0
- LIMIT price required
- STOP_LIMIT price required
- STOP_LIMIT stop price required

---

## Logging

Logs are written automatically to:

```text
logs/trading.log
```

The log file stores:

- Order Requests
- Order Responses
- Successful Executions
- Errors

---

## Assumptions

- The user has valid Binance Futures Testnet API credentials.
- API credentials are stored securely in a `.env` file.
- The Binance Futures Testnet service is available and reachable.
- The trading symbol provided (for example, `BTCUSDT`) is supported by Binance Futures.
- LIMIT orders require a valid price parameter.
- MARKET orders execute at the best available market price on the Binance Futures Testnet.

---

## Requirements

- Python 3.10+
- python-binance
- python-dotenv

---

## Author

Raaga Sree
