from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy

class BuyAndHoldStrategy(Strategy):
    def on_trading_iteration(self):
        if self.first_iteration:
            aapl_price = self.get_last_price("AAPL")
            quantity = self.portfolio_value // aapl_price
            order = self.create_order("AAPL", quantity, "buy")
            self.submit_order(order)

backtesting_start = datetime(2020, 1, 1)
backtesting_end = datetime(2020, 12, 31)
BuyAndHoldStrategy.backtest(
    YahooDataBacktesting,
    backtesting_start,
    backtesting_end,
)
