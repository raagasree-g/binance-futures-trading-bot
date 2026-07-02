# Binance Futures Trading Bot

A command-line Python application that places **BUY** and **SELL** **Market** and **Limit** orders on the **Binance Futures Testnet/Demo Trading** environment.

---

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY and SELL support
- Command Line Interface (CLI)
- Input Validation
- Logging
- Exception Handling

---

## Project Structure

```text
binance-futures-trading-bot/
│
├── bot/
│   ├── client.py
│   ├── cli.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/raagasree-g/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

Install the required dependencies.

```bash
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

### Place a MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000
```

---

## Validation

The application validates the following inputs:

- BUY / SELL order side
- MARKET / LIMIT order type
- Quantity must be greater than 0
- LIMIT orders require a valid price

---

## Logging

Application logs are stored in:

```text
logs/trading.log
```

The log file records:

- Order requests
- Order responses
- Successful executions
- Errors and exceptions

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
- Binance Futures Testnet account
- Binance Testnet API Key and Secret

---

## Author

**Raaga Sree**