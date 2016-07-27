# backtest.py

from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
    """Abstract base class providing an interface for Strategy objects.

    A strategy objetc receives a Pandas DataFrame of prices at a particular
    frequency and returns a DataFrame of signals, consisting of a timestamp and a
    long (1), hold (0) or short (-1) signal respectively.
    """
    @abstractmethod
    def generate_signals(self):
        """A method to generate the signals DataFrame is required for each
        Strategy instance.
        """
        raise NotImplementedError("generate_signals() method needs to be" \
                                  "implemented!")

class Portfolio(metaclass=ABCMeta):
    """Interface for the Portfolio class which performs the major backtesting
    work.

    The portfolio object receives a signals DataFrame and creates a series of
    of positions and cash components. Also produces an equity curve and keeps
    track of the trades.
    """
    @abstractmethod
    def generate_positions(self):
        """A method to generate the positions DataFrame needs to be defined."""
        raise NotImplementedError("genereate_positions() method needs to be" \
                                  "implemented!")

    @abstractmethod
    def backtest_portfolio(self):
        """Portfolio class requires a backtest_portfolio method that generates
        the trading orders and a continuous equity curve.
        """
        raise NotImplementedError("backtest_portfolio() method needs to be" \
                                  "implemented!")
