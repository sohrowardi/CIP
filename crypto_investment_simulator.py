import requests

class Cryptocurrency:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

class Portfolio:
    def __init__(self):
        self.balance = 10000
        self.assets = {}

    def buy(self, cryptocurrency, amount):
        cost = cryptocurrency.price * amount
        if cost > self.balance:
            print("Insufficient balance")
            return
        self.balance -= cost
        if cryptocurrency.symbol in self.assets:
            self.assets[cryptocurrency.symbol] += amount
        else:
            self.assets[cryptocurrency.symbol] = amount

    def sell(self, cryptocurrency, amount):
        if cryptocurrency.symbol not in self.assets or self.assets[cryptocurrency.symbol] < amount:
            print("Insufficient assets")
            return
        self.balance += cryptocurrency.price * amount
        self.assets[cryptocurrency.symbol] -= amount

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,binancecoin,tether,ripple,cardano,solana,polkadot,dogecoin,litecoin,chainlink,usd-coin,stellar,vechain,theta-token,eos,bitcoin-cash,tron,iota,wrapped-bitcoin",
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        data = response.json()
        prices = {}
        for crypto_id, crypto_data in data.items():
            prices[crypto_id.upper()] = crypto_data.get("usd", 0)
        return prices
    except requests.RequestException as e:
        print("Error fetching cryptocurrency prices:", e)
        return None

def parse_transaction(transaction):
    parts = transaction.split()
    if len(parts) < 3:
        return None, None, None
    action = parts[0].lower()
    symbol = parts[1].upper()
    amount_str = parts[2].replace('$', '')
    try:
        amount = float(amount_str)
    except ValueError:
        return None, None, None
    return action, symbol, amount


def main():
    portfolio = Portfolio()

    while True:
        prices = get_crypto_prices()
        if prices is None:
            break

        for symbol, price in prices.items():
            # Update cryptocurrency prices
            setattr(portfolio, symbol.lower(), Cryptocurrency(symbol, symbol.capitalize(), price))

        # Print cryptocurrency prices
        for symbol, cryptocurrency in vars(portfolio).items():
            if isinstance(cryptocurrency, Cryptocurrency):
                print(f"{cryptocurrency.name} Price:", cryptocurrency.price)

        print("Balance:", portfolio.balance)
        for symbol, amount in portfolio.assets.items():
            print(f"{symbol}: {amount}")

        transaction = input("Enter transaction (e.g., 'buy bitcoin 100' or 'sell bitcoin 100$'): ").strip()
        action, symbol, amount = parse_transaction(transaction)
        if action == "buy":
            cryptocurrency = getattr(portfolio, symbol.lower(), None)
            if cryptocurrency:
                if '$' in transaction:
                    amount_in_dollars = amount
                    amount = amount_in_dollars / cryptocurrency.price
                portfolio.buy(cryptocurrency, amount)
            else:
                print("Invalid cryptocurrency symbol")
        elif action == "sell":
            cryptocurrency = getattr(portfolio, symbol.lower(), None)
            if cryptocurrency:
                if '$' in transaction:
                    amount_in_dollars = amount
                    amount = amount_in_dollars / cryptocurrency.price
                portfolio.sell(cryptocurrency, amount)
            else:
                print("Invalid cryptocurrency symbol")
        else:
            print("Invalid transaction format")

if __name__ == "__main__":
    main()
