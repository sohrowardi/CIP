# Crypto Investment Simulator

## Overview
This simulator allows users to emulate investing in various cryptocurrencies and observe the potential performance of their investments over time.

## Features
- Simulate buying and selling of popular cryptocurrencies.
- Check real-time prices of cryptocurrencies.
- Manage a virtual portfolio with an initial balance.
- Perform transactions based on USD or cryptocurrency amount.

## Installation

To run this simulator, you will need Python and the `requests` library installed on your machine.

```bash
pip install requests
```

## Usage
Run the `crypto_investment_simulator.py` script in your terminal:
```bash
python crypto_investment_simulator.py
```
Follow the prompts to buy or sell cryptocurrencies.

## How It Works
The simulator includes two main classes:

- `Cryptocurrency`: Represents a cryptocurrency with a symbol, name, and price.
- `Portfolio`: Manages the user’s balance and assets.
- `The get_crypto_prices` function fetches real-time prices using the CoinGecko API.

Transactions are parsed and executed through the `parse_transaction` function, allowing users to input commands such as ‘buy bitcoin 100’ or ‘sell bitcoin 100$’.