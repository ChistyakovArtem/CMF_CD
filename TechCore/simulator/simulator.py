import numpy as np
import json


class Simulator:

    def clear_simulator(self):
        self.position_a = 0
        self.position_b = 0

        self.current_price_a = None
        self.current_price_b = None

        self.cash = 0
        self.pnl = 0

        self.logs = {
            'position_a': [],
            'position_b': [],
            'current_price_a': [],
            'current_price_b': [],
            'cash': [],
            'pnl': []
        }

    def __init__(self):
        self.position_a = 0
        self.position_b = 0

        self.current_price_a = None
        self.current_price_b = None

        self.cash = 0
        self.pnl = 0

        self.logs = {
            'position_a': [],
            'position_b': [],
            'current_price_a': [],
            'current_price_b': [],
            'cash': [],
            'pnl': []
        }

    def log_data(self):
        self.logs['position_a'].append(self.position_a)
        self.logs['position_b'].append(self.position_b)
        self.logs['current_price_a'].append(self.current_price_a)
        self.logs['current_price_b'].append(self.current_price_b)
        self.logs['cash'].append(self.cash)
        self.logs['pnl'].append(self.pnl)

    def update_positions(self, new_position_a, new_position_b):
        self.cash -= (new_position_a - self.position_a) * self.current_price_a
        self.cash -= (new_position_b - self.position_b) * self.current_price_b

        self.position_a = new_position_a
        self.position_b = new_position_b

        self.pnl = self.cash + self.position_a * self.current_price_a + self.position_b * self.current_price_b

        self.log_data()

    def save_logs(self, path):
        with open(path, 'w') as fp:
            json.dump(self.logs, fp)

    def run(self, strategy, df, window_size):
        self.clear_simulator()
        df.columns = ['price_a', 'price_b']

        for i in range(window_size, df.shape[0]):
            chunk = df.iloc[i - window_size: i]
            new_position_a, new_position_b = strategy.predict(self.position_a, self.position_b, chunk)

            self.current_price_a = df.iloc[i]['price_a']
            self.current_price_b = df.iloc[i]['price_b']

            self.update_positions(new_position_a, new_position_b)

        return self.logs
