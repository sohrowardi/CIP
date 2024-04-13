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
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]
        ethereum_price = data["ethereum"]["usd"]
        return {"BTC": bitcoin_price, "ETH": ethereum_price}
    else:
        print("Failed to fetch cryptocurrency prices")
        return None

def main():
    btc = Cryptocurrency("BTC", "Bitcoin", 0)
    eth = Cryptocurrency("ETH", "Ethereum", 0)
    portfolio = Portfolio()

    while True:
        prices = get_crypto_prices()
        if prices is None:
            break

        btc.price = prices["BTC"]
        eth.price = prices["ETH"]

        print("Bitcoin Price:", btc.price)
        print("Ethereum Price:", eth.price)

        print("Balance:", portfolio.balance)
        print("BTC:", portfolio.assets.get("BTC", 0))
        print("ETH:", portfolio.assets.get("ETH", 0))

        action = input("Enter 'buy' or 'sell': ")
        if action == "buy":
            symbol = input("Enter cryptocurrency symbol (BTC/ETH): ")
            amount = float(input("Enter amount to buy: "))
            if symbol == "BTC":
                portfolio.buy(btc, amount)
            elif symbol == "ETH":
                portfolio.buy(eth, amount)
        elif action == "sell":
            symbol = input("Enter cryptocurrency symbol (BTC/ETH): ")
            amount = float(input("Enter amount to sell: "))
            if symbol == "BTC":
                portfolio.sell(btc, amount)
            elif symbol == "ETH":
                portfolio.sell(eth, amount)
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
