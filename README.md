# Binance Futures Trading Bot

A command-line Python application that places BUY and SELL Market and Limit orders on Binance Futures Testnet/Demo Trading.

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY and SELL support
- Command Line Interface (CLI)
- Input Validation
- Logging
- Exception Handling

## Project Structure

```
trading_bot/
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

## Installation

Clone the repository.

```bash
git clone <repository_url>
cd trading_bot
```

Install dependencies.

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file.

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Usage

### Market Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000
```

## Validation

The application validates:

- BUY / SELL
- MARKET / LIMIT
- Quantity > 0
- Price required for LIMIT orders

## Logging

Logs are stored in:

```
logs/trading.log
```